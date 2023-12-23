FROM python:3.12.1-bullseye

WORKDIR /app

ENV TZ=Asia/Singapore \
    DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

RUN apt-get install -y xvfb xserver-xephyr tigervnc-standalone-server x11-utils gnumeric


RUN pip install icecream python-dotenv pyvirtualdisplay Flask MarkupSafe


ADD . /app

#ADD templates /app/templates

#ADD static /static


CMD ["python3.12", "-m", "flask", "run", "--host=0.0.0.0"]