# Bike Sharing Dashboard 🚲

Dashboard ini dibuat untuk menganalisis pola penggunaan sepeda berdasarkan dataset Bike Sharing dari Washington D.C. tahun 2011-2012. Dashboard ini dibangun menggunakan **Python, Pandas, Matplotlib, Seaborn, dan Streamlit**.

## 🌐 Akses Dashboard
Akses dashboard yang sudah dideploy di Streamlit melalui link berikut:
[https://ilham-mulia-bikesharing.streamlit.app/](https://ilham-mulia-bikesharing.streamlit.app/)

## 📂 Struktur Direktori
```
Bike-Sharing-Dashboard/
│── Dashboard/
│   │── all_data.csv
│   │── logo.png
│   │── run.py
│
│── Data/
│   │── Readme.txt
│   │── day.csv
│   │── hour.csv
│── Notebook.ipynb
│── requirements.txt
│── README.md
```

## 📦 Setup Environment - Anaconda
```bash
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install -r requirements.txt
```

## 🛠️ Setup Environment - Shell/Terminal
```bash
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

## 🚀 Jalankan Streamlit App
```bash
streamlit run Dashboard/run.py
```
