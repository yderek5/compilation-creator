import config
import praw
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from RedDownloader import RedDownloader
import platform

system = platform.system()
downloads_path = None

if system == "Linux":
    downloads_path = "/mnt/f/Downloads"
elif system == "Darwin":
    downloads_path = "~/Downloads"
else:
    downloads_path = "D:\Downloads"

def __init__(self):
    self.reddit = praw.Reddit(
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = config.user_agent)

def make_vid():
    vidlist = []
    for vid in os.listdir(f'{downloads_path}/downloaded'):
        vidlist.append(VideoFileClip(os.path.join(f'{downloads_path}/downloaded', vid)))

    vid = concatenate_videoclips(vidlist)
    vid.write_videofile("top10postsdaily.mp4")


def downloadtop10():
    RedDownloader.DownloadVideosBySubreddit("TikTokCringe", 10, SortBy="top", quality=360, destination=downloads_path)


downloadtop10()
make_vid()
