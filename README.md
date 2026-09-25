# ⚡ Sensör Sinyal Analizi ve Sayısal Filtreleme Paneli

Analog sensörlerden (ivmeölçer, sıcaklık sensörleri) toplanan gürültülü verilerin yazılımsal olarak nasıl filtrelendiğini simüle eden ve analiz eden interaktif web paneli.

🔗 **Canlı Demo:** [https://sernur-sensor-sinyal-paneli.streamlit.app/](https://sernur-sensor-sinyal-paneli.streamlit.app/)

---

## 🎯 Projenin Amacı ve Özellikleri

Fiziksel sensör ölçümlerinde sıklıkla karşılaşılan yüksek frekanslı Gauss gürültüsünü simüle etmek ve sayısal filtreleme algoritmalarının sinyal bütünlüğüne etkisini incelemek amacıyla geliştirilmiştir.

* **Dinamik Sinyal Üretimi:** Ayarlanabilir frekans ve örnekleme aralığında sentetik sinüs dalgası üretimi (NumPy).
* **Gauss Gürültü Simülasyonu:** Gerçek dünya sensör parazitlerini modelleyen ayarlanabilir gürültü katmanı.
* **Sayısal Filtreleme:** Kayan pencere (moving average) algoritmasıyla yüksek frekanslı bileşenlerin temizlenmesi (Pandas).
* **Anlık Mühendislik Metrikleri:** 
  * RMS Hata (Root Mean Square Error)
  * Tepe Gerilim (Peak Voltage)
  * Giriş SNR Değeri (Signal-to-Noise Ratio)
* **İnteraktif Görselleştirme:** Plotly Dark teması ile anlık tepki veren yüksek çözünürlüklü grafikler.

---

## 🛠 Kullanılan Teknolojiler

* **Dil:** Python 3.12+
* **Arayüz & Dağıtım:** Streamlit, Streamlit Community Cloud
* **Veri İşleme:** NumPy, Pandas
* **Görselleştirme:** Plotly Graph Objects
* **Versiyon Kontrol:** Git & GitHub


   
