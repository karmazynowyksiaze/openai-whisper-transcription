# CluePR PoC - Transkrypcja
* [Instalacja lokalna](#local-install)
* [Instalacja na serwerze](#server-deployment)
* [Konfiguracja reverse proxy](#reverse-proxy)



## Instalacja lokalna
1. pobrac repo
2. otworzyc cmd i wejsc do pobranego repo
3. pip install --upgrade pip
4. pip install -r requirements.txt
5. flask run
6. http://127.0.0.1:5000


## Uruchomienie na serwerze
1. apt update && apt upgrade
2. apt install nginx git python python3-venv -y
3. mdkir /app/
4. chmod a+rwx /app
5. cd /app
6. git clone
7. cd openai-whisper-translation
8. python3 -m venv whisperenv
9. source whisperenv/bin/activate
10. flask run