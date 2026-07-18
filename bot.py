import time

print("🤖 ربات املاک مصطفی روشن شد...")

while True:
    print("ربات در حال اجرا است...")
    time.sleep(60)
from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Amlak Mostafa Bot is running!"

def run_bot():
    while True:
        print("ربات در حال اجرا است...")
        time.sleep(60)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
