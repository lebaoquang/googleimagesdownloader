import re
import requests
import urllib.request

link = input("Video URL: ")

html = requests.get(link)

try:
    url = re.search('hd_src:"(.+?)"', html.text)[1]
    print("HD Video")
except:
    url = re.search('sd_src:"(.+?)"', html.text)[1]
    print("SD Video")

print("Downloading . . .")
urllib.request.urlretrieve(url, "FacebookVideo.mp4")
print("Download Successful!")