from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import sys

is_dev_mode = len(sys.argv)>1 and sys.argv[1] == "dev"

app = FastAPI()

@app.get("/")
async def root():
    name = "dev" if is_dev_mode else "pre"
    with open(f"./backend/templates/{name}.html") as f:
        return HTMLResponse(f.read())

from ytdl import ytdl
app.get("/ytdl")(ytdl)

uvicorn.run(app)