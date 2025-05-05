import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Veri setini yükle
df = pd.read_csv("data/agrovision_ai_veriseti.csv").head(1800)

# Kategorik verileri encode et
le_urun = LabelEncoder()
le_iklim = LabelEncoder()
le_toprak = LabelEncoder()
le_oneri = LabelEncoder()

df["ürün"] = le_urun.fit_transform(df["urun"])
df["iklim"] = le_iklim.fit_transform(df["iklim_tipi"])
df["toprak"] = le_toprak.fit_transform(df["toprak_tipi"])
df["oneri"] = le_oneri.fit_transform(df["onerilen_yontem"])

# Girdi ve çıktı verilerini ayır
X = df[["ürün", "iklim", "toprak"]]
y = df["oneri"]

# Veriyi eğitim ve test olarak böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğit
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Model doğruluğunu kontrol et
accuracy = model.score(X_test, y_test)
print(f"Model Doğruluğu: {accuracy}")

# Modeli ve encoder'ları kaydet
joblib.dump(model, "agrovision_model.pkl")
joblib.dump(le_urun, "le_urun.pkl")
joblib.dump(le_iklim, "le_iklim.pkl")
joblib.dump(le_toprak, "le_toprak.pkl")
joblib.dump(le_oneri, "le_oneri.pkl")