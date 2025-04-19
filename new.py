import subprocess
import time
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException

# Start Tor service
print("Starting Tor service...")
subprocess.run(["service", "tor", "start"])

# Wait until Tor's SOCKS5 proxy is ready
start_time = time.time()
while time.time() - start_time < 60:
    try:
        with socket.create_connection(("127.0.0.1", 9050), timeout=5):
            print("✅ Tor SOCKS5 proxy is ready.")
            break
    except:
        print("⏳ Waiting for Tor...")
        time.sleep(2)
else:
    raise TimeoutError("❌ Timed out waiting for Tor to be ready.")

# Add a short delay to ensure Tor connection is fully established
print("Waiting for Tor to fully establish connection...")
time.sleep(5)  # Adding a 5-second delay

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

# Retry mechanism with longer timeout
retry_count = 3
for attempt in range(retry_count):
    try:
        print(f"\nAttempt {attempt + 1}: Opening https://httpbin.org/ip ...")
        driver.get("https://httpbin.org/ip")
        
        # Increase the timeout duration to 60 seconds
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "pre"))
        )
        
        ip_info = driver.find_element(By.TAG_NAME, "pre").text
        print("Current IP info:")
        print(ip_info)
        
        # Visit check.torproject.org to verify if using Tor
        print("\nChecking Tor status on first attempt...")
        driver.get("https://check.torproject.org/")
        
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        
        tor_status_first = driver.find_element(By.TAG_NAME, "h1").text
        print("Tor status on first attempt:")
        print(tor_status_first)

        # Check again to ensure Tor is still working
        print("\nChecking Tor status again to ensure Tor is running...")
        driver.get("https://check.torproject.org/")
        
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        
        tor_status_second = driver.find_element(By.TAG_NAME, "h1").text
        print("Tor status on second attempt:")
        print(tor_status_second)

        break  # Exit loop if successful
    except TimeoutException:
        print(f"Timeout occurred during attempt {attempt + 1}. Retrying...")
        time.sleep(5)  # Add a short delay before retry
    except WebDriverException as e:
        print(f"WebDriver error during attempt {attempt + 1}: {e}")
        break

# Quit the driver after completing the task
driver.quit()
print("Script Completed")
