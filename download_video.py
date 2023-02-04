from pytube import YouTube

url = "https://youtu.be/oUS03TWmZEI"

yt = YouTube(url)

video = yt.streams.filter(res='1080p', fps=50).first()
video.download()