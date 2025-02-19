from flask import Flask, jsonify, request

app = Flask(__name__)

# Main endpoint for Delivery Reports (DLR)
@app.route('/dlr', methods=['POST'])
def dlr():
    data = request.json  # Assumes data is sent as JSON
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Process the DLR (add your business logic here)
    print(f"Received DLR: {data}")

    # Success response
    return jsonify({"status": "DLR received", "data": data}), 200

# Health check endpoint for livenessProbe
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

# Readiness check endpoint for readinessProbe
@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({"status": "ready"}), 200

# Default route to check if the app is running
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Jasmin DLR Flask App is running!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
