import whisper
import torch
import os
import srt
import shutil
from tkinter import Tk, filedialog, Text, Button, Label, messagebox
from datetime import timedelta


os.environ["PATH"] = os.path.abspath("ffmpeg") + os.pathsep + os.environ["PATH"]

def transkrybuj(audio_path, output_dir, model_size="medium"):
    if not os.path.isfile(audio_path):
        messagebox.showerror("Błąd", f"Plik nie istnieje: {audio_path}")
        return ""

    if not shutil.which("ffmpeg"):
        messagebox.showerror("Błąd", "Nie znaleziono ffmpeg!")
        return ""

    device = "cuda" if torch.cuda.is_available() else "cpu"
    log(f"Używane urządzenie: {device.upper()}")
    log("Ładowanie modelu...")

    model_path = os.path.join("models", "medium.pt")
    model = whisper.load_model(model_path, device=device)
    #model = whisper.load_model("medium", device=device)
    result = model.transcribe(audio_path, verbose=False)

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    text_path = os.path.join(output_dir, base_name + ".txt")
    srt_path = os.path.join(output_dir, base_name + ".srt")

    # Zapis .txt
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    log(f"Zapisano plik TXT: {text_path}")

    # Zapis .srt
    subtitles = []
    for i, seg in enumerate(result.get("segments", [])):
        start = timedelta(seconds=seg["start"])
        end = timedelta(seconds=seg["end"])
        subtitles.append(srt.Subtitle(index=i+1, start=start, end=end, content=seg["text"].strip()))
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    log(f"Zapisano plik SRT: {srt_path}")
    log(f"Wykryty język: {result['language']}")

    return result["text"]

def log(msg):
    output_box.insert("end", msg + "\n")
    output_box.see("end")

def wybierz_plik():
    path = filedialog.askopenfilename(filetypes=[("Audio/Video", "*.mp3 *.mp4 *.wav *.m4a")])
    if path:
        file_label.config(text=path)
        return path

def wybierz_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_label.config(text=folder)
        return folder

def rozpocznij_transkrypcje():
    plik = file_label.cget("text")
    folder = folder_label.cget("text")

    if not plik or not os.path.isfile(plik):
        messagebox.showerror("Błąd", "Wybierz poprawny plik audio lub wideo.")
        return
    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Błąd", "Wybierz folder wyjściowy.")
        return

    output_box.delete("1.0", "end")
    tekst = transkrybuj(plik, folder)
    if tekst:
        output_box.insert("end", "\n--- Transkrypcja ---\n" + tekst)

# GUI setup
root = Tk()
root.title("Whisper Transkrypcja (.mp3/.mp4)")
root.geometry("650x500")

Button(root, text="Wybierz plik", command=wybierz_plik).pack(pady=5)
file_label = Label(root, text="(brak pliku)", wraplength=600)
file_label.pack()

Button(root, text="Wybierz folder wyjściowy", command=wybierz_folder).pack(pady=5)
folder_label = Label(root, text="(brak folderu)", wraplength=600)
folder_label.pack()

Button(root, text="Rozpocznij transkrypcję", command=rozpocznij_transkrypcje).pack(pady=10)

output_box = Text(root, height=20, wrap="word")
output_box.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
