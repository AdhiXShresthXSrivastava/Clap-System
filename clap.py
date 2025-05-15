import sounddevice as sd
import numpy as np
import webbrowser
import time

# Parameters
clap_threshold = 100  # Adjust based on microphone sensitivity
clap_count = 0
last_clap_time = 0

def detect_clap(indata, frames, time_info, status):
    global clap_count, last_clap_time
    volume_norm = np.linalg.norm(indata) * 10

    if volume_norm > clap_threshold:
        current_time = time.time()  # Use system time to track clap intervals
        if current_time - last_clap_time < 1:  # Two quick claps
            clap_count += 1
        else:
            clap_count = 1  # Reset if too long between claps

        last_clap_time = current_time

        if clap_count == 2:
            webbrowser.open("https://www.google.com")
            clap_count = 0  # Reset

# Start listening
with sd.InputStream(callback=detect_clap):
    print("Listening for claps...")
    try:
        while True:
            time.sleep(0.1)  # Prevent excessive CPU usage
    except KeyboardInterrupt:
        print("Exiting...")
