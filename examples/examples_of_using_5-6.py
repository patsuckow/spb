"""
How to write a download file progress indicator in Python3
(the type of indicator will depend on the settings that you set)
"""

# Example № 5 (Download video from Youtube using pytube module):
# pip install pytube
from pytube import YouTube
from spb import SimpleProgressBar as spb


filesize = 0
url = 'https://www.youtube.com/watch?v=tHsOmVRjVE4&list=PLQAt0m1f9OHsun-gkQlHMc3WW94vJN3Sm&index=2&t=0s'


def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    pb.iteration = (100 * (filesize - remaining)) / filesize
    pb.loaded_bytes += len(chunk)  # for ⭳[weight] & [speed]
    pb.progress_bar()


yt = YouTube(url)
yt.register_on_progress_callback(progress)

# Please note the value of start and stop here can be omitted.
pb = spb(speed='show', load='show', color='yellow',
         end_msg=f' "{yt.title}" - download complete.')

stream = yt.streams.filter(file_extension='mp4').first()
filesize = stream.filesize
stream.download()  # this wil download in your current working directory



# Example using № 6 (Download video playlist from Youtube using pytube module):
from pytube import YouTube, Playlist
from spb import SimpleProgressBar as spb


filesize = 0
url = 'https://www.youtube.com/playlist?list=PLrCZzMib1e9qM62lMXC90SiFy7-1-kAPJ'
dir_to = '~/name_my_dir'


def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    pb.iteration = (100 * (filesize - remaining)) / filesize
    pb.loaded_bytes += len(chunk)
    pb.progress_bar()


pl = Playlist(url)
pl.parse_links()
pl.populate_video_urls()
print(f"\n Playlist: '{pl.title()}':")

for url in pl.video_urls:
    yt = YouTube(url)
    yt.register_on_progress_callback(progress)

    pb = spb(speed='show', load='show',
             end_msg=f' "{yt.title}" - download complete.')

    stream = yt.streams.filter(file_extension='mp4').first()
    filesize = stream.filesize
    stream.download(dir_to)
