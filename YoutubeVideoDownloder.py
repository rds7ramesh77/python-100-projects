#Python program for Youtube video downloader

import pytube

link=input("inter youtube video url")

yt=pytube.Youtube(link)
yt.streams.first().download()
print("downloaded",link)