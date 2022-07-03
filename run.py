import os
from flask import Flask, request, jsonify, send_file
import torch
from urllib.parse import urlparse

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "healthy"})

@app.route('/detect', methods=["POST"])
def detect():
    params = request.get_json()
    source = params["image"]
    img = model(source)
    a = urlparse(source)
    filename = os.path.basename(a.path)
    filename = filename.split('.')[0]
    img.save(save_dir='outputs')
    return send_file(f"outputs/{filename}.jpg", mimetype='image/jpeg')
    
    

if __name__ == "__main__":
    app.run('0.0.0.0', 8080, False)