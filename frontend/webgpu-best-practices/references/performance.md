# Performance Optimization

## Table of Contents

- [Vertex Data](#vertex-data)
- [Render Bundles](#render-bundles)
- [Indirect Drawing](#indirect-drawing)
- [WebGL Comparison Pitfalls](#webgl-comparison-pitfalls)
- [General Optimization Rules](#general-optimization-rules)

---

## Vertex Data

### Interleave Attributes

Store position, normal, texcoord together per vertex instead of separate buffers:

```js
// BAD: separate buffers
// positions: [x,y,z, x,y,z, ...]
// normals:   [x,y,z, x,y,z, ...]

// GOOD: interleaved
// [pos.x, pos.y, pos.z, norm.x, norm.y, norm.z, uv.u, uv.v, ...]
```

This dramatically improves cache locality (~600% improvement in multi-object scenarios).

### Offset-Aware Matrix Math

Use offset-aware functions that write directly into the target typed array instead of creating temporary arrays:

```js
// BAD: creates temporary Float32Array
const matrix = mat4.multiply(a, b);
buffer.set(matrix, offset);

// GOOD: write directly to target
mat4.multiply(a, b, new Float32Array(buffer, byteOffset, 16));
```

~7% performance gain.

---

## Render Bundles

### When to Use

- CPU-bound applications with many draw calls
- Static or mostly-static scenes
- **Not helpful** if GPU-bound

### Capabilities and Limits

**Can do**: Set pipeline, bind groups, vertex/index buffers, draw calls
**Cannot do**: Set viewport/scissor, blend constants, stencil reference, occlusion queries, execute other bundles

### Best Practices

- Include as many draw calls as practical per bundle
- Only effective when executed **multiple times per frame**
- State resets before/after bundle execution — duplicate necessary state
- Update bind groups/buffers/textures between executions without re-encoding
- Use indirect draws within bundles for dynamic draw counts

**Critical Pitfall**: Rebuilding bundles every frame defeats their purpose. If content changes frequently, direct rendering may be better.

---

## Indirect Drawing

### Consolidate Indirect Buffers

Pack all indirect draw arguments into a **single** `GPUBuffer`:

```js
// BAD: separate buffer per draw
draws.forEach((d) => {
  const buf = device.createBuffer({ size: 20, usage: INDIRECT });
  // ...
});

// GOOD: single consolidated buffer
const indirectBuffer = device.createBuffer({
  size: drawCount * 20, // 5 uint32 per draw
  usage: GPUBufferUsage.INDIRECT,
});
```

### Why Consolidation Matters

Chrome's D3D12 backend executes one compute dispatch per indirect buffer for validation:

- 412 draws in separate buffers = ~3ms validation overhead
- Same draws in one buffer = ~10μs (300x faster)

### Additional Benefits

- Fewer larger allocations improve GPU performance regardless of backend
- Enables GPU-driven rendering (frustum culling in compute shaders)

---

## WebGL Comparison Pitfalls

When comparing WebGPU vs WebGL performance, ensure:

| Setting        | WebGL Default     | WebGPU Default       | Action                                         |
| -------------- | ----------------- | -------------------- | ---------------------------------------------- |
| Antialiasing   | Multisampled (on) | Single-sampled (off) | Disable WebGL AA or implement MSAA in WebGPU   |
| Canvas format  | RGBA8             | Varies               | Use `navigator.gpu.getPreferredCanvasFormat()` |
| Depth buffer   | Enabled           | Not created          | Manually create depth texture if needed        |
| Alpha blending | Premultiplied     | Opaque               | Configure identically                          |
| GPU selection  | Default           | Default              | Use same `powerPreference: 'high-performance'` |

**Never** use `preserveDrawingBuffer` in WebGL (no WebGPU equivalent).

---

## General Optimization Rules

1. **Profile before optimizing** — most apps won't need extreme optimization
2. **Avoid per-object writeBuffer calls** — batch into single large buffers
3. **Don't update unchanging properties every frame** — separate static vs dynamic data
4. **Use instancing** for hundreds of identical meshes
5. **Respect 256-byte alignment** for uniform buffer dynamic offsets
6. **Prefer fewer, larger allocations** over many small buffers
