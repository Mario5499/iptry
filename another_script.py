from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException
import subprocess
import time
import os
import signal

# pid = subprocess.Popen("service tor start && tail -f /dev/null", shell=True).pid
# time.sleep(10)
# os.kill(pid, signal.SIGINT)

# time.sleep(1)


print("Script started")

options =  webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to the Chromium binary
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")  # Disable sandboxing
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage



driver = webdriver.Chrome(options=options)

print("Opening google.com")
driver.get("https://check.torproject.org/")
time.sleep(5)


h1_element = driver.find_element(By.XPATH, "/html/body/div[2]/h1")

print(h1_element.text)



h1_element = driver.find_element(By.XPATH, "/html/body/div[2]/h1")

print(h1_element.text)


driver.get("https://httpbin.org/ip")
time.sleep(3)

print("Current IP info:")
print(driver.page_source)


driver.quit()
print("Script Completed")
