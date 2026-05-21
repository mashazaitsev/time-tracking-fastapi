"""
Purpose: Initialize database engine and seed first superuser on startup

Structure:
    engine (Engine): config - SQLAlchemy engine from settings
    init_db (func): output - Create first superuser if not exists

Relationships:
    Consumes: core.config.settings (SQLALCHEMY_DATABASE_URI, FIRST_SUPERUSER, FIRST_SUPERUSER_PASSWORD)
    Consumes: crud.create_user
    Produces: first superuser row in user table

Important:
    All SQLModel models MUST be imported (via app.models) before init_db runs,
    otherwise SQLModel fails to initialize relationships.
    Tables are created by Alembic migrations, NOT by init_db.
"""

from sqlmodel import Session, create_engine, select

from app import crud
from app.core.config import settings
from app.models import User, UserCreate

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def init_db(session: Session) -> None:
    """
    Purpose: Seed first superuser if not already present

    Flow:
        1. Check if FIRST_SUPERUSER email exists
        2. If not, create superuser via crud.create_user
    """
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
