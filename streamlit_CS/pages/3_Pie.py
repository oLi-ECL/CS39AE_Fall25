import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Page setup
st.title("🥧 Interactive Pie Chart Demo")

# Locate CSV file safely
current_dir = Path(__file__).resolve().parent
csv_path = current_dir.parent / "data" / "pie_demo.csv"

# Load CSV data
try:
    df = pd.read_csv(csv_path)
    st.write("### Data Preview", df)

    # Check for expected columns
    if "Category" in df.columns and "Value" in df.columns:
        # Create interactive pie chart
        fig = px.pie(
            df,
            names="Category",
            values="Value",
            title="Interactive Pie Chart",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.3,  # Change to 0 for solid pie chart
        )

        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ CSV must contain 'Category' and 'Value' columns.")

except FileNotFoundError:
    st.error(f"❌ Could not find file at {csv_path}")
