# Use Ubuntu as the base image
FROM ubuntu:22.04

# Install necessary dependencies including Tor and Chromium
RUN apt-get update && apt-get install -y \
    tor \
    chromium-browser \
    chromium-chromedriver \
    python3-pip \
    libnss3 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Install necessary Python dependencies
RUN pip3 install selenium webdriver-manager beautifulsoup4

# Copy all files from the current directory to /app
COPY pythoncode_one.py /app/pythoncode_one.py

# Set working directory
WORKDIR /app

# Expose Tor's default SOCKS5 port
EXPOSE 9050

# Start Tor in the background
CMD service tor start && tail -f /dev/null
