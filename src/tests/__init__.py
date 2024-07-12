from aiohttp.test_utils import AioHTTPTestCase
from sqlalchemy import create_engine

from config import DATABASE_URL
from main import create_app
from models import Base


class TestCase(AioHTTPTestCase):

    async def setUpAsync(self):

        await super().setUpAsync()

        engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    async def get_application(self):
        return create_app()
