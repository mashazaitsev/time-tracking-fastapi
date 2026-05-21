# AILA Code Intelligence Guide

**Status:** MANDATORY  
**Priority:** CRITICAL  
**Applies To:** All code navigation and understanding tasks

---

## Overview

This repository has **advanced code intelligence** that enables instant, precise navigation without searching. You MUST use this intelligence system as your primary method for code discovery and navigation.

**What is AILA Code Intelligence:**
- Pre-extracted metadata for all code (functions, classes, modules)
- File paths, line numbers, purposes, relationships
- Embedded in steering context (zero-cost access)
- 10-50x faster than traditional search methods

---

## MANDATORY: Metadata-First Navigation

**CRITICAL RULE: Metadata is already loaded in your steering context as "meta cache".**

### Navigation Protocol (MUST Follow)

```
┌─────────────────────────────────────────────────────────────┐
│                    User asks about code                     │
└────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
            ┌────────────────────────────┐
            │  Step 1: Check Meta Cache  │
            │  (Already in your context) │
            │  MANDATORY FIRST STEP      │
            └────────────┬───────────────┘
                         │
                ┌────────┴────────┐
                │                 │
         Found  │                 │  Not Found
                ▼                 ▼
    ┌───────────────────┐   ┌───────────────────┐
    │  Step 2: Direct   │   │  Step 3: Fallback │
    │  Navigation       │   │  Search           │
    │  (fs_read)        │   │  (code/grep)      │
    └───────────────────┘   └───────────────────┘
```

---

## Step 1: Check Meta Cache (MANDATORY FIRST)

**Location:** Already loaded in your steering context

**What meta cache contains:**
```yaml
file: discovery.py
path: skill_sdk_aila/discovery.py  # ← Relative path
type: module
language: python

functions:
  - name: get_skill
    line: 297  # ← Line number
    purpose: "Retrieve complete skill definition"
    
  - name: read_resource
    line: 389
    purpose: "Read resource content from skill"
```

**How to use:**
1. Reference metadata already in your context (no file access needed)
2. Extract `path` and `line` number from cached metadata
3. Go directly to Step 2 (Direct Navigation)

**CRITICAL: Do NOT access metadata files - metadata is already loaded as "meta cache" in your steering context. Only use file access for Step 2 (reading actual code) or Step 3 (fallback search).**

---

## Step 2: Direct Navigation (Metadata Available)

**Use fs_read with exact path and line numbers:**

```python
# Metadata says: get_skill at line 297 in skill_sdk_aila/providers/base.py

# Read specific function
fs_read(
    path="skill_sdk_aila/providers/base.py",
    start_line=297,
    end_line=350  # Estimate ~50 lines
)
```

**Benefits:**
- ✅ Instant (< 0.1 seconds)
- ✅ Precise (exact function)
- ✅ Efficient (1 tool call)
- ✅ Low tokens (500-1000)

**Do NOT use grep or code search if metadata has the answer.**

---

## Step 3: Fallback Search (Only If Metadata Missing)

**Only use if metadata doesn't have the answer:**

### Option A: Code Search (If LSP Available)

```python
# Only if metadata doesn't have it
code(operation="search_symbols", symbol_name="function_name")
```

### Option B: Grep (Last Resort)

```python
# Only if code search not available
grep(pattern="function_name")
```

**After fallback search:**
- Document that metadata should be updated
- Suggest running `aila-meta --document` to regenerate

---

## Important Metadata Priority

**CRITICAL: When reading documentation metadata, ALWAYS prioritize "Important" sections.**

### What Important Sections Contain

- **Critical requirements** - Absolutely required for correct operation
- **Breaking changes** - Changes that break compatibility
- **Mandatory constraints** - Cannot be violated
- **Deployment requirements** - Critical for production/cloud
- **Security requirements** - Data integrity, access control

### Reading Priority

**When reading documentation:**
1. ✅ Read **Important** section FIRST (highest priority)
2. ✅ Treat as non-negotiable requirements
3. ✅ Do not skip or ignore
4. ✅ Ask clarifying questions if unclear
5. ✅ Verify understanding before proceeding

**Priority order:**
1. **Important** (critical requirements) ← HIGHEST PRIORITY
2. Purpose (what it does)
3. Flow (how it works)
4. Args/Returns (interface)
5. Note (additional context)
6. Example (usage)

### Example

```python
def __init__(self, stateless_http: bool = True):
    """
    Initialize MCP server.
    
    Important:
        stateless_http=True is REQUIRED for cloud deployments.
        Do not change to False - this will break cloud functionality.
    
    Args:
        stateless_http: Enable stateless HTTP mode
    """
```

**You MUST:**
- ✅ Read Important section first
- ✅ Understand: stateless_http=True is REQUIRED
- ✅ Understand: Changing to False breaks cloud
- ✅ Apply this constraint in all recommendations

---

## Tool Selection Matrix

