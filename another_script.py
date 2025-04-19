from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = "/usr/bin/chromium-browser"  # Ensure correct location
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set proxy to Tor SOCKS5
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')

# Create the WebDriver instance
driver = webdriver.Chrome(options=options)

print("Opening google.com")
driver.get("https://check.torproject.org/")

time.sleep(5)

# Check if we're using Tor
h1_element = driver.find_element(By.XPATH, "/html/body/div[2]/h1")
print(h1_element.text)  # Should say "Congratulations. This browser is configured to use Tor."

# Get IP info from httpbin to confirm Tor IP
driver.get("https://httpbin.org/ip")
time.sleep(3)

print("Current IP info:")
print(driver.page_source)

driver.quit()
