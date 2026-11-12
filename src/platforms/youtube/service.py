from platforms.youtube.parser import YoutubeParser
from platforms.youtube.schemas import YoutubePost
from platforms.youtube.scraper import YoutubeScraper


class YoutubeService:
    def __init__(self) -> None:
        self.scraper = YoutubeScraper()
        self.parser = YoutubeParser()

    async def get_post_info(self, url: str) -> YoutubePost:
        response = await self.scraper.get_post_info(url=url)
        return self.parser.parse(response=response)
