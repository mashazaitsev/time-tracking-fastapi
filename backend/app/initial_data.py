"""
Purpose: Seed initial database data (first superuser) on application startup

Structure:
    init (func): setup - Open session and call init_db
    main (func): entry - Script entry point with logging

Relationships:
    Consumes: core.db.engine, core.db.init_db
    Produces: first superuser in user table

Note:
    Run via: python app/initial_data.py (or uv run python app/initial_data.py)
    Also called by scripts/prestart.sh before app starts.
"""

import logging

from sqlmodel import Session

from app.core.db import engine, init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    """Purpose: Open database session and seed initial data via init_db"""
    with Session(engine) as session:
        init_db(session)


def main() -> None:
    """Purpose: Entry point — log and run initial data seeding"""
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
