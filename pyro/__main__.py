import asyncio
import nest_asyncio
from pyro.bot import bot


async def main():
    await bot().start()
    await bot().idle()

if __name__ == "__main__":
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
