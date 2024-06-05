from typing import Union
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from lib.transcriber import Transcriber
from typing import Union

from typing import List
from lib.load_audio import load_audio

app = FastAPI()


class Segment(BaseModel):
    timestamp: List[float]
    text: str


class TranscriptionResult(BaseModel):
    text: str
    segments: List[Segment]
    execution_time: float


class ApiTranscribeResponse(BaseModel):
    res: Union[TranscriptionResult, None]
    success: bool = True
    message: Union[str, None] = None


@app.post("/transcribe", response_model=ApiTranscribeResponse)
async def read_root(audio_file: UploadFile):

    try:
        transcriber = Transcriber()
        res = transcriber.transcribe(load_audio(audio_file.file))
    except Exception as e:
        print(e)
        res = None
    return {
        "success":
        res is not None,
        "res":
        res,
        "message":
        "Transcription successful"
        if res is not None else "Transcription failed"
    }


@app.get("/")
async def index():
    return {"res": "Welcome to the API!"}
