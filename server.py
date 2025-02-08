from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

latest_data = {
    "heartRate": 0,
    "spo2": 0,
    "emotion": "No data",
    "avgHeartRate": 0,
    "avgSpo2": 0,
    "timestamp": "No data"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update_data():
    global latest_data
    data = request.json
    
    latest_data = {
        "heartRate": data.get('heartRate', 0),
        "spo2": data.get('spo2', 0),
        "emotion": data.get('emotion', 'Unknown'),
        "avgHeartRate": data.get('avgHeartRate', 0),
        "avgSpo2": data.get('avgSpo2', 0),
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    
    return jsonify({"status": "success"})

@app.route('/get_data')
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)