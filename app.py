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
    """
    Handle toggle switch changes and send POST request to the external server.
    """
    global switch_state
    # Get the new state from the request
    switch_state["switch_state"] = request.form.get("state", "off")

    # Prepare the payload
    payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}

    try:
        # Send POST request to the external server
        response = requests.post(POST_URL, json=payload)
        return jsonify({"status": "success", "response": response.text}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_state', methods=['GET'])
def get_state():
    """
    Return the current switch state as a JSON response.
    """
    return jsonify({"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]})


@app.route('/send_payload', methods=['GET'])
def send_payload():
    """
    Send a POST request with the current switch state when accessed via GET.
    """
    payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}

    try:
        # Send POST request to the external server
        response = requests.post(POST_URL, json=payload)
        return jsonify({"status": "success", "response": response.text}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/receive', methods=['POST'])
def receive_payload():
    """
    Test endpoint to mimic the external server's /api/receive endpoint.
    Logs received payload.
    """
    data = request.json
    print("Received payload:", data)  # Logs the received payload for debugging
    return jsonify({"status": "success", "message": "Payload received successfully."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
