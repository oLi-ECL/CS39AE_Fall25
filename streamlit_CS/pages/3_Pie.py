import csv
import matplotlib.pyplot as plt

# Read data from pie_demo.csv
categories = []
sales = []

with open('pie_demo.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        categories.append(row['Category'])
        sales.append(float(row['Sales']))

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Category')
plt.tight_layout()
plt.show()
