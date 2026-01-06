# 📊 E-Ticaret Satış Analizi

Bu proje, bir e-ticaret firmasının satış verilerinin Python, SQL ve Power BI kullanılarak analiz edilmesini kapsamaktadır.

## 🔍 Proje Amaçları
- Satış performansını analiz etmek
- Ülkelere göre satış dağılımını incelemek
- En çok ciro ve satış adedi oluşturan ürünleri belirlemek
- Müşteri tiplerine (Registered / Guest) göre gelir katkısını karşılaştırmak
- Power BI ile etkileşimli bir dashboard oluşturmak

## 🧰 Kullanılan Teknolojiler
- **Python** (Pandas, NumPy)
- **SQL Server**
- **Power BI**
- **Jupyter Notebook**

## 📁 Proje Yapısı
- `data/` : Temizlenmiş veri seti
- `notebook/` : Veri temizleme ve feature engineering
- `sql/` : Analiz sorguları
- `powerbi/` : Dashboard şablonu ve görsel önizleme

## 📈 Power BI Dashboard
Dashboard aşağıdaki metrikleri içermektedir:
- Toplam ciro (Total Price)
- Toplam satış adedi (Quantity)
- Ürün bazlı Top 10 analizleri
- Ülkelere göre satış dağılımı
- Müşteri tiplerine göre gelir oranları
- Zaman bazlı (Yıl / Ay) analizler

![Dashboard Preview](powerbi/dashboard_preview.png)

## 📌 Notlar
Bu projede kullanılan Power BI dosyası şablon formatındadır (.pbit) ve veri içermemektedir. Dashboard, SQL Server bağlantısı üzerinden yeniden kullanılabilir yapıdadır.
