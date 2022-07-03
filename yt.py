import youtube_dl

url = input("Enter the URL of the video: ")
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        url,
        download=True
    )

if 'entries' in result:
    video = result['entries'][0]
else:
    video = result

video_url = video['url']
video_title = video['title']

print(f'"{video_title}" downloaded !! ')

