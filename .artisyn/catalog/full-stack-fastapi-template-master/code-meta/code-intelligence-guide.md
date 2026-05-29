# Code Intelligence

Code metadata is preloaded in your steering context. Use it directly for code navigation.

## Where CODE.md Lives

```
.artisyn/catalog/{repo-name}/code-meta/{language}/CODE.md
```

If not already in your context, read the CODE.md file(s) from this path.

## How to Use

The metadata contains every function, class, and module with:
- File path and line number
- Purpose and description
- Parameters and return types
- Relationships to other code
- Important constraints (read these first when present)

## Navigation

1. **Check your context** — find the symbol by name in the loaded metadata
2. **Open directly** — use the path + line number to read actual code when needed
3. **Fallback** — only use grep/glob if the symbol isn't in your metadata

You already have the map. Don't search for what you already know.
