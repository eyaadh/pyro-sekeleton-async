import asyncio
import pyro
from pyro.bot import bot


async def main():
    await bot().start()
    await bot().idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
