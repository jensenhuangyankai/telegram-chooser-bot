FROM python:3.12.1-bullseye

WORKDIR /app

ENV TZ=Asia/Singapore \
    DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

RUN apt-get install -y xvfb xserver-xephyr tigervnc-standalone-server x11-utils gnumeric

RUN apt-get install -y ghostscript



RUN pip install icecream fastapi pyTelegramBotAPI gunicorn uvicorn['standard'] tk pillow python-dotenv pyvirtualdisplay


ADD graphic_generator.py .

ADD startup.py .

ADD telegram.py .

RUN mkdir eps

RUN mkdir png

CMD ["python3.12", "telegram.py"]

