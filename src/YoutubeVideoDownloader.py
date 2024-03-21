from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from tkinter import filedialog


def ShowInfoVideo(link):
    yt = YouTube(link)
    print(f"Title: {yt.title}")


def download(link, path, nameFile, onlyAudio=False):
    youtubeObject = YouTube(link)
    if onlyAudio:
        youtubeObject = youtubeObject.streams.get_audio_only()
        filetype = ".mp3"
    else:
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        filetype = ".mp4"
    try:
        print("Downloading...")
        downloadPath = youtubeObject.download(output_path=path, filename=nameFile + filetype)
        print("Download is completed successfully")
        print("Download is at this path: " + downloadPath)
    except VideoUnavailable:
        print("An error has occurred, download FAILED")


# MAIN
url_yt = input("Enter the YouTube video URL: ")
ShowInfoVideo(url_yt)
nameFile = input("Enter the new name of the file to download: ")
print("Select the path of where do you want to save the video: ")
saveFolder = filedialog.askdirectory()
print("Path where the file will be saved: " + str(saveFolder))

while (1):
    answer = input("Do you want to download only audio? [yes / no]")
    if (answer != "yes") & (answer != "no"):
        print("Invalid answer, please write only [yes] or [no]")
        continue
    onlyAudio = answer == "yes"
    download(link=url_yt, path=saveFolder, nameFile=nameFile, onlyAudio=onlyAudio)
    break
print("CREDITS -> Davide Bertoni, github.com/Bert0ns")
input("Press any key to exit")