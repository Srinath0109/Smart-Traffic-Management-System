from flask import Flask, jsonify
import threading
from services.video_processing import process_traffic

app = Flask(__name__)

@app.route("/start", methods=["POST"])
def start_traffic_analysis():
    """Start traffic video processing in a separate thread"""
    thread = threading.Thread(target=process_traffic)
    thread.start()
    return jsonify({"status": "Traffic analysis started!"})

if __name__ == "__main__":
    app.run(debug=True)
