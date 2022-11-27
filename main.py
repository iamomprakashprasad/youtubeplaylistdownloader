from fastapi import FastAPI
from core import Core
app = FastAPI()

constants="https://www.youtube.com/playlist?list=PL67ERKsdJZ0iUgn8rDKdI5r4bhINesEpG"
@app.get("/")
async def get_all_videos(request: str=constants):
    Core(request=request).execute()
    return {"message":'Videos Downloaded'}