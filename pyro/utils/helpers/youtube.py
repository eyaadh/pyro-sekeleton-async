from pyro.utils.common import botCommon
from youtube_api import YouTubeDataAPI


class youtube:
    def __init__(self):
        self.yt_key = botCommon.yt_api_key
        self.yt = YouTubeDataAPI(self.yt_key)

    async def search_yt(self, search_term):
        return self.yt.search(q=search_term, max_results=1)
