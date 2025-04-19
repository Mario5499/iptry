from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

MAX_RETRIES = 10
DELAY_BETWEEN_TRIES = 3  # seconds

h1_element = None
for attempt in range(MAX_RETRIES):
    try:
        print(f"🔄 Try {attempt + 1} to find the h1 element...")
        h1_element = driver.find_element(By.TAG_NAME, "h1")
        print("✅ Found element!")
        print(h1_element.text)
        break
    except NoSuchElementException:
        print(f"❌ h1 not found. Waiting {DELAY_BETWEEN_TRIES}s before retrying...")
        time.sleep(DELAY_BETWEEN_TRIES)

if h1_element is None:
    print("⚠️ Gave up after multiple tries. h1 element not found.")

# Get IP info from httpbin to confirm Tor IP
driver.get("https://httpbin.org/ip")
time.sleep(3)

print("Current IP info:")
print(driver.page_source)

driver.quit()
