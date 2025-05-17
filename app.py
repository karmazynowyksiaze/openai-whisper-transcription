from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import whisper
from datetime import timedelta
import srt
import sys

app = Flask(__name__)
UPLOAD_FOLDER="uploads"
OUTPUT_FOLDER="outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def transription(audio_path, model_size="small"):
    if not os.path.isfile(audio_path):
        print(f"File doesn't exist: {audio_path}")
        return None, None, None

    print (f"Loading Whisper model {model_size}...")
    model = whisper.load_model(model_size)

    print(f"File transcription {audio_path}")
    result = model.transcribe(audio_path, verbose=True)

    # SAVE TO FILE
    base_filename = os.path.splitext(os.path.basename(audio_path))[0]
    txt_output = os.path.join(OUTPUT_FOLDER, base_filename + ".txt")
    with open(txt_output, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"Transcription is saved to file: {txt_output}")

    # SRT FILE
    segments = result["segments"]
    subtitles = []
    for i, seg in enumerate(segments):
        start = timedelta(seconds=seg['start'])
        end = timedelta(seconds=seg['end'])
        content = seg['text'].strip()
        subtitles.append(srt.Subtitle(index=i + 1, start=start, end=end, content=content))

    srt_output = os.path.join(OUTPUT_FOLDER, base_filename + ".srt")
    with open(srt_output, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    print(f"Saved SRT file: {srt_output}")

    print(f"Detected language: {result['language']}")

    return result["text"], base_filename + ".txt", base_filename + ".srt"

@app.route("/", methods=["GET", "POST"])
def index():
    transcription_text = None
    download_link = None
    srt_link = None
    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        transcription_text, txt_filename, srt_filename = transription(path)

        if transcription_text:
            download_link = f"/download/{txt_filename}"
            srt_link = f"/download/{srt_filename}"

    return render_template("index.html", transcription=transcription_text, download_link=download_link, srt_link=srt_link)

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename,
                mimetype='text/plain'
            )
        else:
            return "Plik nie istnieje", 404
    except Exception as e:
        return f"Wystąpił błąd: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)