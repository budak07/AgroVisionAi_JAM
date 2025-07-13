# AgroVision AI 🌾 - Akıllı Tarım Öneri Sistemi

* AgroVision AI, tarım süreçlerini optimize etmek ve sürdürülebilir tarımı desteklemek için makine öğrenmesi tabanlı geliştirilmiş bir akıllı tarım öneri sistemidir. Çiftçilere, seçtikleri ürün, iklim ve toprak koşullarına göre özelleştirilmiş tarım önerileri sunar. Bu proje, Yapay Zeka Teknoloji Akademisi tarafından düzenlenen JAM etkinliği kapsamında Şevval Gürtekin, Murat Gorgoz ve Hasan Budak tarafından tarımsal verimliliği artırmak amacıyla hayata geçirilmiştir.

## 📋 Projenin Amacı
* AgroVision AI, farklı iklim ve toprak koşullarında çiftçilerin tarım kararlarını daha bilinçli ve veri odaklı bir şekilde almalarına yardımcı olmayı hedefler. Sulama, gübreleme ve ekim zamanı gibi konularda kişiselleştirilmiş öneriler sunarak tarımsal üretimi optimize eder ve çevresel sürdürülebilirliği destekler.

## 🚀 Özellikler
* Özelleştirilmiş Öneriler: İklim, toprak ve ürün türüne göre sulama, gübreleme ve ekim zamanı önerileri.
* Makine Öğrenmesi Tabanlı: RandomForestClassifier ile eğitilmiş model, verilerden öğrenerek doğru ve esnek öneriler üretir.
* Kullanıcı Dostu Arayüz: Streamlit ile geliştirilmiş web tabanlı arayüz, çiftçilerin önerilere kolayca erişmesini sağlar.
* Veri Odaklı: 10.000 satırlık sentetik tarım verisiyle eğitilmiş model, gerçek dünya senaryolarına uyarlanabilir.
* Kolay Deploy: Streamlit Cloud ile internete hızlı ve pratik bir şekilde dağıtılabilir.



## 🛠 Teknoloji ve Araçlar
* Programlama Dili: Python
* Kütüphaneler;
* Scikit-learn: RandomForestClassifier modeli için.
* Pandas: Veri işleme ve analiz.
* Streamlit: Kullanıcı dostu web arayüzü tasarımı.
* Joblib: Model ve encoder’ların kaydedilmesi.
* Platformlar:
* GitHub: Kod depolama ve versiyon kontrolü.
* Streamlit Cloud: Web uygulamasının dağıtımı.



## 📊 Veri Seti
* Model, 10.000 satırlık sentetik bir tarım veri setiyle eğitilmiştir. Veri seti aşağıdaki sütunları içerir:

* ürün: Ekilen ürün (ör. Kiraz, Buğday).
* iklim: Bölgenin iklim tipi (ör. Deniz etkisinde, Karasal).
* toprak: Toprak türü (ör. Kuru, Verimli).
* öneri: Önerilen tarım uygulaması (ör. Sulama önerilir, Gübreleme gerekli).
* Veri seti, modelin eğitimi ve test edilmesi için kullanılmıştır. %96 doğruluk oranı ile model, güvenilir ve etkili öneriler üretir.





## 🌟 Kullanım Senaryoları
* Çiftçiler, tarlalarının koşullarına göre en uygun tarım stratejilerini öğrenir.
* Tarım danışmanları, veri odaklı önerilerle çiftçilere rehberlik edebilir.
* Araştırmacılar, tarımsal verimliliği artırmak için modeli genişletebilir veya özelleştirebilir.


## 📢 Gelecek Planları
* Gerçek dünya verileriyle modeli güçlendirme.
* Mobil uygulama entegrasyonu.
* Daha fazla ürün ve iklim türü için öneri genişletme.
* IoT cihazlarıyla entegrasyon (ör. toprak nem sensörleri).





### Not:Yandaki  linkten  yapmış olduğumuz projeyi test edebilirsiniz (https://agrovisionaijam.streamlit.app)
