# # pytube module intro

# # 1)YouTube Object:##############

# # This is the main object in the pytube library. It represents a YouTube video and allows you to interact with it.
# # You can create a YouTube object by passing a URL (the link to the YouTube video) as a parameter.

# # yt = YouTube('https://www.youtube.com/watch?v=VIDEO_ID')


# # 2)Streams:###################

# # pytube allows you to download videos in different formats and resolutions. These are referred to as "streams."
# # Streams are represented by the yt.streams property, and you can filter them based on various attributes like resolution, file type (audio/video), etc.

# # Get all available streams
# # streams = yt.streams.all()

# # # Get the highest resolution video stream
# # highest_res = yt.streams.get_highest_resolution()

# # # Get the first audio stream (only audio, no video)
# # audio_stream = yt.streams.filter(only_audio=True).first()


# #3)Download:###################
# # The .download() method allows you to download the selected stream.
# # Download the highest resolution stream
# # highest_res.download(output_path="path_to_folder")


# #4.Audio and Video:

# # You can download only the audio or video streams.
# # For example, to download only the audio:

# # audio_stream = yt.streams.filter(only_audio=True).first()
# # audio_stream.download()

# #5.Extracting Metadata
# # You can also extract metadata, such as title, description, views, etc., of the YouTube video using the pytube library.
# # yt = YouTube('https://www.youtube.com/watch?v=VIDEO_ID')

# # # Get metadata
# # title = yt.title
# # views = yt.views
# # length = yt.length
# # author = yt.author
# # description = yt.description

# # # Display video metadata
# # print(f"Title: {title}")
# # print(f"Views: {views}")
# # print(f"Length: {length} seconds")
# # print(f"Author: {author}")
# # print(f"Description: {description[:100]}...")  # Print the first 100 characters of description


# #6).Download Audio Only
# If you want to download the audio in the best quality, you can filter for audio-only streams:
#     from pytube import YouTube

# url = 'https://www.youtube.com/watch?v=VIDEO_ID'
# yt = YouTube(url)

# # Get the best audio stream
# audio_stream = yt.streams.filter(only_audio=True).first()

# # Download the audio
# audio_stream.download(output_path="path_to_audio_folder")

# print("Audio download complete!")

# #7.Downloading a Playlist
# You can also download an entire YouTube playlist with pytube. You would use the Playlist object for this purpose.
# from pytube import Playlist

# playlist_url = 'https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID'
# playlist = Playlist(playlist_url)

# # Iterate over all videos in the playlist and download them
# for video in playlist.videos:
#     video.streams.get_highest_resolution().download()
#     print(f"Downloaded: {video.title}")


# #8.Handling Exceptions
# pytube may raise exceptions in certain cases, such as network issues, invalid URLs, or unsupported video formats. You can handle these exceptions using try-except blocks.
# from pytube import YouTube
# from pytube.exceptions import PytubeError

# url = 'https://www.youtube.com/watch?v=VIDEO_ID'

# try:
#     yt = YouTube(url)
#     yt.streams.get_highest_resolution().download()
#     print("Download complete!")
# except PytubeError as e:
#     print(f"An error occurred: {e}")

################Advanced Features##########
#1) Custom download path: You can specify the output path where the video/audio should be saved using the download() method.
#  example :-yt.streams.get_highest_resolution().download(output_path='/path/to/save/directory')

#2)Progress Bar: You can add a custom progress bar to track the download progress by using the on_progress_callback method.
# eg:-def progress_function(stream, chunk, bytes_remaining):
#     progress = (100 * (file_size - bytes_remaining)) / file_size
#     print(f"Download progress: {progress:.1f}%")

# yt = YouTube(url, on_progress_callback=progress_function)
# yt.streams.get_highest_resolution().download()
# from pytube import YouTube
# from pytube.exceptions import PytubeError  
# import yt_dlp

# url = "https://youtu.be/ttIOdAdQaUE?feature=shared"

# ydl_opts = {
#     'format': 'best',  # Download the best format available
# }

# try:
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     print("Download complete")
# except Exception as e:
#     print(f"An error occurred: {e}")

#to delete the download audio/video/file we will do in this way
import os
if os.path.exists("What is Artificial Intelligence？ ｜ ChatGPT ｜ The Dr Binocs Show ｜ Peekaboo Kidz [ttIOdAdQaUE].mp4"):
        os.remove("What is Artificial Intelligence？ ｜ ChatGPT ｜ The Dr Binocs Show ｜ Peekaboo Kidz [ttIOdAdQaUE].mp4")  # Delete the video file
        print("What is Artificial Intelligence？ ｜ ChatGPT ｜ The Dr Binocs Show ｜ Peekaboo Kidz [ttIOdAdQaUE].mp4} has been deleted.")
else:
        print("The file does not exist.")




