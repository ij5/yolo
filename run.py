from flask import Flask, request, jsonify, send_file
import torch


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "healthy"})

@app.route('/detect', methods=["POST"])
def detect():
    source = request.files["image"]
    img = model(source)
    return send_file(img, mimetype='image/jpeg')
    
    

if __name__ == "__main__":
    app.run('0.0.0.0', 8080, False)