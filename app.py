from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

# Store the latest data received from ESP8266
latest_data = {
    'heartRate': 0,
    'spo2': 0,
    'emotion': 'UNKNOWN',
    'avgHeartRate1Hr': 0
}

@app.route('/')
def index():
    # Render the main page and pass the latest data to the template
    return render_template('index.html', data=latest_data)

@app.route('/update', methods=['POST'])
def update():
    # Receive data from ESP8266
    if request.is_json:
        data = request.get_json()
        latest_data['heartRate'] = data.get('heartRate', 0)
        latest_data['spo2'] = data.get('spo2', 0)
        latest_data['emotion'] = data.get('emotion', 'UNKNOWN')
        latest_data['avgHeartRate1Hr'] = data.get('avg1hr', 0)
        return 'Data received successfully!', 200
    else:
        return 'Invalid data format', 400

@app.route('/live_data', methods=['GET'])
def live_data():
    # Return the latest data as JSON
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
