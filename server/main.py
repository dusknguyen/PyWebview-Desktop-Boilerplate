from fastapi import FastAPI
from fastapi.responses import JSONResponse
import subprocess
import os

from fastapi.staticfiles import StaticFiles
import webview

server = FastAPI()

@server.get("/api/example")
def open_example_window():
    webview.create_window("example", "https://exmaple.com/")
    return {"message": "open example window"}



server.mount("/", StaticFiles(directory="dist", html=True), name="static")
