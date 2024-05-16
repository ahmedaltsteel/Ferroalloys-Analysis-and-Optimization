import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

steel_grades = ["ASTMA992M", "G300", "092"]
years = [2022, 2023, 2024]
rolling_mills = ["RM1", "RM2", "RM3"]
materials = ["Carbon", "Silicon", "Nickel", "Chromium", "Vanadium"]
cost_data = {
    "Material": materials,
    "Cost (AED)": [486381.73, 114066.58, 500382.66, 43907.69, 2086540.05]
}
cost_df = pd.DataFrame(cost_data)

st.title("Ferroalloys Consumption Analysis Dashboard")

st.sidebar.header("Filters")
selected_rm = st.sidebar.selectbox("Choose Rolling Mill", rolling_mills)
selected_grade = st.sidebar.selectbox("Choose Steel Grade", steel_grades)
selected_year = st.sidebar.selectbox("Choose a Year", years)

st.subheader(f"Consumption for {selected_rm}, {selected_grade} in {selected_year}")
gauges = st.columns(len(materials))

for i, material in enumerate(materials):
    value = np.random.uniform(0, 1)
    gauges[i].gauge(label=material, value=value)

st.subheader("Analysis for Vanadium")
vanadium_data = {
    "Grade": steel_grades,
    "Actual Value": np.random.uniform(0, 0.15, len(steel_grades)),
    "High Limit": np.random.uniform(0.1, 0.15, len(steel_grades)),
    "Low Limit": np.random.uniform(0, 0.05, len(steel_grades))
}
vanadium_df = pd.DataFrame(vanadium_data)
fig = px.scatter(vanadium_df, x="Grade", y="Actual Value",
                 error_y="High Limit", error_y_minus="Low Limit")
st.plotly_chart(fig)

st.subheader("Cost of Overshot in AED")
fig, ax = plt.subplots()
cost_df.plot(kind="bar", x="Material", y="Cost (AED)", ax=ax)
st.pyplot(fig)
