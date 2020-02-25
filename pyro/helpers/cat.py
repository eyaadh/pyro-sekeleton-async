import os
import aiohttp
import aiofiles
import mimetypes
import secrets
from pyro.utils.common import botCommon


class cat:
    def __init__(self):
        self.cat_endpoint = "https://cataas.com/cat"
        self.cat_say_endpoint = "https://cataas.com/cat/cute/says/"
        self.tmp_dir = botCommon.tmp_dir

        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

    async def random_cat(self):
        async with aiohttp.ClientSession() as catSession:
            async with catSession.get(self.cat_endpoint) as resp:
                tmp_file_name = f"{secrets.token_hex(4)}.{mimetypes.guess_extension(resp.headers['Content-Type'])}"
                tmp_file = os.path.join(self.tmp_dir, tmp_file_name)
                if resp.status == 200:
                    async with aiofiles.open(tmp_file, mode="wb") as catFile:
                        async for chunk in resp.content.iter_any():
                            await catFile.write(chunk)

                return tmp_file

    async def cat_says(self, say_txt):
        async with aiohttp.ClientSession() as catSession:
            async with catSession.get(self.cat_endpoint) as resp:
                async with catSession.get(f"{self.cat_say_endpoint}{say_txt}") as resp:
                    tmp_file_name = f"{secrets.token_hex(4)}.{mimetypes.guess_extension(resp.headers['Content-Type'])}"
                    tmp_file = os.path.join(self.tmp_dir, tmp_file_name)
                    if resp.status == 200:
                        async with aiofiles.open(tmp_file, mode="wb") as catFile:
                            async for chunk in resp.content.iter_any():
                                await catFile.write(chunk)

                    return tmp_file
