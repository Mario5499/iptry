import subprocess
import time
import socket

# Start Tor
print("Starting Tor service...")
subprocess.run(["service", "tor", "start"])

# Wait until Tor's SOCKS5 proxy is actually ready
def wait_for_tor(host="127.0.0.1", port=9050, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=5):
                print("✅ Tor SOCKS5 proxy is ready.")
                return True
        except:
            print("⏳ Waiting for Tor...")
            time.sleep(2)
    raise TimeoutError("❌ Timed out waiting for Tor to be ready.")

# Wait for Tor to be ready before continuing
wait_for_tor()

print("✅ Tor is ready. Running another_script.py...\n")
subprocess.run(["python3", "another_script.py"])
