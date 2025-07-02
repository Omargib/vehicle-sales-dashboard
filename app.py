"""App Streamlit for Vehicle Analysis."""
# Import libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Load dataset#


@st.cache_data
def load_data():
    """Define function to load dataset"""
    raw_df = pd.read_csv("vehicles_us.csv")
    raw_df.columns = raw_df.columns.str.lower().str.strip()

    # Convert data types
    raw_df[['model_year', 'cylinders']] = raw_df[['model_year', 'cylinders']].apply(
        lambda col: pd.to_numeric(col, errors='coerce').astype('Int64')
    )
    raw_df['date_posted'] = pd.to_datetime(
        raw_df['date_posted'], errors='coerce')

    return raw_df.dropna()


df = load_data()

# Create Web App

# Assign Header

st.header("Vehicle Sales Explorer")

show_hist = st.checkbox("Show Price Histogram")
show_scatter = st.checkbox("Show Price vs Odometer Scatter Plot")

if show_hist:
    fig = px.histogram(df, x='price', nbins=50,
                       title='Distribution of Vehicle Prices')
    st.plotly_chart(fig)

if show_scatter:
    fig = px.scatter(df, x='odometer', y='price', color='tytpe',
                     title='Price vs Odometer by Vehicle Type',
                     hover_data=['model', 'model_year'])
    st.plotly_chart(fig)
