import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Student": ["Arun", "Priya", "Kaviya", "Rahul", "Sneha"],
    "Maths": [85, 92, 78, 88, 95],
    "Science": [90, 85, 80, 84, 91],
    "English": [75, 89, 85, 90, 87]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average marks
df["Average"] = (df["Maths"] + df["Science"] + df["English"]) / 3

print("Student Performance Data")
print(df)

# Bar Chart
plt.bar(df["Student"], df["Average"])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.show()