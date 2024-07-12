import os

POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "12345")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", "url_shortener")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "db")

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DATABASE}"

# "postgresql+asyncpg://postgres:12345@db/url_shortener"
SERVER_PORT = os.environ.get("SERVER_PORT", 8000)
