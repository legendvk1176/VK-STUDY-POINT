FROM python:3.10-alpine

WORKDIR /app

COPY . .

# ffmpeg package includes both ffmpeg and ffprobe. Install the build tools
# required by the Python dependencies and Bento4 as well.
RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    ffmpeg \
    aria2 \
    make \
    g++ \
    cmake \
    wget \
    unzip

# Fail the image build early if ffprobe is not available on PATH.
RUN command -v ffprobe && ffprobe -version

RUN wget -q https://github.com/axiomatic-systems/Bento4/archive/v1.6.0-639.zip && \
    unzip v1.6.0-639.zip && \
    cd Bento4-1.6.0-639 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    cp mp4decrypt /usr/local/bin/ && \
    cd ../.. && \
    rm -rf Bento4-1.6.0-639 v1.6.0-639.zip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
