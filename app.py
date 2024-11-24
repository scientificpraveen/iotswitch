from flask import Flask, jsonify
import requests

app = Flask(__name__)

# NodeMCU API endpoint (this will send a request back to NodeMCU to toggle a pin)
Nodemcu_url = "http://<nodemcu-ip>/toggle"  # Replace <nodemcu-ip> with the actual IP of the NodeMCU

@app.route('/api/togglePin', methods=['GET'])
def toggle_pin():
    try:
        # Send request to NodeMCU to toggle pin (replace with real NodeMCU IP)
        response = requests.get(Nodemcu_url)
        
        if response.status_code == 200:
            return jsonify({
                "message": "Pin state toggled successfully",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": "Failed to toggle pin on NodeMCU",
                "status": "error"
            }), 500
    except Exception as e:
        return jsonify({
            "message": f"Error: {str(e)}",
            "status": "error"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Run Flask on port 80
