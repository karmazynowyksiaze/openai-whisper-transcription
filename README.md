# OpenAI Whisper Transcription

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/python-3.8+-yellow" alt="Python version">
</p>

A simple web application for transcribing audio files using OpenAI's Whisper model. Upload audio files and get text transcriptions easily.
Prosta aplikacja Webowa do transkrypcji plików audio w formacie mp3 lub mp4. Wykorzystano model OpenAI Whisper. 

## Wlasciwosci

- ✅ Audio file upload and transcription
- ✅ Text file download
- ✅ Clean, user-friendly interface
- ✅ Support for various audio formats
- ✅ Easy deployment options

## Demo

Aplikacja jest dostępna pod adresem: [http://51.20.108.26](http://51.20.108.26)

## Spis treści

- [Instalacja lokalna](#instalacja-lokalna)
- [Wdrożenie na serwerze (Dystrubucja Ubuntu)](#server-deployment)
- [Konfiguracja Reverse Proxy](#reverse-proxy-configuration)
- [Warunki licencyjne](#license)

## Instalacja lokalna

1. Pobieranie repozytorium
   ```bash
   git clone https://github.com/karmazynowyksiaze/openai-whisper-transcription.git
   cd openai-whisper-transcription
   ```

2. Otwórz CMD w katalogu pobranego repozytorium

3. Aktualizacja pip:
   ```bash
   pip install --upgrade pip
   ```

4. Instalacja bibliotek:
   ```bash
   pip install -r requirements.txt
   ```

5. Uruchomienie aplikacji:
   ```bash
   flask run
   ```

6. Dostęp do aplikacji w przeglądarce:
   ```
   http://127.0.0.1:5000
   ```

## Server Deployment

1. Aktualizacja zainstalowanych pakietów w systemie:
   ```bash
   apt update && apt upgrade
   ```

2. Instalacja wymaganych pakietów:
   ```bash
   apt install nginx git python python3-venv -y
   ```

3. Przygotowanie katalogu do aplikacji:
   ```bash
   mkdir /app/
   chmod a+rwx /app
   cd /app
   ```

4. Pobieranie repozytorium:
   ```bash
   git clone https://github.com/karmazynowyksiaze/openai-whisper-transcription.git
   cd openai-whisper-transcription
   ```

5. Ustawienie wirtualnego środowiska Python:
   ```bash
   python3 -m venv whisperenv
   source whisperenv/bin/activate
   ```

6. Instalacja wymaganych bibliotek oraz uruchomienie aplikacji:
   ```bash
   pip install -r requirements.txt
   flask run
   ```

## Reverse Proxy Configuration

1. Utworzenie pliku konfiguracyjnego nginx:
   ```bash
   cp /app/openai-whisper-transcription/nginx-reverseproxy_flask.conf /etc/nginx/sites-available/
   ```

2. Uruchomienie reverse proxy:
   ```bash
   sudo ln -s /etc/nginx/sites-available/nginx-reverseproxy_flask.conf /etc/nginx/sites-enabled/
   ```

3. Restart nginx:
   ```bash
   sudo systemctl restart nginx
   ```
## Licencja

Ten projekt jest dostępny na licencji MIT

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model
- [Flask](https://flask.palletsprojects.com/) for the web framework
