from flask import Flask, jsonify, render_template
from pathlib import Path
import csv
import time

app = Flask(__name__, static_folder="static", template_folder="templates")

CSV_FILE = Path(__file__).parent / "videos.csv"
_last_mtime = 0
_cache = []

def load_csv():
    global _last_mtime, _cache
    try:
        mtime = CSV_FILE.stat().st_mtime
    except FileNotFoundError:
        return []
    
    # file güncellemesi
    if mtime != _last_mtime:
        items = []
        with CSV_FILE.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = (row.get("url") or "").strip()
                title = (row.get("title") or "").strip()
                if url:
                    items.append({"url": url, "title": title})
        _cache = items
        _last_mtime = mtime
    return _cache

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/videos")
def api_videos():
    return jsonify(load_csv())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
