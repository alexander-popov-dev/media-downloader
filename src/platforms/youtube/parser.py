from urllib.parse import urlencode

from src.platforms.youtube.schemas import YoutubeAudio, YoutubePost, YoutubeVideo


class YoutubeParser:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    @staticmethod
    def _has(codec: str | None) -> bool:
        return codec not in (None, "none")

    @staticmethod
    def _size(fmt: dict) -> float:
        return fmt.get("filesize") or fmt.get("filesize_approx") or 0

    @staticmethod
    def _fmt_size(size: float) -> str:
        if not size:
            return "—"
        mb = size / 1_000_000
        return f"{mb / 1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB"

    def parse(self, response: dict) -> YoutubePost:
        url = response["webpage_url"]
        formats = [
            f for f in response.get("formats", [])
            if f.get("url") and f.get("protocol") == "https"
        ]

        audio_streams = [
            f for f in formats
            if self._has(f.get("acodec")) and not self._has(f.get("vcodec"))
        ]
        audio_streams.sort(key=lambda f: f.get("abr") or f.get("tbr") or 0, reverse=True)
        best_audio_size = self._size(audio_streams[0]) if audio_streams else 0

        return YoutubePost(
            url=url,
            title=response["title"],
            author=response.get("uploader") or response.get("channel") or "",
            videos=self._build_videos(formats, url, best_audio_size),
            audios=self._build_audios(audio_streams, url),
        )

    def _build_videos(self, formats: list[dict], url: str, audio_size: float) -> list[YoutubeVideo]:
        by_height: dict[int, dict] = {}
        for f in formats:
            h = f.get("height")
            if not h or not self._has(f.get("vcodec")):
                continue
            if h not in by_height or self._size(f) > self._size(by_height[h]):
                by_height[h] = f

        videos = []
        for h, f in sorted(by_height.items(), reverse=True):
            has_audio = self._has(f.get("acodec"))
            total = self._size(f) + (0 if has_audio else audio_size)
            videos.append(YoutubeVideo(
                url=f"{self._base_url}/youtube/download/video?" + urlencode({"url": url, "height": h}),
                format="MP4" if h <= 1080 else "MKV",
                resolution=f"{h}p",
                size=self._fmt_size(total),
            ))
        return videos

    def _build_audios(self, audio_streams: list[dict], url: str) -> list[YoutubeAudio]:
        by_bitrate: dict[int, dict] = {}
        for f in audio_streams:
            abr = round(f.get("abr") or f.get("tbr") or 0)
            if abr and abr not in by_bitrate:
                by_bitrate[abr] = f

        audios = []
        for abr, f in sorted(by_bitrate.items(), reverse=True):
            audios.append(YoutubeAudio(
                url=f"{self._base_url}/youtube/download/audio?" + urlencode({"url": url, "format_id": f["format_id"]}),
                format=(f.get("ext") or "").upper(),
                bitrate=f"{abr} kbps",
                size=self._fmt_size(self._size(f)),
            ))
        return audios