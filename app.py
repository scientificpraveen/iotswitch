from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
app = Flask(__name__, template_folder='/var/www/html/iotswitch/templates')

# Server Configuration
SERVER_IP = "http://167.71.237.12"
SERVER_PORT = "80"
POST_URL = f"{SERVER_IP}:{SERVER_PORT}/api/receive"

# State storage
switch_state = {"switch_id": "1", "switch_state": "off"}

@app.route('/')
def index():
    """Serve the HTML page with the current toggle state."""
    return render_template('index.html', switch_state=switch_state["switch_state"])

@app.route('/toggle', methods=['POST'])
def toggle_switch():
    """Handle switch toggling and send the updated state."""
    global switch_state
    switch_state["switch_state"] = request.form.get("state", "off")
    payload = {"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]}

    try:
        response = requests.post(POST_URL, json=payload)
        return jsonify({"status": "success", "response": response.text}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_state', methods=['GET'])
def get_state():
    """Return the current switch state."""
    return jsonify({"switch_id": switch_state["switch_id"], "switch_state": switch_state["switch_state"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

