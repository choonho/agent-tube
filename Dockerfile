FROM selenium/standalone-chrome:latest

USER root

# Python 설치
RUN apt-get update && apt-get install -y python3 python3-pip

# 앱 복사 및 Python 패키지 설치
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app
WORKDIR /app

ENV YOUTUBE_URL=https://www.youtube.com/watch?v=dQw4w9WgXcQ

CMD ["python3", "youtube_agent.py"]

