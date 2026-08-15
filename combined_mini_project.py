import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 17000, 20000, 22000],
    "Profit": [3000, 4000, 5000, 4500, 6000, 6500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Data Visualization Tool")
print(df)

# Line Chart for Sales
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar Chart for Profit
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit Analysis")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# Pie Chart for Sales Distribution
plt.pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()