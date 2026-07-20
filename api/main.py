
import uvicorn
import uuid
import shutil
import os
from fastapi import FastAPI, UploadFile, HTTPException
from pathlib import Path

#initialize FastAPI instance
app = FastAPI(title="Video Processing Pipeline", version="1.0.0")

#upload directory - where video uploads will be stored
UPLOAD_DIR = "raw"

#if directory does not exist -> create directory
os.makedirs(UPLOAD_DIR, exist_ok=True)

print(UPLOAD_DIR)

def validate_video_file(file: UploadFile) -> bool:
    """
    Basic validation — check the content type is a video.
    """

    allowed_types = {
        "videp/mp4",
        "video/x-matroska", #.mkv
        "video/quicktime", #.mov
        "video/x-msvideo", #.avi
    }

    return file.content_type in allowed_types


def save_upload(file: UploadFile, job_id: str) -> str:
    """
    Saves the uploaded file to raw/<job_id>/original.<ext>
    Returns the path where the file was saved.
    """

    #extract the file extension 
    ext = os.path.splitext(file.filename)[-1]   

    #create destination folder raw/job_id
    dest_folder = os.path.join(UPLOAD_DIR, job_id)

    #create destination directory
    os.makedirs(dest_folder, exist_ok=True)

    dest_path = os.path(dest_folder, f"original{ext}")

    #Write file to disk
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return dest_path


#root GET endpoint
@app.get("/")
async def root():
    return {"message": "Video Processing Pipeline" }


#POST endpoint for receiving video file
@app.post("/upload")
async def upload_file(file: UploadFile):
    return 0

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)