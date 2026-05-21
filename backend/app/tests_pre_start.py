"""
Purpose: Wait for database readiness before test suite execution with retry logic

Structure:
    init (func): setup - Attempt DB connection with tenacity retry
    main (func): entry - Script entry point

Relationships:
    Consumes: core.db.engine
    Produces: (blocks until DB is ready)

Semantics:
    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]

Note:
    Run via scripts/tests-start.sh before pytest.
"""

import logging

from sqlalchemy import Engine
from sqlmodel import Session, select
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.core.db import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init(db_engine: Engine) -> None:
    """
    Purpose: Attempt single DB connection, raising on failure (retried by tenacity)

    Structure:
        db_engine (Engine): input - SQLAlchemy engine to test
    """
    try:
        # Try to create session to check if DB is awake
        with Session(db_engine) as session:
            session.exec(select(1))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    """Purpose: Entry point — wait for database readiness with retry logging"""
    logger.info("Initializing service")
    init(engine)
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
