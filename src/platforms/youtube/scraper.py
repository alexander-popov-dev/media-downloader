import asyncio

import yt_dlp


class YoutubeScraper:

    def download_video(self, url: str, height: int, out_dir: str = "downloads") -> None:
        container = "mp4" if height <= 1080 else "mkv"
        opts = {
            "format": f"bv*[height={height}]+ba/b[height={height}]",
            "format_sort": ["ext"] if height <= 1080 else [],
            "merge_output_format": container,
            "outtmpl": f"{out_dir}/%(title).150B [{height}p].%(ext)s",
            "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])

    def download_audio(self, url: str, format_id: str, out_dir: str = "downloads") -> None:
        opts = {
            "format": format_id,
            "outtmpl": f"{out_dir}/%(title).150B [audio].%(ext)s",
            "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])

    @staticmethod
    async def get_post_info(url: str) -> dict:
        with yt_dlp.YoutubeDL() as ydl:
            result = await asyncio.to_thread(ydl.extract_info, url=url)
            return dict(result)