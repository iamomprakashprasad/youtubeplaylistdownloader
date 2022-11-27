# Steps to setup

git clone https://github.com/iamomprakashprasad/youtubeplaylistdownloader.git
cd youtubeplaylistdownloader
virtualenv -p python3 .venv
pip install -r requirements.txt
uvicorn main:app


Method 1: 
Change the value of playlist_link and opent localhost fastapi in firefox

Method 2:
by default it will download https://www.youtube.com/playlist?list=PL67ERKsdJZ0iUgn8rDKdI5r4bhINesEpG 
open in postman hit localhost fastapi with params {"request":"playlist_link"}