from aiohttp import web
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import DATABASE_URL, SERVER_PORT
from logs import configure_logging
from routes import generate_short_url, get_click_count, redirect


def create_app():
    app = web.Application()
    app.router.add_post("/api/generate_short_url/", generate_short_url)
    app.router.add_get(
        "/api/count/{short_url:[a-zA-Z0-9]{5}}", get_click_count
    )
    app.router.add_get("/{short_url:[a-zA-Z0-9]{5}}", redirect)

    engine = create_async_engine(DATABASE_URL, echo=True)
    app["session"] = async_sessionmaker(bind=engine)
    return app


if __name__ == "__main__":
    configure_logging()
    app = create_app()
    web.run_app(app, port=SERVER_PORT)
