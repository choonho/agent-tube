FROM python:3.10-slim

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libgbm-dev \
    libgtk-3-0 \
    libxrandr2 \
    libu2f-udev \
    libvulkan1 \
    && apt-get clean

# Chrome 설치
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    apt-get clean

# 소스 복사
COPY . /app
WORKDIR /app

# 환경변수 기본값 설정
ENV YOUTUBE_URL=https://www.youtube.com/watch?v=EiHx5oEIvG4

# 실행 명령
CMD ["python", "youtube_agent.py"]

