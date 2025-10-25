# pie_chart_plot.py

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv('../data/pie_demo.csv')

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart from CSV Data')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle
plt.show()
