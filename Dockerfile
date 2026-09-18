FROM python:3.10-slim

WORKDIR /app

# Install runtime/build dependencies. Debian's ffmpeg package provides both
# /usr/bin/ffmpeg and /usr/bin/ffprobe, which are required by the bot.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    gcc \
    g++ \
    make \
    cmake \
    wget \
    unzip \
    libffi-dev \
    && command -v ffmpeg \
    && command -v ffprobe \
    && ffprobe -version \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Heroku worker process
CMD ["python3", "main.py"]
