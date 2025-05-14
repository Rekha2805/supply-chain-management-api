import random, time, hashlib
from sklearn.linear_model import LinearRegression
import numpy as np

# 📈 Forecast Demand
def forecast():
    sales = np.array([100, 110, 105, 120, 130, 125, 135, 140, 138, 145])
    days = np.arange(len(sales)).reshape(-1, 1)
    model = LinearRegression().fit(days, sales)
    pred = model.predict([[len(sales)]])[0]
    print(f"\n📊 Forecasted Demand: {pred:.2f} units")
    return f"Forecasted Demand: {pred:.2f}"

# 💬 Chatbot Order Tracking
def track_order():
    orders = {"ORD123": "Shipped", "ORD124": "In Transit", "ORD125": "Delivered"}
    oid = input("\n📦 Enter Order ID: ").strip().upper()
    status = orders.get(oid, "Not found")
    print(f"Order Status: {status}")
    return f"{oid}: {status}"

# 🌡️ IoT Simulation
def simulate_iot():
    temp = round(random.uniform(2, 8), 2)
    loc = random.choice(["Chennai", "Bangalore", "Mumbai"])
    print(f"\n🌐 IoT: Temp={temp}°C | Location={loc}")
    return f"IoT: {temp}°C @ {loc}"

# 🔐 Blockchain Logging
class Block:
    def __init__(self, idx, data, prev):
        self.i, self.t, self.d, self.p = idx, time.time(), data, prev
        self.h = self.hash()

    def hash(self):
        return hashlib.sha256(f"{self.i}{self.t}{self.d}{self.p}".encode()).hexdigest()

class Chain:
    def __init__(self):
        self.chain = [Block(0, "Genesis", "0")]

    def add(self, data):
        b = Block(len(self.chain), data, self.chain[-1].h)
        self.chain.append(b)
        print(f"🔒 Block Added: {b.h[:10]}...")

# 🔧 Main App
def main():
    print("📦 Smart SCM Assistant")
    c = Chain()
    c.add(forecast())
    c.add(track_order())
    c.add(simulate_iot())
    print("\n📄 Blockchain Ledger:")
    for b in c.chain:
        print(f"{b.i}: {b.d} | {b.h[:10]}...")

if __name__ == "__main__":
    main()
