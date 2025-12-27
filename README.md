# 🚲 Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis pola peminjaman sepeda menggunakan Bike Sharing Dataset.
Analisis dilakukan menggunakan Google Colab, kemudian hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Dataset
Dataset yang digunakan adalah Bike Sharing Dataset yang terdiri dari:
- day.csv → data peminjaman harian
- hour.csv → data peminjaman per jam

Dataset mencakup informasi jumlah peminjaman sepeda berdasarkan waktu, jenis pengguna (casual dan registered), serta hari kerja dan hari libur.

## Menjalankan Notebook (Google Colab)
1. Buka file notebook (.ipynb) pada repository ini.
2. Klik "Open in Colab".
3. Jalankan setiap cell secara berurutan untuk melihat proses analisis data.

## Menjalankan Dashboard (Local)
1. Install dependencies:
   pip install -r requirements.txt
2. Jalankan dashboard:
   streamlit run app.py

## Dashboard Online
Dashboard dapat diakses secara online melalui link berikut:
https://bike-sharing-dashboard-iqbalkurniawan.streamlit.app/

## Ringkasan Insight
- Pengguna registered mendominasi jumlah peminjaman sepeda, terutama pada hari kerja.
- Pola peminjaman per jam menunjukkan dua puncak utama, yaitu pada pagi dan sore hari.
- Hari kerja memiliki rata-rata peminjaman lebih tinggi dibandingkan hari libur.
- Tren peminjaman harian bersifat fluktuatif mengikuti aktivitas pengguna.

## Requirements
Library Python yang digunakan:
- streamlit
- pandas
- matplotlib
- numpy
- seaborn
