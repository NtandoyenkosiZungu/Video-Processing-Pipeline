
import uvicorn
from fastapi import FastAPI
from pathlib import Path

#initialize FastAPI instance
app = FastAPI(title="Video Processing Pipeline", version="1.0.0")

#upload directory - where video uploads will be stored
UPLOAD_DIR = Path("raw")

#If path does not exits -> Create path
UPLOAD_DIR.mkdir(exist_ok=True)

#root GET endpoint
@app.get("/")
async def root():
    return {"message": "Video Processing Pipeline" }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)