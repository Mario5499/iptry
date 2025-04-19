from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import time

print("Script started")

# Set up Chrome options for headless + Tor SOCKS5 proxy
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1345x610")
options.add_argument("--proxy-server=socks5://127.0.0.1:9050")

# Launch browser
driver = webdriver.Chrome(options=options)

try:
    # Visit httpbin to check IP address
    print("Opening https://httpbin.org/ip ...")
    driver.get("https://httpbin.org/ip")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "pre"))
    )
    
    ip_info = driver.find_element(By.TAG_NAME, "pre").text
    print("Current IP info:")
    print(ip_info)

    # Visit check.torproject.org to verify if using Tor
    print("\nChecking Tor status on first attempt...")
    driver.get("https://check.torproject.org/")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    
    tor_status_first = driver.find_element(By.TAG_NAME, "h1").text
    print("Tor status on first attempt:")
    print(tor_status_first)

    # Check again to ensure Tor is still working
    print("\nChecking Tor status again to ensure Tor is running...")
    driver.get("https://check.torproject.org/")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    
    tor_status_second = driver.find_element(By.TAG_NAME, "h1").text
    print("Tor status on second attempt:")
    print(tor_status_second)

except TimeoutException:
    print("Timeout occurred while waiting for a page element.")
except WebDriverException as e:
    print(f"WebDriver error: {e}")
finally:
    driver.quit()
    print("Script Completed")
