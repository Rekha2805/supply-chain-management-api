import random
import time
import statistics

# Simulated AI accuracy data
ai_predictions = [random.uniform(0.85, 0.95) for _ in range(100)]
ai_accuracy = statistics.mean(ai_predictions)

# Simulated chatbot response times (in seconds)
chatbot_response_times = [random.uniform(0.9, 2.0) for _ in range(100)]
avg_response_time = statistics.mean(chatbot_response_times)

# Simulated IoT data reception rate (percentage of data received on time)
iot_data_points = [random.choice([True] * 98 + [False] * 2) for _ in range(1000)]
iot_reliability = (sum(iot_data_points) / len(iot_data_points)) * 100

# Simulated API response times
api_times = [random.uniform(100, 300) for _ in range(50)]  # in milliseconds
avg_api_time = statistics.mean(api_times)

# Report
def performance_report():
    print("\n--- Supply Chain Management Performance Report ---")
    print(f"AI Prediction Accuracy: {ai_accuracy*100:.2f}%")
    print(f"Avg Chatbot Response Time: {avg_response_time:.2f} seconds")
    print(f"IoT Data Reliability: {iot_reliability:.2f}%")
    print(f"Avg API Response Time: {avg_api_time:.2f} ms")
    print("---------------------------------------------------")

performance_report()