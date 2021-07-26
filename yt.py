import pytube
SAVE_PATH = "C:/" #change if you need
link = input('Enter youtube URL')
yt = pytube.YouTube(link)
vdo = yt.streams.first()
vdo.download(SAVE_PATH)

print(vdo.title , 'Successfully downloaded')
