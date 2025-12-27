import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Analisis Peminjaman Sepeda",
    layout="wide"
)

st.title("🚲 Dashboard Analisis Peminjaman Sepeda")
st.write("Dashboard ini menampilkan visualisasi utama dan ringkasan insight dari data peminjaman sepeda.")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    return day_df, hour_df

day_df, hour_df = load_data()
st.write("✅ day.csv terbaca, jumlah baris:", day_df.shape)
st.write("✅ hour.csv terbaca, jumlah baris:", hour_df.shape)
st.write("Kolom day.csv:", list(day_df.columns))
st.write("Kolom hour.csv:", list(hour_df.columns))

# =========================
# PREVIEW DATA
# =========================
with st.expander("📄 Lihat Preview Data"):
    st.subheader("Data Harian (day.csv)")
    st.dataframe(day_df.head())

    st.subheader("Data Per Jam (hour.csv)")
    st.dataframe(hour_df.head())

# =========================
# VISUALISASI UTAMA
# =========================
st.header("📊 Visualisasi Utama")

col1, col2 = st.columns(2)

# 1. Tren Peminjaman Harian
with col1:
    st.subheader("Tren Total Peminjaman Harian")
    fig, ax = plt.subplots()
    ax.plot(day_df["cnt"], color="blue")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

# 2. Rata-rata Peminjaman per Jam
with col2:
    st.subheader("Rata-rata Peminjaman per Jam")
    hourly_avg = hour_df.groupby("hr")["cnt"].mean()

    fig, ax = plt.subplots()
    sns.barplot(x=hourly_avg.index, y=hourly_avg.values, ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig)

# =========================
# RINGKASAN INSIGHT
# =========================
st.header("🧠 Ringkasan Insight")

total_rentals = day_df["cnt"].sum()
avg_daily = day_df["cnt"].mean()
peak_hour = hourly_avg.idxmax()

st.markdown("""
- 📌 **Pengguna registered mendominasi peminjaman sepeda** dibandingkan pengguna casual, khususnya pada hari kerja.
- 📌 **Pola peminjaman per jam menunjukkan dua puncak**, yaitu pada pagi hari (jam berangkat kerja) dan sore hari (jam pulang kerja).
- 📌 **Hari kerja memiliki total peminjaman lebih tinggi** dibandingkan hari libur.
- 📌 **Rata-rata peminjaman harian bersifat fluktuatif**, mengikuti pola aktivitas pengguna.
- 📌 Insight ini merupakan ringkasan dari hasil analisis eksploratif data yang dilakukan pada Google Colab.
""")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Dashboard dibuat menggunakan Streamlit | Data: Bike Sharing Dataset")
