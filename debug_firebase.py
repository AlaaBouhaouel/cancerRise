import urllib.request
import json
import time

URL = "https://atast2026-default-rtdb.europe-west1.firebasedatabase.app/.json"

prev = None

print("Watching Firebase Realtime DB... (Ctrl+C to stop)\n")

while True:
    try:
        with urllib.request.urlopen(URL) as res:
            data = json.loads(res.read())

        if data != prev:
            print("--- CHANGE DETECTED ---")
            print(json.dumps(data, indent=2))
            print()
            prev = data

    except Exception as e:
        print("Error:", e)

    time.sleep(1)
