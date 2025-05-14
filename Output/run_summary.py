import requests

BASE_URL = 'http://127.0.0.1:5000'

# 1. Predicted Demand
forecast_input = {"sales_data": [40, 50, 32]}  # This should return 122
forecast_resp = requests.post(f"{BASE_URL}/api/forecast", json=forecast_input)
predicted_demand = forecast_resp.json().get("predicted_demand", "N/A")

# 2. Chatbot Response
chat_input = {"message": "Where is my shipment?"}
chat_resp = requests.post(f"{BASE_URL}/api/chatbot", json=chat_input)
chatbot_response = chat_resp.json().get("response", "N/A")

# 3. Simulated Sensor Data
sensor_resp = requests.get(f"{BASE_URL}/api/iot")
sensor_data = sensor_resp.json()

# 4. Encryption
sample_text = "Sensitive Inventory Data"
encrypt_resp = requests.post(f"{BASE_URL}/api/encrypt", json={"data": sample_text})
encrypted_data = encrypt_resp.json().get("encrypted", "N/A")

# 5. Decryption
decrypt_resp = requests.post(f"{BASE_URL}/api/decrypt", json={"data": encrypted_data})
decrypted_data = decrypt_resp.json().get("decrypted", "N/A")

# Final formatted output
print("\n================ Supply Chain Management Output ================\n")
print(f"Predicted Demand:\n\n{predicted_demand}\n")
print(f"Chatbot Response: {chatbot_response}\n")
print("Simulated Sensor Data:", sensor_data, "\n")
print(f"Encrypted Data: {encrypted_data[:30]}...")  # Truncate for readability
print(f"\nDecrypted Data:\n\n{decrypted_data}")
print("\n================================================================")
