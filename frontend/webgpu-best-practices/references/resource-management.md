# Resource Management

## Table of Contents

- [Buffer Uploads](#buffer-uploads)
- [Image Textures](#image-textures)
- [Bind Groups](#bind-groups)

---

## Buffer Uploads

### Strategy Selection

| Method                 | When to Use                                       | Complexity |
| ---------------------- | ------------------------------------------------- | ---------- |
| `writeBuffer()`        | Default for most cases, especially WASM           | Low        |
| `mappedAtCreation`     | Static data set once at creation                  | Low        |
| Staging Buffer Ring    | Frequent per-frame updates (2-3 rotating buffers) | High       |
| GPU Compute Generation | Data can be algorithmically generated             | Medium     |

### writeBuffer()

- Safest default choice. User agent handles staging internally.
- Works well for WASM apps where ArrayBuffer views may be invalidated.

### mappedAtCreation

- Best for static geometry/index buffers initialized once.
- No `COPY_DST` flag needed — eliminates CPU-side copy.

```js
const buffer = device.createBuffer({
  size: data.byteLength,
  usage: GPUBufferUsage.VERTEX,
  mappedAtCreation: true,
});
new Float32Array(buffer.getMappedRange()).set(data);
buffer.unmap();
```

### Staging Buffer Ring

- Maintain 2-3 pre-mapped staging buffers for per-frame dynamic data.
- Rotate through them to avoid stalls waiting for GPU to finish reading.
- Only use if profiling shows `writeBuffer` is a bottleneck.

### Mapped Buffer Pooling

- Pre-allocate mapped buffers and reuse them to avoid async wait overhead.
- Eliminates GPU pipeline copies vs `writeBuffer` (potential 2x gain).

**Rule**: Start with `writeBuffer`/`mappedAtCreation`. Only optimize if profiling identifies uploads as the bottleneck.

---

## Image Textures

### Loading Priority

1. **Compressed textures** (Basis Universal) — reduce GPU memory, speed uploads, improve caching
2. **WebP** — small files, lossy/lossless, transparency support
3. **PNG** — lossless fallback
4. **JPG** — ubiquitous, lossy only

### Loading from URL

Always use `fetch()` + `createImageBitmap()` instead of `HTMLImageElement`:

```js
const response = await fetch(url);
const blob = await response.blob();
const bitmap = await createImageBitmap(blob);
// Use bitmap with copyExternalImageToTexture or textureSource
```

This decodes off the main thread.

### Video Textures — CRITICAL

`GPUExternalTexture` auto-destroys as a microtask:

- **Must** create and render in the same callback
- **Never** `await` between `importExternalTexture()` and render
- **Must** create new bind groups every frame

### Canvas/OffscreenCanvas

Pass directly to `copyExternalImageToTexture()` for GPU fast paths.

### Mipmaps

WebGPU requires explicit mipmap generation:

- Render downsampled previous level into next level
- Use linear filtering with `RENDER_ATTACHMENT` usage flag

---

## Bind Groups

### Avoid `layout: 'auto'`

Auto-generated layouts are only usable with the pipeline that generated them. Use explicit `GPUBindGroupLayout` to share across pipelines:

```js
const bindGroupLayout = device.createBindGroupLayout({
  entries: [{ binding: 0, visibility: GPUShaderStage.VERTEX, buffer: {} }],
});
const pipelineLayout = device.createPipelineLayout({
  bindGroupLayouts: [bindGroupLayout],
});
```

### Group by Change Frequency

```wgsl
@group(0) @binding(0) var<uniform> perFrame : FrameData;    // Changes every frame
@group(1) @binding(0) var<uniform> perMaterial : Material;   // Changes per material
@group(2) @binding(0) var<uniform> perDraw : DrawData;       // Changes per draw call
```

Place less-frequently changing data at lower group indices.

### Maximize Reuse

- Multiple pipelines can share identical bind group layouts and instances.
- Subset reuse is valid: pipelines can use bind groups with more resources than needed.
- **Critical**: All bind group layouts in a pipeline layout must have bind groups set, even if the shader doesn't reference them.

### Uniform Buffer Consolidation

- Use a single large uniform buffer with dynamic offsets instead of individual per-object buffers.
- **256-byte minimum offset alignment** for dynamic uniform buffers.
- Reduces JS overhead by ~40%.
