import pytube
SAVE_PATH = "C:/" #change if you need
link = "https://www.youtube.com/watch?v=3jr67TKuH20"
yt = pytube.YouTube(link)
vdo = yt.streams.first()
vdo.download(SAVE_PATH)

print(vdo.title , 'Successfully downloaded')