from dishka import Provider, provide, Scope

from platforms.youtube.parser import YoutubeParser
from platforms.youtube.scraper import YoutubeScraper
from platforms.youtube.service import YoutubeService


class YoutubeProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_scraper(self) -> YoutubeScraper:
        return YoutubeScraper()

    @provide(scope=Scope.REQUEST)
    def get_parser(self) -> YoutubeParser:
        return YoutubeParser(base_url="BASE_URL")

    @provide(scope=Scope.REQUEST)
    def get_service(
            self,
            scraper: YoutubeScraper,
            parser: YoutubeParser,
    ) -> YoutubeService:
        return YoutubeService(
            scraper=scraper,
            parser=parser,
        )
