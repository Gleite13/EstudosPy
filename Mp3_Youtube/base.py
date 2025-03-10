from pytubefix import YouTube
from pytubefix.cli import on_progress

link = "https://www.youtube.com/watch?v=7qtIwDi90N4"  # Coloca aqui entra as aspas o endereço do video no Youtube

yt = YouTube(link, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download(mp3=True)