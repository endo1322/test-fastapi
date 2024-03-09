from typing import Optional
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
import cv2
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/uploadfile")
async def upload_files(file: UploadFile = File(...)):
    # アップロードされたファイルの情報を出力
    print('a')
    file_info = {
        "filename": file.filename,
        "content_type": file.content_type,
    }
    print(file_info)
    return file_info
