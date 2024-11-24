from flask import Flask, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO (Use GPIO 17 on Raspberry Pi or similar for NodeMCU)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # You can change this to match your GPIO pin

@app.route('/api/togglePin', methods=['GET'])
def toggle_pin():
    # Read current pin state
    pin_state = GPIO.input(17)
    
    # Toggle the pin state (HIGH -> LOW, LOW -> HIGH)
    GPIO.output(17, not pin_state)
    
    # Return the new state of the pin as JSON response
    return jsonify({
        "message": "Pin state toggled successfully",
        "new_pin_state": "HIGH" if GPIO.input(17) else "LOW"
    }), 200

@app.route('/api/getPinState', methods=['GET'])
def get_pin_state():
    # Return the current state of the pin
    pin_state = GPIO.input(17)
    return jsonify({
        "pin_state": "HIGH" if pin_state else "LOW"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Make it accessible on port 80
