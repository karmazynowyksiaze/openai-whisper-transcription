# OpenAI Whisper Transcription

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/python-3.8+-yellow" alt="Python version">
</p>

A simple web application for transcribing audio files using OpenAI's Whisper model. Upload audio files and get text transcriptions easily.

## Features

- ✅ Audio file upload and transcription
- ✅ Text file download
- ✅ Clean, user-friendly interface
- ✅ Support for various audio formats
- ✅ Easy deployment options

## Demo

The application is currently available at: [http://51.20.108.26](http://51.20.108.26)

## Table of Contents

- [Local Installation](#local-installation)
- [Server Deployment](#server-deployment)
- [Reverse Proxy Configuration](#reverse-proxy-configuration)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/karmazynowyksiaze/openai-whisper-transcription.git
   cd openai-whisper-transcription
   ```

2. Open command prompt in the downloaded repository directory

3. Update pip:
   ```bash
   pip install --upgrade pip
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Access the application in your browser:
   ```
   http://127.0.0.1:5000
   ```

## Server Deployment

1. Update and upgrade packages:
   ```bash
   apt update && apt upgrade
   ```

2. Install required packages:
   ```bash
   apt install nginx git python python3-venv -y
   ```

3. Create and prepare application directory:
   ```bash
   mkdir /app/
   chmod a+rwx /app
   cd /app
   ```

4. Clone the repository:
   ```bash
   git clone https://github.com/karmazynowyksiaze/openai-whisper-transcription.git
   cd openai-whisper-transcription
   ```

5. Set up Python virtual environment:
   ```bash
   python3 -m venv whisperenv
   source whisperenv/bin/activate
   ```

6. Install dependencies and run:
   ```bash
   pip install -r requirements.txt
   flask run
   ```

## Reverse Proxy Configuration

1. Copy the Nginx configuration file:
   ```bash
   cp /app/openai-whisper-transcription/nginx-reverseproxy_flask.conf /etc/nginx/sites-available/
   ```

2. Enable the site:
   ```bash
   sudo ln -s /etc/nginx/sites-available/nginx-reverseproxy_flask.conf /etc/nginx/sites-enabled/
   ```

3. Restart Nginx:
   ```bash
   sudo systemctl restart nginx
   ```

## Troubleshooting

### 413 Request Entity Too Large

If you encounter this error when uploading large files, you need to modify the Nginx configuration:

1. Open your Nginx configuration file:
   ```bash
   sudo nano /etc/nginx/sites-available/nginx-reverseproxy_flask.conf
   ```

2. Add or modify the following line in the server block:
   ```
   client_max_body_size 100M;  # Adjust size as needed
   ```

3. Restart Nginx:
   ```bash
   sudo systemctl restart nginx
   ```

### File Download Issues

If files are displayed in the browser instead of being downloaded:

1. Make sure your download routes are properly configured with correct headers:
   ```python
   @app.route('/download/<filename>')
   def download_file(filename):
       file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
       return send_file(
           file_path,
           as_attachment=True,
           download_name=filename,
           mimetype='text/plain'
       )
   ```

2. Ensure all required imports are present:
   ```python
   from flask import send_file
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model
- [Flask](https://flask.palletsprojects.com/) for the web framework
