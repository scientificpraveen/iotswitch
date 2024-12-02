from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, template_folder='/var/www/html/iotswitch/templates')

# Server Configuration
SERVER_IP = "http://167.71.237.12"
SERVER_PORT = "80"
POST_URL = f"{SERVER_IP}:{SERVER_PORT}/api/receive"

# Store switch state globally
switch_state = {"switch_id": "1", "switch_state": "off"}

@app.route('/')
def index():
    """Serve the HTML page with the current toggle state."""
    # Pass the current state to the HTML template
    return render_template('index.html', switch_state=switch_state["switch_state"])

@app.route('/api/receive', methods=['POST'])
def receive_data():
    """Mock endpoint to confirm data reception."""
    return jsonify({"status": "success", "message": "Data received"})

@app.route('/toggle', methods=['POST'])
def toggle_switch():
    """Handle switch toggling and send the updated state."""
    global switch_state
    data = request.json  # Expecting JSON payload
    
    if data and "state" in data:
        # Update the switch state
        switch_state["switch_state"] = data["state"]
        payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}

        try:
            # Send data to an external server (mocked here with POST_URL)
            response = requests.post(POST_URL, json=payload)
            return jsonify({
                "status": "success",
                "response": response.text,
                "switch_state": switch_state["switch_state"]
            }), response.status_code
        except requests.exceptions.RequestException as e:
            # Handle any errors in the POST request
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        # Invalid payload received
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

@app.route('/get_state', methods=['GET'])
def get_state():
    """Return the current switch state."""
    # Return 1 for "on" and 0 for "off"
    return jsonify({switch_state["switch_id"]: 1 if switch_state["switch_state"] == "on" else 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
