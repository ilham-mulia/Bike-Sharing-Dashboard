import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load dataset
all_df = pd.read_csv("all_data.csv")
all_df["dteday"] = pd.to_datetime(all_df["dteday"], errors='coerce')  # Handle errors

# Helper functions
def create_rentals_per_season_df(df):
    return df.groupby('season')['cnt'].sum().reset_index()

def create_rentals_per_workingday_df(df):
    return df.groupby('workingday')['cnt'].sum().reset_index()

def create_rentals_per_weather_df(df):
    return df.groupby('weathersit')['cnt'].sum().reset_index()

def create_rentals_per_weekday_df(df):
    return df.groupby('weekday')['cnt'].sum().reset_index()

# Sidebar filters
with st.sidebar:
    st.image("logo.png")

    if not all_df.empty:
        start_date, end_date = st.date_input(
            "Rentang Waktu", 
            [all_df["dteday"].min(), all_df["dteday"].max()]
        )
        # Konversi start_date & end_date agar sesuai tipe dengan dteday
        start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)
    else:
        st.error("Data tidak tersedia!")
        start_date, end_date = None, None

# Pastikan start_date & end_date valid sebelum filter
if start_date is not None and end_date is not None:
    filtered_df = all_df[
        (all_df["dteday"] >= start_date) & 
        (all_df["dteday"] <= end_date)
    ]
else:
    filtered_df = all_df.copy()  # Jika tidak ada filter, gunakan semua data

# Generate data for visualization
rentals_per_season = create_rentals_per_season_df(filtered_df)
rentals_per_workingday = create_rentals_per_workingday_df(filtered_df)
rentals_per_weather = create_rentals_per_weather_df(filtered_df)
rentals_per_weekday = create_rentals_per_weekday_df(filtered_df)

# Dashboard layout
st.header('Bike Sharing Dashboard 🚲')

st.subheader('Pola Penggunaan Sepeda Berdasarkan Musim')
fig, ax = plt.subplots()
sns.barplot(x="season", y="cnt", data=rentals_per_season, ax=ax)
st.pyplot(fig)

st.subheader('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
fig, ax = plt.subplots()
sns.barplot(x="weathersit", y="cnt", data=rentals_per_weather, ax=ax)
st.pyplot(fig)

st.subheader('Waktu Puncak Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
fig, ax = plt.subplots()
sns.barplot(x="weekday", y="cnt", data=rentals_per_weekday, ax=ax)
st.pyplot(fig)
