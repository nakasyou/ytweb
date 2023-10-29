from typing import Union
import uuid
import os
from fastapi.responses import JSONResponse
from yt_dlp import YoutubeDL

if not os.path.isdir("data"):
    os.mkdir("data")
with open("data/promise.txt", "w") as f:
    f.write("")
with open("data/requested.txt", "w") as f:
    f.write("")

def download(url: str) -> bytes :
    movie_id = uuid.uuid4()
    with YoutubeDL({
        'outtmpl': f'data/tmp/{movie_id}'
    }) as ydl:
        ydl.download([url])
    with open(f'data/tmp/{movie_id}.webm', "rb") as f:
        return f.read()

async def ytdl(
        mode_init: Union[str, None] = None,
        promise_id: Union[str, None] = None,
        mode_request: Union[str, None] = None,
        ):
    mode_init = bool(mode_init != None)
    mode_request = bool(mode_request != None)

    if mode_init:
        id = uuid.uuid4()
        with open("data/promise.txt", "a") as f:
            f.write(f"{id}\n")
        return id
    if mode_request:
        with open("data/promise.txt") as f:
            ids = f.read().split("\n")[:-1]
            if promise_id in ids[:2]:
                # ダウンロード可能
                with open("data/requested.txt") as f:
                    not_requested = promise_id not in f.read().split("\n")
                if not_requested:
                    # 過去にリクエストしてない
                    with open("data/requested.txt", "a") as f:
                        f.write(f"{promise_id}\n")
                    return "requested"
        return JSONResponse("400 Bad apple", 400)
    if promise_id:
        # ダウンロードチェック
        with open("data/promise.txt") as f:
            ids = f.read().split("\n")[:-1]
            if promise_id in ids[:2]:
                return {
                    "status": "downloading",
                }
            else:
                return {
                    "status": "pending"
                }
    return mode_init
