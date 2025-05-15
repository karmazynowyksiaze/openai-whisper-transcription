import whisper
import os
import sys
import srt
from datetime import timedelta

def transription(mp3_path, model_size="base"):
    if not os.path.isfile(mp3_path):
        print(f"File doesn't exist: {mp3_path}")
        return

    print (f"Loading Whisper model {model_size}...")
    model = whisper.load_model(model_size)

    print(f"File transcription {mp3_path}")
    result = model.transcribe(mp3_path, verbose=True)

    #SAVE TO FILE
    text_output = os.path.splitext(mp3_path)[0] = ".txt"
    with open(text_output, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print (f"Transcription is saved to file: {text_output}")

    #SRT FILE
    segments = result["segments"]
    subtitles = []
    for i, seg in enumerate(segments):
        start = timedelta(seconds=seg['start'])
        end = timedelta(seconds=seg['end'])
        content = seg['text'].strip()
        subtitles.append(srt.Subtitle(index=i+1, start=start, end=end, content=content))
    
    srt_output = os.path.splitext(mp3_path)[0] + ".srt"
    with open(srt_output, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    print (f"Saved SRT file: {srt_output}")

    print (f"Detected language: {result['language']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: transcription.py tst_video.mp3")
        sys.exit(1)
    
    file = sys.argv[1]
    transription(file)