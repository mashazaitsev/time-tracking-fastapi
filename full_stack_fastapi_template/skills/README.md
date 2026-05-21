# full-stack-fastapi-template - AILA Skills Provider

This repository has been enabled as an AILA skills provider.

## What This Means

Your repository can now provide skills to AILA agents through the MCP server.

## Structure

- `full_stack_fastapi_template/skills/` - Skills directory
- `full_stack_fastapi_template/__init__.py` - Provider entry point
- `pyproject.toml` - Entry point configuration

## How It Works

The `get_skills_directory()` function in `__init__.py` tells the MCP server where to find skills.

## Creating Skills

Use skill-management-aila to create skills in this repository.

**Auto-enabled:** 2026-03-24
