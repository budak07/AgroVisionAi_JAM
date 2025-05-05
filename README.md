AgroVision AI 🌾

Tarım süreçlerini optimize etmek için geliştirilmiş, makine öğrenmesi tabanlı bir akıllı öneri sistemidir. Çiftçilere, seçtikleri ürün, iklim ve toprak koşullarına göre en uygun tarım önerilerini sunar. Bu proje, tarımsal verimliliği artırmak ve sürdürülebilir tarımı desteklemek amacıyla bir hackathon kapsamında geliştirilmiştir.

📋 Proje Amacı AgroVision AI, çiftçilerin tarım kararlarını daha bilinçli almasına yardımcı olmak için:

Ürün, iklim ve toprak koşullarına göre özelleştirilmiş öneriler sunar (örneğin, sulama, gübreleme, ekim zamanı). Makine öğrenmesi ile verilerden öğrenerek daha doğru ve esnek öneriler üretir. Kullanıcı dostu bir Streamlit arayüzü ile kolay erişim sağlar.

🚀 Özellikler Makine Öğrenmesi Modeli: RandomForestClassifier ile eğitilmiş model, ürün, iklim ve toprak verilerini analiz ederek öneriler üretir. Kullanıcı Dostu Arayüz: Streamlit ile geliştirilmiş web tabanlı arayüz, çiftçilerin kolayca öneri almasını sağlar. Veri Odaklı: 50.000 satırlık sentetik tarım verisiyle eğitilmiş model, gerçek dünya senaryolarına uyarlanabilir. Kolay Deploy: Streamlit Cloud ile internete kolayca dağıtılabilir.

🛠️ Teknolojiler Python: Ana programlama dili. Scikit-learn: Makine öğrenmesi modeli (RandomForestClassifier). Pandas: Veri işleme ve analiz. Streamlit: Web arayüzü. Joblib: Model ve encoder’ların kaydedilmesi. GitHub & Streamlit Cloud: Kod depolama ve deploy.

📊 Veri Seti Proje, sentetik_veri_50k_genis.csv adlı sentetik bir veri seti kullanır. Veri seti şu sütunları içerir:

ürün: Ekilen ürün (ör. Kiraz, Buğday). iklim: Bölgenin iklim tipi (ör. Deniz etkisinde, Karasal). toprak: Toprak türü (ör. Kuru, Verimli). öneri: Önerilen tarım uygulaması (ör. Sulama önerilir, Gübreleme gerekli). Veri seti, modelin eğitimi ve test edilmesi için kullanılmıştır. Model, %96 doğruluk oranıyla öneriler üretir.
