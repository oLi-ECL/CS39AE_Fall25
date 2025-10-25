# pie_chart_plot.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set page title
st.title("🍰 Pie Chart Demo")

# Build the correct absolute path
current_dir = Path(__file__).resolve().parent
csv_path = current_dir.parent / "data" / "pie_demo.csv"

# Debug info (optional)
# st.write("CSV Path:", csv_path)

# Load the data
try:
    df = pd.read_csv(csv_path)
    st.write("### Data Preview", df)

    # Check that CSV has the expected columns
    if "Category" in df.columns and "Sales" in df.columns:
        # Create pie chart
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(df["Sales"], labels=df["Category"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")  # Equal aspect ratio = circle

        st.pyplot(fig)
    else:
        st.warning("⚠️ CSV must contain 'Category' and 'Sales' columns.")

except FileNotFoundError:
    st.error(f"❌ Could not find file at {csv_path}")
