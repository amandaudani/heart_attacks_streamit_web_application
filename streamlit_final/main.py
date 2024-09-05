import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

# App Title
st.title("Heart Health Explorer")

# Introduction Section
st.header("Understanding Heart Attacks: A Vital Insight")
st.write("""
Heart attacks, a leading cause of mortality globally, occur when the blood flow to the heart is obstructed. This blockage is typically caused by the accumulation of fat, cholesterol, and other substances, forming a plaque in the coronary arteries. When this plaque ruptures, it can lead to a life-threatening clot. Early detection and awareness of the risk factors are key to prevention.

In this web app, we delve into heart attack data, exploring various risk factors, correlations, and statistical insights that can help in understanding and preventing this deadly condition.
""")

# Displaying an Image Related to Heart Health
st.image("D:/streamlit_final/h1.jpg", width=550, caption="Anatomy of a Heart Attack")

# Dataset Section
st.title("Heart Attack Dataset Overview")
data = pd.read_csv("heart_attack_dataset.csv")
st.write("Dataset Dimensions:", data.shape)

# Sidebar Menu for Navigation
menu = st.sidebar.radio("Navigation", ["Home", "Visualizations"])

if menu == "Home":
    st.image("D:/streamlit_final/h2.jpg", width=550, caption="Heart Health Awareness")

    st.header("Explore the Dataset")
    if st.checkbox("Show Data Sample"):
        st.table(data.head(150))
    
    st.header("Statistical Summary")
    if st.checkbox("Display Statistical Summary"):
        st.table(data.describe())
    
    st.header("Correlation Matrix")
    if st.checkbox("View Correlation Heatmap"):
        # Display heatmap for numeric columns only
        numeric_data = data.select_dtypes(include=[np.number])
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

elif menu == "Visualizations":
    st.title("Data Visualizations")
    graph_type = st.selectbox("Choose a Graph Type", ["Scatter Plot", "Bar Graph", "Histogram"])

    if graph_type == "Scatter Plot":
        if "Blood Pressure (mmHg)" in data.columns and "outpu" in data.columns:
            value = st.slider("Filter Data by Age", 0, int(data["age"].max()), 0)
            filtered_data = data[data["age"] > value]
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.scatterplot(data=filtered_data, x="age", y="Gender", ax=ax)
            st.pyplot(fig)
        else:
            st.write("Required columns are not present in the dataset.")
    
    elif graph_type == "Bar Graph":
        if "Gender" in data.columns:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x="Gender", y=data.index, data=data, ax=ax)
            st.pyplot(fig)
        else:
            st.write("The required column 'Gender' is missing from the dataset.")
    
    elif graph_type == "Histogram":
        if "Cholesterol (mg/dL)" in data.columns:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(data["Cholesterol (mg/dL)"], kde=True, ax=ax)
            st.pyplot(fig)
        else:
            st.write("The required column 'Cholesterol (mg/dL)' is missing from the dataset.")
