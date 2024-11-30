from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Server Configuration
SERVER_IP = "http://167.71.237.12"
SERVER_PORT = "80"
POST_URL = f"{SERVER_IP}:{SERVER_PORT}/api/receive"

# State storage
switch_state = {"switch_id": "1", "switch_state": "off"}

@app.route('/toggle', methods=['POST'])
def toggle_switch():
    """Handle switch toggling and send the updated state."""
    global switch_state

    # Attempt to read JSON data from the request
    try:
        data = request.get_json()

        if data is None:
            return jsonify({"status": "error", "message": "Invalid JSON"}), 400

        # Get the new state from the JSON payload
        switch_state["switch_state"] = data.get("state", "off")
        payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}

        # Send updated state to another server
        response = requests.post(POST_URL, json=payload)

        return jsonify({
            "status": "success", 
            "switch_state": 1 if switch_state["switch_state"] == "on" else 0,
            "response": response.text
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_state', methods=['GET'])
def get_state():
    """Return the current switch state as 1 for on, 0 for off."""
    return jsonify({
        switch_state["switch_id"] : 1 if switch_state["switch_state"] == "on" else 0
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
