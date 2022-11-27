import os
from bs4 import BeautifulSoup as bs
import re
from gateways import GetAllLinks, DownloadVideos

class Core:
    def __init__(self,request) :
        self.data=[]
        self.playlist=request
    def execute(self):
        home_directory= os.path.expanduser( '~' )
        downloads_path= os.path.join(home_directory,"Downloads","ytplaylist.html")
        playlist_response=GetAllLinks().execute(playlist_url=self.playlist)
        soup=str((bs(playlist_response,'html.parser')))
        b  =  open(downloads_path,"w",encoding="utf_8")
        b.write(str(soup))
        c  =  open(downloads_path,"r",encoding="utf_8")

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
                                        self.data.append(url)
                                except:
                                    break
                                e+=1
                    except:
                        break
                    te +=1
            lin +=1
        c.close()
        b.close()
        os.remove(downloads_path)
        print("Given data is in list so you can print url by use this code print(data[0])\n\n")

        self.data=list(set(self.data))
        count=0
        total_videos=1
        for i in self.data:
            if "totalVideos" in i:
                total_videos=re.findall(r'\b\d+\b', i)[0]
                print(total_videos)
                break
        downloads=list()
        for i in self.data:
            if "index=" in i:
                temp=i.split("index=",1)
                if str(temp[1]).isdigit():
                    count+=1
                    downloads.append(DownloadVideos().execute(url=i,count=count))


        print(count)
        if str(count)!=str(total_videos):
            print("Some videos may be downloaded more than one time due to youtube algorithms")
