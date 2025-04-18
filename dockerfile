# Use a base image with necessary libraries
FROM ubuntu:22.04

# Install dependencies and add the PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:xtradeb/apps \
    && apt-get update \
    && apt-get install -y \
    ungoogled-chromium \
    chromium-chromedriver \
    libnss3 \
    libgbm1 \
    tor \
    curl \
    gnupg \
    ca-certificates \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium webdriver-manager beautifulsoup4

# Copy all files from the current directory to /app
COPY . /app/

# Set working directory
WORKDIR /app

# Expose Tor's default SOCKS5 port
EXPOSE 9050

# Start Tor in the background
CMD service tor start && tail -f /dev/null
