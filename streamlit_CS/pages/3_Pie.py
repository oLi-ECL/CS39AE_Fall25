import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GitHub raw URL of the CSV
csv_url = "https://raw.githubusercontent.com/username/my_repo/main/streamlit_CS/data/pie_demo.csv"

# Read CSV directly from GitHub
df = pd.read_csv(csv_url)

st.write("### Sales Data")
st.dataframe(df, width='stretch')  # updated from deprecated use_container_width

# Plot a pie chart
fig, ax = plt.subplots()
ax.pie(df['Sales'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
ax.set_title("Sales Distribution by Category")
st.pyplot(fig)
