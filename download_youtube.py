import pytube

link = "https://www.youtube.com/watch?v=p3yAYJTFXZw"

youtube = pytube.YouTube(link)
video = youtube.streams.get_highest_resolution()
video.download()
