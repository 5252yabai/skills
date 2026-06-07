---
name: webgpu-best-practices
description: WebGPU best practices, performance optimization, and common pitfall prevention. Use when writing, reviewing, or refactoring WebGPU code — including buffer/texture management, bind group layout, shader construction, render pipeline setup, compute shaders, error handling, device loss recovery, and performance tuning. Triggers on any WebGPU-related task (createBuffer, createTexture, createRenderPipeline, createComputePipeline, WGSL shaders, GPUDevice, GPUQueue, etc.).
---

# WebGPU Best Practices

Apply these rules when writing or reviewing WebGPU code. Consult the reference files for detailed patterns and code examples.

## Critical Rules Checklist

### Resource Creation

- [ ] Use `navigator.gpu.getPreferredCanvasFormat()` for canvas texture format
- [ ] Use explicit `GPUBindGroupLayout` — avoid `layout: 'auto'` (prevents cross-pipeline reuse)
- [ ] Group bind groups by update frequency: @group(0) per-frame, @group(1) per-material, @group(2) per-draw
- [ ] Set all bind group slots in pipeline layout, even if shader doesn't reference them
- [ ] Add `label` to all GPU objects for meaningful error messages

### Buffer Management

- [ ] Default to `writeBuffer()` for most uploads
- [ ] Use `mappedAtCreation` for static data initialized once
- [ ] Respect 256-byte minimum offset alignment for dynamic uniform buffers
- [ ] Prefer single large uniform buffer with dynamic offsets over per-object buffers
- [ ] Interleave vertex attributes (position + normal + uv) in a single buffer

### Textures

- [ ] Prefer compressed formats (Basis Universal) for image textures
- [ ] Load via `fetch()` + `createImageBitmap()`, not `HTMLImageElement`
- [ ] `GPUExternalTexture` (video): create and use in same callback, never `await` between creation and render, create new bind groups every frame

### Shaders

- [ ] `array<vec3f>` in compute shaders expects 16-byte stride — use `array<f32>` with manual reconstruction for vertex data
- [ ] Use pipeline-overridable constants for workgroup size and feature toggles
- [ ] Use `getCompilationInfo()` to check shader compilation errors

### Performance

- [ ] Profile before optimizing — don't assume the bottleneck
- [ ] Consolidate indirect draw arguments into a single buffer (300x faster on Chrome/D3D12)
- [ ] Render bundles: only useful if CPU-bound and reused multiple times per frame
- [ ] Don't rebuild render bundles every frame — defeats their purpose
- [ ] Don't update unchanging uniforms every frame

### Error Handling

- [ ] Attach `device.lost` handler immediately — never `await` the promise directly
- [ ] Error scopes: wrap synchronous code only, never wrap `await`
- [ ] Register `uncapturederror` listener for global error capture
- [ ] Request new adapter before new device after device loss

## Reference Guides

Read the relevant reference file when working on specific areas:

- **[Resource Management](references/resource-management.md)** — buffer upload strategies, texture loading, bind group patterns, uniform consolidation
- **[Performance](references/performance.md)** — vertex interleaving, render bundles, indirect drawing, WebGL comparison pitfalls
- **[Shaders](references/shaders.md)** — JS template literal construction, overridable constants, vec3 alignment, compute shader patterns
- **[Error Handling](references/error-handling.md)** — error scopes, shader debugging, device loss recovery, debugging tools

## Common Mistakes Quick Reference

| Mistake                                            | Fix                                                |
| -------------------------------------------------- | -------------------------------------------------- |
| `layout: 'auto'` on pipelines                      | Use explicit `GPUBindGroupLayout`                  |
| `array<vec3f>` in storage buffers                  | Use `array<f32>` + manual vec3 reconstruction      |
| `await` inside error scope                         | Keep scopes synchronous only                       |
| `await` between `importExternalTexture` and render | Create and use in same sync callback               |
| Separate buffer per indirect draw                  | Consolidate into single indirect buffer            |
| `HTMLImageElement` for texture loading             | Use `fetch()` + `createImageBitmap()`              |
| `await device.lost` directly                       | Use `device.lost.then(callback)`                   |
| Per-object uniform buffers                         | Single buffer + dynamic offsets (256-byte aligned) |
| Separate vertex attribute buffers                  | Interleave into single buffer                      |
| Rebuilding render bundles every frame              | Only rebuild when scene structure changes          |
