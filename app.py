from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, template_folder='/var/www/html/iotswitch/templates')

# Server Configuration
SERVER_IP = "http://167.71.237.12"
SERVER_PORT = "80"
POST_URL = f"{SERVER_IP}:{SERVER_PORT}/api/receive"

# State storage (initial state of the switch)
switch_state = {"switch_id": "1", "switch_state": "0"}

@app.route('/')
def index():
    """Serve the HTML page with the current toggle state."""
    return render_template('index.html', switch_state=switch_state["switch_state"])
        

@app.route('/get_state', methods=['GET'])
def get_state():
    return jsonify({"1": switch_state["switch_state"]})

if __name__ == '__main__':
    # Start the Flask app on port 4000
    app.run(host='0.0.0.0', port=4000, debug=True)
