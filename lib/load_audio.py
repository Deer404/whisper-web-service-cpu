from typing import BinaryIO, List
import numpy as np
import ffmpeg
from pydantic import BaseModel

SAMPLE_RATE = 16000


class AudioData(BaseModel):
    data: List[float]


def load_audio(file: BinaryIO,
               encode=True,
               sample_rate: int = SAMPLE_RATE) -> AudioData:
    if encode:
        try:
            out, _ = (ffmpeg.input("pipe:",
                                   threads=0).output("-",
                                                     format="s16le",
                                                     acodec="pcm_s16le",
                                                     ac=1,
                                                     ar=sample_rate).run(
                                                         cmd="ffmpeg",
                                                         capture_stdout=True,
                                                         capture_stderr=True,
                                                         input=file.read()))
        except ffmpeg.Error as e:
            raise RuntimeError(
                f"Failed to load audio: {e.stderr.decode()}") from e
    else:
        out = file.read()

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0
