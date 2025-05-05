import streamlit as st
import pandas as pd
import joblib
import time

# Streamlit tema özelleştirme (CSS ile)
st.markdown("""
    <style>
    /* Arka plan ve genel stil */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa 0%, #b2dfdb 100%);
        font-family: 'Verdana', sans-serif;
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Başlık stili */
    h1 {
        color: #ff5722; /* Turuncu neon */
        font-size: 48px;
        text-align: center;
        text-shadow: 2px 2px 4px #f44336;
        margin-bottom: 10px;
        animation: bounceIn 1s;
    }
    @keyframes bounceIn {
        0% { transform: scale(0.8); opacity: 0; }
        60% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); }
    }

    h3 {
        color: #4caf50; /* Yeşil neon */
        font-size: 24px;
        text-align: center;
        text-shadow: 1px 1px 3px #66bb6a;
    }

    /* Dropdown ve butonlar için stil */
    .stSelectbox label {
        color: #4caf50;
        font-weight: bold;
        font-size: 18px;
        text-shadow: 1px 1px 2px #66bb6a;
    }
    .stButton button {
        background: linear-gradient(45deg, #ff9800, #ff5722);
        color: white;
        border-radius: 20px;
        font-size: 18px;
        padding: 12px 25px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 87, 34, 0.4);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #ff7043, #ff5722);
        box-shadow: 0 6px 20px rgba(255, 87, 34, 0.6);
    }

    /* Öneri kartı için stil */
    .suggestion-card {
        background: rgba(255, 255, 255, 0.9);
        border-left: 6px solid #4caf50;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        animation: slideIn 0.5s ease-out;
    }
    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    /* Hata mesajı stili */
    .stError {
        background: rgba(255, 205, 210, 0.9);
        border-left: 6px solid #d32f2f;
        padding: 15px;
        border-radius: 15px;
        animation: shake 0.5s;
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }

    /* Footer stili */
    .footer {
        text-align: center;
        color: #757575;
        font-size: 14px;
        margin-top: 30px;
        padding-top: 10px;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Başlık ve hoş geldin mesajı
st.title("🌾 AgroVision AI – Akıllı Tarım Danışmanı")
st.markdown("### 🌱 Çiftçilere Özel Parlak Fikirler!")
st.markdown("Tarım bilgilerini girerek en iyi yöntemleri keşfet. 🚜 Hazır mısınız?")
st.write("---")

# Veriyi yükle
@st.cache_data
def load_data():
    return pd.read_csv("data/agrovision_ai_veriseti.csv").head(1800)

df = load_data()

# Model ve encoder'ları yükle
model = joblib.load("agrovision_model.pkl")
le_urun = joblib.load("le_urun.pkl")
le_iklim = joblib.load("le_iklim.pkl")
le_toprak = joblib.load("le_toprak.pkl")
le_oneri = joblib.load("le_oneri.pkl")

# Arayüz – Giriş Formu
st.subheader("🔍 Tarım Bilgilerini Girin!")

# Formu düzenli bir şekilde oluştur
with st.form(key="tarim_formu"):
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        urun = st.selectbox("🌿 Ürün Seç", sorted(df["urun"].unique()))
    
    with col2:
        iklim = st.selectbox("☁️ İklim Tipi Seç", sorted(df["iklim_tipi"].unique()))
    
    with col3:
        toprak = st.selectbox("🌍 Toprak Tipi Seç", sorted(df["toprak_tipi"].unique()))
    
    # Butonlar için bir satır
    col_btn1, col_btn2, _ = st.columns([1, 1, 2])
    with col_btn1:
        submit_button = st.form_submit_button("💡 Öneri Al!")
    with col_btn2:
        clear_button = st.form_submit_button("🗑️ Temizle")

# Temizle butonuna basıldığında
if clear_button:
    st.rerun()  # st.experimental_rerun yerine st.rerun kullanıldı

# Öneri Al butonuna basıldığında
if submit_button:
    with st.spinner("🌾 Öneri hesaplanıyor, lütfen bekleyin..."):
        time.sleep(1)  # Simüle edilmiş gecikme
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

            # Sonucu kart içinde göster
            st.markdown(f"""
                <div class="suggestion-card">
                    <h4 style="color: #4caf50;">🌟 ÖNERİ</h4>
                    <p style="font-size: 22px; color: #ff5722;"><b>{oneri}</b></p>
                    <p style="color: #757575;">Bu yöntem, seçtiğiniz koşullar için en iyisi! Daha fazla bilgi için uzmanınıza danışın.</p>
                </div>
            """, unsafe_allow_html=True)
        except ValueError:
            st.error("❌ Üzgünüz, bu kombinasyon için öneri yok! Farklı bir seçim yapmayı dene.")

# Footer
st.markdown("""
    <div class="footer">
        © 2025 AgroVision AI | <a href="https://x.com" target="_blank" style="color: #4caf50;">Bizi Takip Et</a> | Hackathon Projesi
    </div>
""", unsafe_allow_html=True)