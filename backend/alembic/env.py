import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from backend.app.database import DATABASE_URL, Base 
from backend.app import models

# ensure project root is importable so `backend` package can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# Interpret the config file for Python logging.
config = context.config
fileConfig(config.config_file_name)

target_metadata = models.Base.metadata


def run_migrations_offline():
    url = DATABASE_URL
    if not url:
        url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    url = DATABASE_URL
    if not url:
        url = config.get_main_option("sqlalchemy.url")
    
    connectable = engine_from_config(
        config.get_section(config.config_ini_section) or {},
        prefix='sqlalchemy.',
        url=url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    # Only try to run online if we have a valid DATABASE_URL
    if DATABASE_URL and DATABASE_URL.strip():
        run_migrations_online()
    else:
        # Fall back to offline if no DATABASE_URL
        run_migrations_offline()
