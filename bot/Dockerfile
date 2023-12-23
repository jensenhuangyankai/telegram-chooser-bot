FROM python:3.12.1-bullseye

WORKDIR /app

ENV TZ=Asia/Singapore \
    DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

# Install Chrome and additional required libraries
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable dbus \
    fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf \xvfb


RUN apt-get install -y xvfb xserver-xephyr tigervnc-standalone-server x11-utils gnumeric

RUN apt install -y ffmpeg

RUN pip install icecream fastapi pyTelegramBotAPI gunicorn uvicorn['standard'] tk pillow python-dotenv pyvirtualdisplay selenium webdriver-manager

ADD new_graphic_generator.py .

ADD sel.py .

ADD startup.py .

ADD telegram.py .

RUN touch /tmp/xvfb.auth

CMD ["uvicorn", "telegram:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "1"]

#host='0.0.0.0',
#     port=8001,
#     workers=1,

