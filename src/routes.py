import random
import string

from aiohttp import web
from sqlalchemy import update
from sqlalchemy.future import select

from models import URL


async def generate_short_url(request):
    data = await request.json()

    long_url = data["long_url"]

    # todo handle collisions
    short_url = "".join(
        random.choices(string.ascii_letters + string.digits, k=5)
    )

    async with request.app["session"]() as session:
        async with session.begin():
            new_url = URL(long_url=long_url, short_url=short_url)
            session.add(new_url)

    return web.json_response({"short_url": short_url})


async def redirect(request):
    short_url = request.match_info["short_url"]

    async with request.app["session"]() as session:
        # instead of select and update we can use update with returning
        result = await session.execute(
            update(URL)
            .where(URL.short_url == short_url)
            .values(click_count=URL.click_count + 1)
            .returning(URL.long_url)
        )
        url = result.scalar_one_or_none()
        await session.commit()
        if not url:
            return web.HTTPNotFound()

        return web.HTTPFound(url)


async def get_click_count(request):
    short_url = request.match_info["short_url"]

    async with request.app["session"]() as session:
        result = await session.execute(
            select(URL.click_count).where(URL.short_url == short_url)
        )
        click_count = result.scalar_one_or_none()

        if click_count is None:
            return web.HTTPNotFound()
        else:
            return web.json_response({"click_count": click_count})
