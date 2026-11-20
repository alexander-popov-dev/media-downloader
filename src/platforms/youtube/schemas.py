from pydantic import BaseModel

class YoutubeVideo(BaseModel):
    url: str
    format: str
    resolution: str
    # height: int
    # width: int
    size: str

class YoutubeAudio(BaseModel):
    url: str
    format: str
    bitrate: str
    size: str

class YoutubePost(BaseModel):
    url: str
    title: str
    author: str
    videos: list[YoutubeVideo]
    audios: list[YoutubeAudio]
