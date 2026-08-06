---
name: n8n
description: n8n workflow automation — Code nodes (JavaScript/Python), expressions, node configuration, validation errors, workflow architecture patterns, and n8n-mcp MCP tools. Use whenever the user mentions n8n, builds or edits an n8n workflow, writes an expression or Code node, hits a validation error, or calls any n8n-mcp tool. Load the matching reference below before acting.
---

# n8n

Entry point for all n8n work. Detailed guidance lives in `references/` — read the
matching file **before** writing workflow JSON, expressions, or Code node logic.
Never answer from memory; the references encode failure modes that are easy to get wrong.

## Routing

| Situation                                                                                      | Read                                         |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Calling **any** n8n-mcp tool (search nodes, validate, templates, manage workflows/credentials) | `references/n8n-mcp-tools-expert/SKILL.md`   |
| Designing or building a new workflow; choosing an architecture                                 | `references/n8n-workflow-patterns/SKILL.md`  |
| Setting node parameters; required fields, `displayOptions`, `patchNodeField`                   | `references/n8n-node-configuration/SKILL.md` |
| Writing `{{ }}` expressions, `$json`/`$node` access, mapping data between nodes                | `references/n8n-expression-syntax/SKILL.md`  |
| Writing a Code node in JavaScript (default)                                                    | `references/n8n-code-javascript/SKILL.md`    |
| Writing a Code node in Python (only on explicit request)                                       | `references/n8n-code-python/SKILL.md`        |
| `validate_node` / `validate_workflow` returned errors or warnings                              | `references/n8n-validation-expert/SKILL.md`  |

Multiple can apply — a new workflow with a Code node needs the patterns file _and_
the JavaScript file. Read each one you need.

## Non-negotiables

1. **MCP tools first.** If n8n-mcp tools are available, read the MCP guide before the
   first call. Wrong `nodeType` format and malformed parameter structures are the most
   common failures.
2. **Expressions are the #1 error source.** Any field referencing a previous node's
   data goes through the expression guide.
3. **JavaScript over Python** for Code nodes in ~95% of cases. Use Python only when the
   user explicitly asks or the task needs Python's standard library (regex, hashlib,
   statistics).
4. **Validation warnings are not all real.** The validation guide lists known false
   positives — check it before "fixing" something that isn't broken.

## Layout

```
references/
  n8n-mcp-tools-expert/     tool selection, parameter formats, common patterns
  n8n-workflow-patterns/    6 core architectures + per-pattern deep dives
  n8n-node-configuration/   operation-aware config, property dependencies
  n8n-expression-syntax/    syntax rules, examples, common mistakes
  n8n-code-javascript/      data access, builtins, error patterns, SplitInBatches
  n8n-code-python/          data access, stdlib, limitations
  n8n-validation-expert/    error catalog, false positives, validation loop
```

Each folder carries its own supporting `.md` files (`COMMON_PATTERNS.md`,
`ERROR_CATALOG.md`, …). Follow the links inside each `SKILL.md`.
