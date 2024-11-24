from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial states of pins
pins_state = {
    "D4": False,
    "D5": False,
    "D6": False,
    "D7": False
}

@app.route('/pins', methods=['GET', 'PUT'])
def handle_pins():
    if request.method == 'GET':
        # Return the current state of all pins in JSON format
        return jsonify(pins_state)
    
    if request.method == 'PUT':
        data = request.json
        pin = data.get('pin')
        state = data.get('state')
        
        if pin in pins_state:
            pins_state[pin] = state
            return jsonify({pin: state}), 200
        else:
            return jsonify({"error": "Invalid pin"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
