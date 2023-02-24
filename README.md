## Seperate tasks
### 1. Flask application using MongoDB and Factory design pattern to building simple Rest API.
* cd flask_app
* docker-compose up --build
* the url: 0.0.0.0:8080
### 2. Memory consumption alarm that sends HTTP request API that is written in first task.
* python3 -m venv .venv
* source .venv/bin/activate
* pip install requests
* python alarm.py
* Or you can use bash script version: chmod +x alarm.sh && ./alarm.sh
