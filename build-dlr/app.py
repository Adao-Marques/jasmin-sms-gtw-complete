from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint principal para Delivery Reports (DLR)
@app.route('/dlr', methods=['POST'])
def dlr():
    data = request.json  # Assume que os dados são enviados como JSON
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Processa o DLR (aqui você pode adicionar sua lógica de negócios)
    print(f"Received DLR: {data}")

    # Resposta de sucesso
    return jsonify({"status": "DLR received", "data": data}), 200

# Endpoint de health check para livenessProbe
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

# Endpoint de readiness check para readinessProbe
@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({"status": "ready"}), 200

# Rota padrão para verificar se o app está rodando
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Jasmin DLR Flask App is running!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
