from flask import Flask, request, jsonify
from ai_models.demand_forecast import predict_demand
from chatbot.chatbot_service import get_chatbot_response
from iot.sensor_simulator import get_simulated_sensor_data
from security.encryption_utils import encrypt_data, decrypt_data

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Supply Chain Management System is running."})

@app.route('/api/forecast', methods=['POST'])
def forecast():
    try:
        data = request.get_json()
        sales_data = data.get('sales_data', [])
        if not sales_data:
            return jsonify({"error": "Missing or invalid sales_data"}), 400
        result = predict_demand(sales_data)
        return jsonify({"predicted_demand": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify({"error": "Message is required"}), 400
        response = get_chatbot_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/iot', methods=['GET'])
def iot_data():
    try:
        data = get_simulated_sensor_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    try:
        content = request.json.get('data', '')
        if not content:
            return jsonify({"error": "Data is required"}), 400
        encrypted = encrypt_data(content)
        return jsonify({"encrypted": encrypted})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    try:
        encrypted = request.json.get('data', '')
        if not encrypted:
            return jsonify({"error": "Data is required"}), 400
        decrypted = decrypt_data(encrypted)
        return jsonify({"decrypted": decrypted})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
