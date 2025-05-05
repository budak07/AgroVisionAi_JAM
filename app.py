import streamlit as st
import pandas as pd
import joblib

# Başlık
st.title("🌾 AgroVision AI – Akıllı Tarım Danışmanı")

# Veriyi yükle (sadece dropdown'lar için)
@st.cache_data
def load_data():
    return pd.read_csv("data/agrovision_ai_veriseti.csv").head(1800)  # train_model.py ile uyumlu yol

df = load_data()

# Model ve encoder'ları yükle
model = joblib.load("agrovision_model.pkl")
le_urun = joblib.load("le_urun.pkl")
le_iklim = joblib.load("le_iklim.pkl")
le_toprak = joblib.load("le_toprak.pkl")
le_oneri = joblib.load("le_oneri.pkl")

# Arayüz – Giriş Formu
st.subheader("🔍 Tarım Bilgilerini Girin")

urun = st.selectbox("Ürün seçin", sorted(df["ürün"].unique()))
iklim = st.selectbox("İklim tipi seçin", sorted(df["iklim"].unique()))
toprak = st.selectbox("Toprak tipi seçin", sorted(df["toprak"].unique()))

# Butona basınca öneriyi getir
if st.button("💡 Öneri Al"):
    try:
        # Girdileri encode et
        urun_encoded = le_urun.transform([urun])[0]
        iklim_encoded = le_iklim.transform([iklim])[0]
        toprak_encoded = le_toprak.transform([toprak])[0]

        # Model için input oluştur
        input_data = [[urun_encoded, iklim_encoded, toprak_encoded]]

        # Tahmin yap
        tahmin = model.predict(input_data)
        oneri = le_oneri.inverse_transform(tahmin)[0]

        # Sonucu göster
        st.success(f"🧠 ÖNERİ: {oneri}")
    except ValueError:
        st.error("❌ Girilen kombinasyon modelde bulunamadı. Lütfen farklı bir kombinasyon deneyin.")
