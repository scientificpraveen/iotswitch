from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Server Configuration
SERVER_IP = "http://167.71.237.12"
SERVER_PORT = "80"
POST_URL = f"{SERVER_IP}:{SERVER_PORT}/api/receive"

# State storage
switch_state = {"switch_id": "1", "switch_state": "off"}

@app.route('/')
def index():
    """Serve HTML page with toggle switch."""
    return render_template('index.html', switch_state=switch_state["switch_state"])

@app.route('/toggle', methods=['POST'])
def toggle_switch():
    """Handle toggle change and send POST request."""
    global switch_state
    switch_state["switch_state"] = request.form.get("state", "off")

    # Send POST request
    payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}
    try:
        response = requests.post(POST_URL, json=payload)
        return jsonify({"status": "success", "response": response.text}), response.status_code
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/send_payload', methods=['GET'])
def send_payload():
    """Send POST payload when requested using GET method."""
    payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}
    try:
        response = requests.post(POST_URL, json=payload)
        return jsonify({"status": "success", "response": response.text}), response.status_code
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)  # Flask runs on port 4000
