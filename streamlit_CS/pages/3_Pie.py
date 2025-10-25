# pie_chart_plot.py

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find the absolute path to this script (3_Pie.py)
current_dir = Path(__file__).resolve().parent

# Build path to data/pie_demo.csv relative to the project structure
csv_path = current_dir.parent / 'data' / 'pie_demo.csv'

# Load the CSV
data = pd.read_csv(csv_path)

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(data['Value'], labels=data['Category'], autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart from CSV Data')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle
plt.show()
