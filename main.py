from typing import Literal
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import instagpy

insta = instagpy.InstaGPy()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://instagram-media-downloader.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/get_data")
async def fetch_data(url: str):
    total = 0
    media_type = Literal['mp4', 'jpg']
    post = insta.get_post_details(url)
    print(post['data'])
    media = insta.get_media_url(post)

    if type(media) == str:
        total = 1
        media_type = 'mp4'
    else:
        total = len(media) - 1
        media_type = 'jpg'
    return {
        "total": total,
        "media_type": media_type,
        "data" : media
    }