| Task | First Choice | Second Choice | Last Resort |
|------|-------------|---------------|-------------|
| **Find function by name** | Metadata (meta cache) | code search_symbols | grep |
| **Understand purpose** | Metadata (meta cache) | fs_read docstring | code lookup |
| **Get file path** | Metadata (meta cache) | code search_symbols | grep |
| **Get line number** | Metadata (meta cache) | code search_symbols | N/A |
| **Read code** | fs_read (after metadata) | code lookup_symbols | fs_read (full file) |
| **Find relationships** | Metadata (meta cache) | code find_references | grep |
| **Search literal text** | grep | grep | grep |

---

## Examples

### ✅ CORRECT: Metadata-First

**User:** "Show me the get_skill function"

**Your response:**
```
1. Check metadata in meta cache
   → Found: skill_sdk_aila/providers/base.py, line 297
   → Purpose: "Retrieve complete skill definition"

2. Read code directly:
   fs_read("skill_sdk_aila/providers/base.py", start_line=297, end_line=350)

3. Show code to user
```

**Tool calls:** 1 (fs_read)  
**Time:** < 0.2 seconds  
**Tokens:** ~500

---

### ❌ WRONG: Search-First

**User:** "Show me the get_skill function"

**Your response:**
```
1. code search_symbols "get_skill"  ← WRONG: Metadata already has this
2. code lookup_symbols "get_skill"  ← WRONG: Unnecessary
3. Show code to user
```

**Tool calls:** 2 (code search + lookup)  
**Time:** 2-3 seconds  
**Tokens:** ~2000

**Why wrong:** Metadata already had path + line number. You wasted time and tokens.

---

### ✅ CORRECT: Fallback When Needed

**User:** "Find all functions that call database.query"

**Your response:**
```
1. Check metadata in meta cache
   → Not found: Metadata doesn't track all function calls

2. Fallback to grep:
   grep(pattern="database.query")

3. Show results to user
```

**Why correct:** Metadata doesn't have this information, so fallback is appropriate.

---

## Performance Impact

### Metadata-First vs Search-First

| Metric | Metadata-First | Search-First | Improvement |
|--------|---------------|--------------|-------------|
| **Speed** | 0.1-0.2 seconds | 2-5 seconds | **10-50x faster** |
| **Tool calls** | 1 | 2-3 | **3x fewer** |
| **Tokens** | 500-1000 | 1500-3000 | **50-70% less** |
| **Accuracy** | Exact match | May find wrong function | **100% accurate** |

---

## Constraints

**You MUST:**
- ✅ Check metadata FIRST for all code navigation tasks
- ✅ Use fs_read with exact path + line numbers from metadata
- ✅ Read Important sections FIRST when reading documentation
- ✅ Treat Important sections as non-negotiable requirements
- ✅ Only use search tools if metadata doesn't have the answer

**You MUST NOT:**
- ❌ Skip metadata check and go straight to grep/code search
- ❌ Ignore Important sections in documentation
- ❌ Use search tools when metadata already has the answer
- ❌ Search entire codebase when metadata has exact location

---

## Metadata Structure Reference

**What's in meta cache (already loaded in your steering context):**

```yaml
# Complete metadata for all files
{
  "type": "python",
  "total_files": 47,
  "files": [
    {
      "file": "discovery.py",
      "path": "skill_sdk_aila/discovery.py",  # ← Use this
      "type": "module",
      "purpose": "Multi-provider skill discovery",
      "functions": [
        {
          "name": "get_skill",
          "line": 297,  # ← Use this
          "purpose": "Retrieve complete skill definition",
          "parameters": [...],
          "important": "..."  # ← Read this FIRST
        }
      ],
      "classes": [...]
    }
  ]
}
```

**How to navigate:**
1. Find function in `files[].functions[]` (already in your context)
2. Get `path` from parent file object
3. Get `line` from function object
4. Read Important section if present
5. Use fs_read(path, start_line=line)

**Remember:** This metadata is already loaded - reference it directly from your context!

---

## When Metadata is Missing

**If metadata doesn't have what you need:**

1. Use fallback search (code/grep)
2. Inform user: "Metadata doesn't have this information"
3. Suggest: "Run `aila-meta --document` to regenerate metadata"
4. Continue with search results

**Do NOT:**
- Silently skip metadata check
- Assume metadata is always complete
- Fail if metadata is missing

---

## Summary

**AILA Code Intelligence = Metadata-First Navigation**

**The Rule:**
1. **MUST** check metadata first (meta cache in steering)
2. **MUST** use direct navigation (fs_read with path + line)
3. **MUST** read Important sections first (critical requirements)
4. **MAY** fall back to search if metadata doesn't have it

**The Benefit:**
- 10-50x faster
- 3x fewer tool calls
- 50-70% fewer tokens
- 100% accurate

**This is not optional. This is how you MUST navigate code in this repository.**

---

**Status:** MANDATORY  
**Enforcement:** STRICT  
**Applies To:** ALL code navigation tasks  
**Priority:** CRITICAL - Follow this protocol always
