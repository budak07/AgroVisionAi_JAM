import streamlit as st
import pandas as pd
import joblib

# Başlık
st.title("🌾 AgroVision AI – Akıllı Tarım Danışmanı")

# Veriyi yükle (sadece dropdown'lar için)
@st.cache_data
def load_data():
    file_path = "data/agrovision_ai_veriseti.csv"
    if not os.path.exists(file_path):
        st.error(f"Hata: Dosya bulunamadı - {file_path}")
        # Uygulamayı durdurabilir veya başka bir işlem yapabilirsiniz
        st.stop() # Streamlit uygulamasını durdurur
        # veya raise FileNotFoundError(f"Dosya bulunamadı: {file_path}") # Daha teknik bir hata fırlatır
    try:
        df = pd.read_csv(file_path).head(1800)
        return df
    except Exception as e:
        st.error(f"Dosya okunurken bir hata oluştu: {e}")
        st.stop()

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
