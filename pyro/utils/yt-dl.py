import os
import youtube_dl
from pyro.utils.common import botCommon


class yt_dl:
    def __init__(self, client):
        self.tg_client = client

    async def update_yt_progress(self):
        pass

    @staticmethod
    async def progress_hooks(d):
        pass

    @staticmethod
    async def yt_dl(vid_id, chat_id, message_id):
        tmp_dir = os.path.join(botCommon.tmp_dir, f"{vid_id}+{chat_id}+{message_id}")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

        ydlOpts = {
            'format': "bestvideo[height<=480][ext=mp4]+bestaudio/best",
            'progress_hooks': [yt_dl.progress_hooks],
            'noplaylist': 'true',
            'outtmpl': f'{tmp_dir}/%(title)s.%(ext)s',
            'ignoreerrors': 'true',
            'restrictfilenames': 'true',
            'merge_output_format': 'mp4'
        }
        with youtube_dl.YoutubeDL(ydlOpts) as yt:
            yt.download(f'http://www.youtube.com/watch?v={vid_id}')
