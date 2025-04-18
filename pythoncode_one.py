from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException
import subprocess
import time

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



driver.quit()
print("Script Completed")
