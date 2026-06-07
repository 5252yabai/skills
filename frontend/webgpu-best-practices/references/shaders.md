# Shader Best Practices

## Table of Contents

- [Dynamic Shader Construction](#dynamic-shader-construction)
- [Pipeline-Overridable Constants](#pipeline-overridable-constants)
- [Compute Shader Alignment](#compute-shader-alignment)
- [Shader Modularity](#shader-modularity)

---

## Dynamic Shader Construction

### Use JavaScript Template Literals

Define shaders in JavaScript strings instead of separate .wgsl files for dynamic flexibility:

```js
const shaderCode = /* wgsl */ `
  const LIGHT_COUNT = ${lightCount};
  const USE_NORMAL_MAP = ${useNormalMap};

  @fragment fn main() -> @location(0) vec4f {
    var color = vec4f(0);
    for (var i = 0u; i < LIGHT_COUNT; i++) {
      color += calculateLight(i);
    }
    return color;
  }
`;
```

### Benefits

- Replace preprocessor `#define` with string interpolation
- Enable conditional code inclusion/exclusion
- Type-safe constant injection
- VSCode: "WGSL Literal" extension provides syntax highlighting for tagged templates

---

## Pipeline-Overridable Constants

Set constants at pipeline creation time without recompiling shader source:

```wgsl
override workgroupSize: u32 = 64;
override useSRGB: bool = true;

@compute @workgroup_size(workgroupSize)
fn main() { /* ... */ }
```

```js
const pipeline = device.createComputePipeline({
  compute: {
    module: shaderModule,
    entryPoint: "main",
    constants: {
      workgroupSize: 256,
      useSRGB: 0, // false
    },
  },
});
```

### Use Cases

- Workgroup size tuning per device
- Boolean feature toggles (driver may optimize dead branches)
- Numeric constants that vary per pipeline variant
- Use `@id(N)` attribute for numeric identifiers instead of string names

---

## Compute Shader Alignment

### The vec3 Problem

Compute shaders require `vec3` on 16-byte boundaries, but vertex data often uses 12-byte stride:

```wgsl
// BAD: array<vec3f> expects 16-byte stride
@group(0) @binding(0) var<storage> positions: array<vec3f>;

// GOOD: scalar array with manual reconstruction
@group(0) @binding(0) var<storage> data: array<f32>;

fn getPosition(index: u32) -> vec3f {
  let base = index * stride + offset;
  return vec3f(data[base], data[base + 1], data[base + 2]);
}
```

### Pass Metadata as Uniforms

Use uniforms for stride/offset (not bind group `offset` which requires 256-byte alignment):

```wgsl
struct VertexInfo {
  stride: u32,    // in f32 units
  offset: u32,    // in f32 units
  count: u32,
};
@group(0) @binding(1) var<uniform> info: VertexInfo;
```

### Unpacking Compressed Data

Use WGSL builtins for packed formats:

```wgsl
let packed = data[index];
let unpacked = unpack4x8unorm(packed);     // 4 x u8 → vec4f [0,1]
let halves = unpack2x16float(packed);       // 2 x f16 → vec2f
```

Use bitmasking for 8/16-bit integers manually.

### Atomic Synchronization

For parallel modifications, use atomic operations on quantized integer values:

```wgsl
@group(0) @binding(0) var<storage, read_write> counter: atomic<u32>;

fn increment() {
  atomicAdd(&counter, 1u);
}
```

---

## Shader Modularity

### Compose with JavaScript Imports

```js
// lib/lighting.js
export const lightingCode = /* wgsl */ `
  fn calculateLight(index: u32) -> vec4f { /* ... */ }
`;

// main-shader.js
import { lightingCode } from "./lib/lighting.js";

const shader = /* wgsl */ `
  ${lightingCode}

  @fragment fn main() -> @location(0) vec4f {
    return calculateLight(0);
  }
`;
```

### Output Struct Alignment

Compute shader outputs can use properly-aligned structs since you control their layout:

```wgsl
struct OutputVertex {
  position: vec4f,  // 16-byte aligned ✓
  normal: vec4f,    // pad vec3 to vec4
  uv: vec2f,
  _pad: vec2f,      // explicit padding
};
```
