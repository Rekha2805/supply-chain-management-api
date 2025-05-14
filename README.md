

# Supply Chain Management System (SCM) API

This is a **Supply Chain Management System (SCM)** built with **Flask**, designed to handle various functionalities including demand forecasting, chatbot interaction, IoT data simulation, and data encryption & decryption. This API provides the backend services for a smart and secure SCM system.

## Features

* **📊 Demand Forecasting**: Predicts future demand based on historical sales data.
* **💬 Chatbot Integration**: Allows users to interact with a chatbot for order tracking and support.
* **🌐 IoT Data Simulation**: Simulates sensor data like temperature and location for monitoring shipments.
* **🔐 Data Encryption & Decryption**: Provides secure data encryption and decryption for sensitive information.

## Requirements

* Python 3.x
* Flask
* NumPy
* scikit-learn
* Required Python modules: `flask`, `numpy`, `scikit-learn`, `random`, `hashlib`

To install the required modules, run:

```bash
pip install -r requirements.txt
```

## Endpoints

### 1. **Home Route**

* **URL**: `/`
* **Method**: `GET`
* **Description**: Displays a message indicating that the SCM system is running.
* **Response**:

  ```json
  {
      "message": "Supply Chain Management System is running."
  }
  ```

### 2. **Forecast Demand**

* **URL**: `/api/forecast`
* **Method**: `POST`
* **Description**: Accepts sales data and returns the predicted demand based on linear regression.
* **Request Payload**:

  ```json
  {
      "sales_data": [100, 110, 105, 120, 130, 125]
  }
  ```
* **Response**:

  ```json
  {
      "predicted_demand": 150.32
  }
  ```

### 3. **Chatbot Order Tracking**

* **URL**: `/api/chatbot`
* **Method**: `POST`
* **Description**: Accepts a user message and returns a response from the chatbot (e.g., order status).
* **Request Payload**:

  ```json
  {
      "message": "Track my order"
  }
  ```
* **Response**:

  ```json
  {
      "response": "Your order is shipped."
  }
  ```

### 4. **Simulated IoT Data**

* **URL**: `/api/iot`
* **Method**: `GET`
* **Description**: Returns simulated IoT sensor data (e.g., temperature, location).
* **Response**:

  ```json
  {
      "temperature": 7.4,
      "location": "Bangalore"
  }
  ```

### 5. **Encrypt Data**

* **URL**: `/api/encrypt`
* **Method**: `POST`
* **Description**: Accepts data and returns the encrypted version.
* **Request Payload**:

  ```json
  {
      "data": "Sensitive Data"
  }
  ```
* **Response**:

  ```json
  {
      "encrypted": "a3c9...d5b9"
  }
  ```

### 6. **Decrypt Data**

* **URL**: `/api/decrypt`
* **Method**: `POST`
* **Description**: Accepts encrypted data and returns the decrypted content.
* **Request Payload**:

  ```json
  {
      "data": "a3c9...d5b9"
  }
  ```
* **Response**:

  ```json
  {
      "decrypted": "Sensitive Data"
  }
  ```

## Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/scm-api.git
   cd scm-api
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. The server will start, and the API will be accessible at:

   ```
   http://127.0.0.1:5000/
   ```

## Folder Structure

```plaintext
/SCM_API
│
├── app.py                  # Main Flask application
├── ai_models/
│   └── demand_forecast.py  # Forecast demand logic
├── chatbot/
│   └── chatbot_service.py  # Chatbot response logic
├── iot/
│   └── sensor_simulator.py # IoT data simulation
├── security/
│   └── encryption_utils.py # Encryption/decryption logic
└── requirements.txt         # List of dependencies
```

## Contributing

Feel free to fork the repository, create a feature branch, and submit a pull request. Please follow the code style guidelines and ensure that tests are written for new features.

