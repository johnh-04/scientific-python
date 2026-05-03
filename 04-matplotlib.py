# Matplolib is a powerful library for creating static, animated, and interactive visualizations in Python. It provides a wide range of plotting functions and customization options to create various types of plots, such as line plots, scatter plots, bar charts, histograms, and more.

# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Simple chart
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Data')  # Create a line plot
plt.xlabel("X-axis")  # Set label for X-axis
plt.ylabel("Y-axis")  # Set label for Y-axis
plt.title("Line Plot")  # Set title for the plot
plt.legend()  # Display legend
plt.grid(True)  # Show grid
plt.show()  # Display the plot

# Bar chart
x = ['A', 'B', 'C', 'D']
y = [10, 25, 7, 30]

plt.bar(x, y, color='orange')  # Create a bar chart
plt.xlabel("Categories")  # Set label for X-axis
plt.ylabel("Values")  # Set label for Y-axis
plt.title("Bar Chart")  # Set title for the plot
plt.show()  # Display the plot

# Histogram
data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution

plt.hist(data, bins=30, color='green', edgecolor='black')  # Create a histogram with 30 bins
plt.xlabel("Value")  # Set label for X-axis
plt.ylabel("Frequency")  # Set label for Y-axis
plt.title("Histogram")  # Set title for the plot
plt.show()  # Display the plot

# Scatter plot
x = np.random.rand(100)  # Generate 100 random numbers between 0 and 1 for X-axis
y = np.random.rand(100)  # Generate 100 random numbers between 0 and

plt.scatter(x, y, color='red', alpha=0.5)  # Create a scatter plot with red points and some transparency
plt.xlabel("X-axis")  # Set label for X-axis
plt.ylabel("Y-axis")  # Set label for Y-axis
plt.title("Scatter Plot")  # Set title for the plot
plt.show()  # Display the plot

# Pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen', 'lightyellow'], startangle=140)  # Create a pie chart with percentage labels
plt.title("Pie Chart")  # Set title for the plot
plt.show()  # Display the plot

# Adding different lines to the same plot
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced numbers between 0 and 10
y1 = np.sin(x)  # Calculate sine values
y2 = np.cos(x)  # Calculate cosine values

plt.plot(x, y1, label='Sine', color='blue', linestyle='--', linewidth=2)  # Plot sine values
plt.plot(x, y2, label='Cosine', color='orange', linestyle='-.', linewidth=2)  # Plot cosine values
plt.xlabel("X-axis")  # Set label for X-axis
plt.ylabel("Y-axis")  # Set label for Y-axis
plt.title("Sine and Cosine Waves")  # Set title for the plot
plt.legend()  # Display legend
plt.grid(True)  # Show grid
plt.show()  # Display the plot

# Subplots
x = np.linspace(0, 10, 5)  # Generate 5 evenly spaced numbers between 0 and 10
y1 = [10, 20, 30, 40, 50]  # Sample data for bar chart
y2 = [5, 10, 15, 20, 25]  # Sample data for bar chart

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Create a figure with 2 subplots (2 rows, 2 columns)

axs[0, 0].plot(x, y1, color='blue')  # First subplot: line plot
axs[0, 0].set_title("Line Plot")  # Set title for the first subplot

axs[0, 1].bar(x, y2, color='orange')  # Second subplot: bar chart
axs[0, 1].set_title("Bar Chart")  # Set title for the second subplot

axs[1, 0].hist(np.random.randn(1000), bins=30, color='green', edgecolor='black')  # Third subplot: histogram
axs[1, 0].set_title("Histogram")  # Set title for the third subplot

axs[1, 1].scatter(x[:5], np.random.rand(5), color='red', alpha=0.5)  # Fourth subplot: scatter plot
axs[1, 1].set_title("Scatter Plot")  # Set title for the fourth subplot

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the subplots

# Save chart as image
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, marker='o', linestyle='-', color='blue')  # Create a line plot
plt.xlabel("X-axis")  # Set label for X-axis
plt.ylabel("Y-axis")  # Set label for Y-axis
plt.title("Line Plot")  # Set title for the plot
plt.savefig("line_plot.png")  # Save the plot as a PNG image
plt.show()  # Display the plot

# Matplotlib and Pandas integration
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)  # Create a DataFrame from the data
print(df)  # Output: DataFrame with columns "Name", "Age", and "City"

df.plot(kind='bar', x='Name', y='Age', color='purple', title='Age of Individuals')  # Create a bar chart using DataFrame
plt.show()  # Display the plot