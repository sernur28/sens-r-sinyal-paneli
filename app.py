import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 1. Sayfa Yapılandırması ve İkon
st.set_page_config(
    page_title="Sensör Sinyal Laboratuvarı",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Sensör Sinyal Analizi ve Sayısal Filtreleme")
st.caption("Analog sensör çıkışlarının sayısal hareketli ortalama (moving average) filtresiyle anlık analizi.")

# 2. Yan Menü Kontrolleri
st.sidebar.header("Kontrol Paneli")

sensor_tipi = st.sidebar.selectbox(
    "Hedef Sensör Modeli",
    ["Endüstriyel İvmeölçer (Titreşim)", "Hassas Sıcaklık Sensörü (PT100/RTD)", "Biyomedikal Sinyal (Simülasyon)"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Sinyal Parametreleri")
frekans = st.sidebar.slider("Sinyal Frekansı (Hz)", min_value=1, max_value=25, value=5)
gurultu_miktari = st.sidebar.slider("Gürültü Genliği (Gauss)", min_value=0.0, max_value=2.0, value=0.6, step=0.1)
filtre_boyutu = st.sidebar.slider("Filtre Pencere Boyutu", min_value=3, max_value=35, value=11, step=2)

st.sidebar.markdown("---")
st.sidebar.info(f"Aktif İzleme: **{sensor_tipi.split(' ')[0]}**")

# 3. Sentetik Sinyal ve Gürültü Üretimi
zaman = np.linspace(0, 1, 600)  # 600 örnekleme noktası
temiz_sinyal = np.sin(2 * np.pi * frekans * zaman)
gurultu = np.random.normal(0, gurultu_miktari, len(zaman))
ham_sinyal = temiz_sinyal + gurultu

# 4. Sayısal Filtreleme Algoritması
filtreli_sinyal = pd.Series(ham_sinyal).rolling(window=filtre_boyutu, center=True).mean().bfill().ffill().values

# 5. Özel Tasarımlı Grafik Alanı
fig = go.Figure()

# Ham sinyal: Yarı saydam duman tonu (arka plan gürültüsü hissi verir)
fig.add_trace(go.Scatter(
    x=zaman, y=ham_sinyal,
    mode="lines",
    name="Ham Gürültülü Veri",
    line=dict(color="rgba(200, 200, 200, 0.35)", width=1.2)
))

# Filtrelenmiş sinyal: Sıcak altın / kehribar tonu (özel odak noktası)
fig.add_trace(go.Scatter(
    x=zaman, y=filtreli_sinyal,
    mode="lines",
    name="Filtrelenmiş Sinyal",
    line=dict(color="#E0A96D", width=2.8)
))

# Teorik referans: İnce beyaz kesikli çizgi
fig.add_trace(go.Scatter(
    x=zaman, y=temiz_sinyal,
    mode="lines",
    name="Teorik İdeal Sinyal",
    line=dict(color="#FFFFFF", dash="dot", width=1.5)
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    xaxis=dict(title="Zaman (saniye)", gridcolor="#21262D"),
    yaxis=dict(title="Genlik (V)", gridcolor="#21262D"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# 6. Mühendislik Metrik Kartları
col1, col2, col3, col4 = st.columns(4)

rms_hata = np.sqrt(np.mean((filtreli_sinyal - temiz_sinyal)**2))
snr_degeri = 10 * np.log10(np.var(temiz_sinyal) / (np.var(gurultu) + 1e-6))

col1.metric("Örnek Sayısı", f"{len(zaman)} nokta")
col2.metric("Tepe Gerilimi", f"{np.max(np.abs(ham_sinyal)):.2f} V")
col3.metric("RMS Hata Oranı", f"{rms_hata:.4f}")
col4.metric("Giriş SNR Değeri", f"{snr_degeri:.1f} dB")