# Code Intelligence

This project has pre-extracted code metadata in CODE.md files. Use them to understand the codebase before searching.

## CODE.md Files

Read these files to understand the codebase structure, functions, classes, and relationships:

- `.artisyn/catalog/full-stack-fastapi-template-master/code-meta/python/CODE.md` — python (46 files)
- `.artisyn/catalog/full-stack-fastapi-template-master/code-meta/typescript/CODE.md` — typescript (104 files)

## Protocol

1. **Read CODE.md** — contains every function/class with file path, line number, purpose, and relationships
2. **Navigate directly** — use the path + line from metadata to open exact code locations
3. **Fallback to search** — only use grep/glob if CODE.md doesn't cover what you need

## What CODE.md Gives You

- File paths and line numbers for every symbol
- Function signatures, parameters, return types
- Purpose descriptions and business context
- Module relationships and data flow
- Important constraints and requirements (in `important` fields — read these first)

Reading CODE.md replaces 15-40 file reads with a single file that maps the entire codebase.
