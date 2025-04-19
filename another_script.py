from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException
import subprocess
import time

print("Script started")

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1345x610")
options.add_argument("--proxy-server=socks5://127.0.0.1:9050")



driver = webdriver.Chrome(options=options)

print("Opening google.com")
driver.get("https://check.torproject.org/")

time.sleep(20)
h1_element = driver.find_element(By.XPATH, "/html/body/div[2]/h1")

print(h1_element.text)


driver.get("https://httpbin.org/ip")
time.sleep(10)

print("Current IP info:")
print(driver.page_source)


driver.quit()
print("Script Completed")
