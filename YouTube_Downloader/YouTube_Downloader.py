from pytube import YouTube

url = 'https://www.youtube.com/watch?v=vEQ8CXFWLZU'

try:
    myvideo = YouTube(url)

    print("############################## Video Title ########################")
    print(myvideo.title)

    print("############################## Thumbnail Image ########################")
    print(myvideo.thumbnail_url)

    print("################################## Downloading Video ##################")
    myvideo_stream = myvideo.streams.get_highest_resolution()
    if myvideo_stream:
        myvideo_stream.download()
        print("Download complete.")
    else:
        print("No video streams available for download.")
except Exception as e:
    print("An error occurred:", e)
