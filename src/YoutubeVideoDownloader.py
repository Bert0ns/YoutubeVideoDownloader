from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from tkinter import filedialog


def show_info_video(link):
    yt = YouTube(link)
    print(f"Title: {yt.title}")


def download(link, path, name_file, only_audio):
    yt_obj = YouTube(link)
    if only_audio:
        yt_obj = yt_obj.streams.get_audio_only()
        filetype = ".mp3"
    else:
        yt_obj = yt_obj.streams.get_highest_resolution()
        filetype = ".mp4"
    try:
        print("Downloading...")
        download_path = yt_obj.download(output_path=path, filename=name_file + filetype)
        print("Download is completed successfully")
        print("Download is at this path: " + download_path)
    except VideoUnavailable:
        print("An error has occurred, download FAILED")


# MAIN
url_yt = input("Enter the YouTube video URL: ")
show_info_video(url_yt)
nameFile = input("Enter the new name of the file to download: ")
while 1:
    print("Select the path of where do you want to save the video: ")
    saveFolder = filedialog.askdirectory()
    if saveFolder != "":
        break
    else:
        print("There was an issue in selecting the path, retry")
print("Path where the file will be saved: " + str(saveFolder))

while 1:
    answer = input("Do you want to download only audio? [yes / no]: ")
    if (answer != "yes") & (answer != "no"):
        print("Invalid answer, please write only [yes] or [no]")
        continue
    only_audio = answer == "yes"
    download(link=url_yt, path=saveFolder, name_file=nameFile, only_audio=only_audio)
    break
print("CREDITS -> Davide Bertoni, github.com/Bert0ns")
input("Press enter to exit")
