import whisper

model = whisper.load_model("base")
result = model.transcribe("tst_video.mp4")
print(result["text"])