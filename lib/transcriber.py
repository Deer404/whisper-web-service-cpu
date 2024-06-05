import time
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model_id = "models/whisper-large-v3/"
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id,
                                                  torch_dtype=torch_dtype,
                                                  low_cpu_mem_usage=True,
                                                  use_safetensors=True)
model.to(device)
processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)


class Transcriber:

    def transcribe(self, audio, language="zh"):
        print("Transcribing...")
        start_time = time.time()
        result = pipe(audio, generate_kwargs={"language": language})
        execution_time = time.time() - start_time
        print(
            f"Transcription done, took {execution_time} seconds, result: {result}"
        )
        if not isinstance(result, dict):
            raise ValueError("Result is not a dictionary")
        if result is None:
            raise ValueError("Result is None")
        return {
            'text': result.get("text"),
            'segments': result.get("chunks"),
            'execution_time': execution_time
        }
