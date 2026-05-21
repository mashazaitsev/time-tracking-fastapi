"""
Purpose: Configure Alembic migration environment for online and offline modes

Structure:
    get_url (func): config - Return database URL from settings
    run_migrations_offline (func): migration - Run migrations without DB connection
    run_migrations_online (func): migration - Run migrations with live DB connection

Relationships:
    Consumes: app.models.SQLModel.metadata, app.core.config.settings.SQLALCHEMY_DATABASE_URI
    Produces: Database schema migrations

Important:
    app.models MUST be imported before target_metadata is set,
    otherwise Alembic won't detect model changes for autogenerate.
"""

import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
assert config.config_file_name is not None
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from app.models import SQLModel  # noqa
from app.core.config import settings # noqa

target_metadata = SQLModel.metadata


def get_url():
    """
    Purpose: Return database connection URL from application settings

    Structure:
        url (str): output - SQLAlchemy database URI

    Relationships:
        Consumes: settings.SQLALCHEMY_DATABASE_URI
        Produces: Database URL string
    """
    return str(settings.SQLALCHEMY_DATABASE_URI)


def run_migrations_offline():
    """
    Purpose: Run migrations in offline mode (emit SQL without DB connection)

    Structure:
        url (str): internal - Database URL from get_url()

    Relationships:
        Consumes: get_url(), target_metadata
        Produces: SQL migration statements

    Flow:
        1. Get database URL
        2. Configure Alembic context with URL and metadata
        3. Run migrations within transaction
    """
    url = get_url()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    Purpose: Run migrations in online mode with live database connection

    Structure:
        configuration (dict): internal - Alembic config section
        connectable (Engine): internal - SQLAlchemy engine

    Relationships:
        Consumes: get_url(), config section, target_metadata
        Produces: Applied database migrations

    Flow:
        1. Build engine config with database URL
        2. Create connectable engine with NullPool
        3. Configure context with connection and run migrations
    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
