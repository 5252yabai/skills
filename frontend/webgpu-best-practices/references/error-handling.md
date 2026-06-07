# Error Handling & Debugging

## Table of Contents

- [Error Types and Scopes](#error-types-and-scopes)
- [Shader Debugging](#shader-debugging)
- [Device Loss](#device-loss)
- [Debugging Tools](#debugging-tools)

---

## Error Types and Scopes

### Three Error Types

| Type          | Cause                             | Predictability         |
| ------------- | --------------------------------- | ---------------------- |
| Validation    | Invalid inputs, wrong usage flags | Predictable, catchable |
| Out-of-memory | GPU memory exhaustion             | Unpredictable          |
| Internal      | Driver/implementation bugs        | Rare                   |

### Error Scope Pattern

Only wrap **synchronous** code — never wrap `await`:

```js
// GOOD: narrow scope around specific operation
device.pushErrorScope("validation");
const texture = device.createTexture({
  /* ... */
});
const error = await device.popErrorScope();
if (error) console.error("Texture creation failed:", error.message);

// BAD: scope wrapping async code
device.pushErrorScope("validation");
await someAsyncOperation(); // ← scope may miss errors
device.popErrorScope();
```

### Global Error Capture

```js
device.addEventListener("uncapturederror", (event) => {
  console.error("Uncaptured WebGPU error:", event.error.message);
});
```

This suppresses console output — re-log if visibility is needed.

### Error Message Rules

- Error messages are for **human reading only**
- **Never** parse error message strings programmatically — formats vary by browser
- Use labels on GPU objects for better error messages:

```js
const buffer = device.createBuffer({
  label: "Player Transform UBO",
  size: 64,
  usage: GPUBufferUsage.UNIFORM,
});
```

### Debug Groups

```js
pass.pushDebugGroup("Render Scene");
pass.pushDebugGroup("Draw Player");
// draw calls...
pass.popDebugGroup();
pass.popDebugGroup();
```

---

## Shader Debugging

### Compilation Info

```js
const module = device.createShaderModule({ code: shaderSource });
const info = await module.getCompilationInfo();
for (const msg of info.messages) {
  console.log(
    `${msg.type} at line ${msg.lineNum}:${msg.linePos}: ${msg.message}`,
  );
}
```

### Visualization Strategy

When shaders produce wrong output:

1. Start with a **solid color** to verify the pipeline works
2. Visualize **intermediate values** as colors:

```wgsl
// Debug: visualize normals
return vec4f(normal * 0.5 + 0.5, 1.0);

// Debug: visualize UVs
return vec4f(uv, 0.0, 1.0);

// Debug: visualize depth
return vec4f(vec3f(depth), 1.0);
```

3. **Simplify** by removing code until it works, then add back incrementally
4. Distinguish vertex vs fragment shader issues early

### Validate Data Before Shaders

Ensure buffer data is correct before blaming the shader — read back buffers if needed.

### Force Error Processing

Submit an empty command to pump the WebGPU error queue:

```js
device.queue.submit([]);
```

---

## Device Loss

### Causes

- Driver crashes, resource pressure, long-running shaders
- Driver updates, browser events
- All GPU objects become unusable — must recreate everything

### Detection

```js
// Attach immediately after device creation — NEVER await directly
device.lost.then((info) => {
  console.error(`Device lost: ${info.reason} - ${info.message}`);
  if (info.reason !== "destroyed") {
    recoverFromDeviceLoss();
  }
});
```

`reason` is either `'destroyed'` (intentional) or `'unknown'`.

### Recovery Strategies

**Minimal**: Display "please refresh" message.

**GPU Restart**: Reload GPU portion without page refresh:

1. Request new adapter (consumed adapters return lost devices)
2. Request new device
3. Recreate all GPU resources

**State Restoration**: Sync restorable data to JS/localStorage:

1. Keep CPU-side copies of critical data
2. Rebuild GPU resources from cached state

### Testing Device Loss

```js
// Simulated (limited — also unmaps buffers)
device.destroy();

// Chrome: navigate to about:gpucrash
// (escalating restrictions on repeated crashes)
```

### Key Rule

Always request a **new adapter** before requesting a new device after loss.

---

## Debugging Tools

| Tool                                                                    | Purpose                                              |
| ----------------------------------------------------------------------- | ---------------------------------------------------- |
| Browser DevTools Console                                                | WebGPU prints errors here by default                 |
| [WebGPU-Dev-Extension](https://github.com/nicedoc/webgpu-dev-extension) | Stack traces for async errors, formatted WGSL errors |
| [WebGPU-Inspector](https://github.com/nicedoc/webgpu-inspector)         | Capture commands, inspect buffers/textures/calls     |
| `uncapturederror` listener                                              | Catch errors outside error scopes                    |
| `getCompilationInfo()`                                                  | Detailed shader errors with line numbers             |
