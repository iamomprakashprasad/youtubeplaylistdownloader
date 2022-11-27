import requests
from pytube import YouTube as yt
import os

class GetAllLinks:
    """
    get all links from youtube specific to playlist
    """
    def __init__(self):
        self.session=requests.session()

    def execute(self,playlist_url):
        """
        main method to get all links
        """
        print(f"Playlist Url --> {playlist_url}")
        response=self.session.get(url=playlist_url)
        response.raise_for_status()
        print(f"response --> {response}")
        return response.text


class DownloadVideos:
    def __init__(self):
        self.session= requests.session()

    def execute(self,url,count):
        """
        main method to download videos
        """
        yt_video=yt(url=url)
        print(f"Downloading videos --> {yt_video.title} count --> {count}")
        home_directory= os.path.expanduser( '~' )
        downloads_path= os.path.join(home_directory,"Downloads")
        yt(url=url).streams.get_highest_resolution().download(output_path=downloads_path)
        print(f"video downloaded --> {yt_video.title}")

