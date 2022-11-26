import os
from bs4 import BeautifulSoup as bs
import re
from gateways import GetAllLinks, DownloadVideos

data = []
# playlist=input("paste playlist url\n")
playlist="https://www.youtube.com/watch?v=um3h13KJRxg&list=PL_yIBWagYVjwYmv3PlwYk0b4vmaaHX6aL"
playlist_response=GetAllLinks().execute(playlist_url=playlist)
soup=(bs(playlist_response,'html.parser'))
# print(f"Soup --> {soup}")
b  =  open("a.html","w",encoding="utf_8")
b.write(str(soup))
c  =  open("a.html","r",encoding="utf_8")

d = c.readlines()
lin = 0
while True:
    try:
        a = d[lin]
    except:
        print("Finished")
        break
    if '"url":"/watch?v=' in a:
        a = a.split('"url":"')
        te = 0
        while True:
            try:
                if "/watch?v=" in a[te]:
                    aa = a[te].split('",')
                    e = 0
                    while True:
                        try:
                            if "/watch?v=" in aa[e]:
                                url = "https://www.youtube.com"+aa[e]
                                #url is added in data if you want to print all url uncomment this code
                                #print(url)
                                data.append(url)
                        except:
                            break
                        e+=1
            except:
                break
            te +=1
    lin +=1
c.close()
b.close()
os.remove("a.html")
print("Given data is in list so you can print url by use this code print(data[0])\n\n")

file=open("file.py","w")
data=list(set(data))
file.write(str(data))
count=0
total_videos=1
for i in data:
    if "totalVideos" in i:
        total_videos=re.findall(r'\b\d+\b', i)[0]
        print(total_videos)
        break

for i in data:
    if "index=" in i:
        temp=i.split("index=",1)
        if str(temp[1]).isdigit():
            count+=1
            DownloadVideos().execute(url=i,count=count)
            break

print(count)
if str(count)!=str(total_videos):
    print("Some videos may be downloaded more than one time due to youtube algorithms")
