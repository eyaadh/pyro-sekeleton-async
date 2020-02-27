import os
import youtube_dl
import time
import asyncio
from pyro.utils.common import botCommon
from pyrogram import Client

progress_status = {}
class yt_dl:
    @staticmethod
    async def update_dl_progress(chat_id, message_id):
        client = Client(":memory:", config_file=botCommon.bot_config_file, bot_token=botCommon.bot_api_key)
        async with client:
            await client.send_message(int(chat_id), "test")

    @staticmethod
    def progress_hooks(d):
        if d["status"] == "downloading":
            tmp_dir = os.path.basename(os.path.dirname(d["filename"]))
            vid_id, chat_id, message_id = tmp_dir.split("+")
            global progress_status
            job_details = {
                f"{chat_id}+{message_id}": {
                    "status": "downloading",
                    "progress": d['downloaded_bytes'],
                    "speed": d['speed']
                }
            }
            loop = asyncio.get_running_loop()
            loop.run_until_complete(yt_dl.update_dl_progress(chat_id, message_id))

    @staticmethod
    async def dl(vid_id, chat_id, message_id):
        tmp_dir = os.path.join(botCommon.tmp_dir, f"{vid_id}+{chat_id}+{message_id}")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

        global progress_status

        job_details = {
            f"{chat_id}+{message_id}": {
                "status": "downloading",
                "progress": 0,
                "speed": 0
            }
        }
        progress_status.update(job_details)

        ydlOpts = {
            'format': "bestvideo[height<=480][ext=mp4]+bestaudio/best",
            'progress_hooks': [yt_dl().progress_hooks],
            'noplaylist': 'true',
            'outtmpl': f'{tmp_dir}/%(title)s.%(ext)s',
            'ignoreerrors': 'true'
        }
        with youtube_dl.YoutubeDL(ydlOpts) as yt:
            yt.download([f'http://www.youtube.com/watch?v={vid_id}'])
