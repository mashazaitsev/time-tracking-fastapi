"""Skills provider for full-stack-fastapi-template"""

from pathlib import Path

def get_skills_directory():
    """Return path to skills directory for AILA skill discovery.

    Returns:
        Path: Path to skills directory inside this package

    Important:
        Uses Path(__file__).parent which works with setuptools <70.0.
        If you upgrade to setuptools 82.0+, this may become a namespace
        package and __file__ will be None. The constraint in pyproject.toml
        prevents this issue.
    """
    return Path(__file__).parent / "skills"
