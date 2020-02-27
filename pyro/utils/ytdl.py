import os
import youtube_dl
import time
import asyncio
from pyro.utils.common import botCommon

progress_status = {}
progress_status_msg_counter = {}


class yt_dl:
    @staticmethod
    async def progress_hooks(d):
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
            progress_status.update(job_details)

    @staticmethod
    async def dl(vid_id, chat_id, message_id, client):
        tmp_dir = os.path.join(botCommon.tmp_dir, f"{vid_id}+{chat_id}+{message_id}")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

        await client.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<code>Starting the download...</code>",
            parse_mode="html"
        )

        global progress_status
        global progress_status_msg_counter

        job_details = {
            f"{chat_id}+{message_id}": {
                "last_updated": time.time(),
            }
        }
        progress_status_msg_counter.update(job_details)

        job_details = {
            f"{chat_id}+{message_id}": {
                "status": "downloading",
                "progress": 0,
                "speed": 0
            }
        }
        progress_status.update(job_details)

        while progress_status[f"{chat_id}+{message_id}"]["status"] == "downloading":
            if time.time() - int(progress_status_msg_counter[f"{chat_id}+{message_id}"]['last_updated']):
                try:
                    await client.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=f"<code>{progress_status[f'{chat_id}+{message_id}']['progress']}</code>",
                        parse_mode="html"
                    )
                    job_details = {
                        f"{chat_id}+{message_id}": {
                            "last_updated": time.time(),
                        }
                    }
                    progress_status_msg_counter.update(job_details)
                except:
                    pass
            await asyncio.sleep(1)

        ydlOpts = {
            'format': "bestvideo[height<=480][ext=mp4]+bestaudio/best",
            'progress_hooks': [yt_dl().progress_hooks],
            'noplaylist': 'true',
            'outtmpl': f'{tmp_dir}/%(title)s.%(ext)s',
            'ignoreerrors': 'true'
        }
        with youtube_dl.YoutubeDL(ydlOpts) as yt:
            yt.download([f'http://www.youtube.com/watch?v={vid_id}'])

