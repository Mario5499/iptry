import subprocess
import time
import os
import signal

# Start tor (no shell=True)
subprocess.Popen(["service", "tor", "start"])

# Start dummy process to keep container alive
pid = subprocess.Popen(["tail", "-f", "/dev/null"]).pid

print("wait for 20 seconds")
time.sleep(20)

# Stop the dummy process (not tor)
os.kill(pid, signal.SIGINT)
print("end wait")

time.sleep(5)
print("RUNNING ANOTHER SCRIPT")
# Run your actual script (which should use the Tor proxy in browser options)
subprocess.run(["python3", "another_script.py"])
