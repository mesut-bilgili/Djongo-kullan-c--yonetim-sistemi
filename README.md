# 👥 Django & MongoDB (Djongo) Kişi Kayıt ve Yönetim Sistemi

Bu proje; dinamik kişi kaydı, akıllı arama/filtreleme, gelişmiş güncelleme mekanizmaları ve ReportLab entegrasyonu ile fotoğraflı, Türkçe karakter destekli PDF çıktısı üretebilen modern bir web uygulamasıdır. 

Veritabanı olarak NoSQL yapısındaki **MongoDB** kullanılmış, Django ile entegrasyonu **Djongo** ORM aracı ile sağlanmıştır.

---

## 🚀 Öne Çıkan Özellikler

*   **⚡ Dinamik Ön Yüz Düzenleme (No-Admin Edit):** Kullanıcıların admin paneline girmesine gerek kalmadan, ana sayfa üzerinden "Düzenle" butonuyla kayıtları anında forma doldurup güncelleyebilmesini sağlar.
*   **🔍 Işık Hızında Canlı Arama:** Tamamen JavaScript ile çalışan filtreleme mekanizması sayesinde, sayfa yenilenmeden Ad, Soyad veya Telefon bilgisine göre anlık arama yapabilir.
*   **📊 Dinamik Kayıt Sayacı:** Filtreleme esnasında ekranda anlık listelenen kişi sayısını dinamik olarak güncelleyen şık bir sayaç (badge) barındırır.
*   **📄 ReportLab ile PDF Üretimi:** Kayıtlı kişilerin bilgilerini ve yüklenen fotoğraflarını içeren, Türkçe karakter (Arial) destekli profesyonel PDF dosyaları üretir.
*   **🖨️ Akıllı Yazdırma (Print CSS):** "Listeyi Yazdır" butonu tetiklendiğinde form elemanlarını, e-posta, butonlar gibi dinamik alanları gizleyerek kağıda sadece temiz kayıt listesini basar.
*   **🛡️ Güvenli Veri Girişi ve Doğrulama:**
    *   Aynı TC Kimlik numarasıyla ikinci bir kayıt açılmasını engelleyen arka plan (Django views) kontrolü.
    *   Telefon ve TC Kimlik alanlarına sadece rakam girilmesini zorunlu kılan dinamik ön yüz maskelemesi.
*   **🔑 Güvenli Yönetim Paneli:** Kayıt silme işlemleri için Django'nun yerleşik oturum açma (authentication) altyapısına sahip güvenli Admin Paneli entegrasyonu.

---

## 🛠️ Kullanılan Teknolojiler

*   **Backend:** Python 3.x, Django
*   **Database:** MongoDB, Djongo (Connector)
*   **PDF Generation:** ReportLab
*   **Frontend:** HTML5, CSS3, Bootstrap 5, Vanilla JavaScript

---

## 📦 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Projeyi Klonlayın
```bash
git clone [https://github.com/kullanici_adin/Django-kullanici-yonetim-sistemi.git](https://github.com/kullanici_adin/Django-kullanici-yonetim-sistemi.git)
cd Django-kullanici-yonetim-sistemi

### 2. Sanal Ortamı Aktive Edin 
# Windows için:
python -m venv venv
venv\Scripts\activate

# macOS/Linux için:
python3 -m venv venv
source venv/bin/activate

### 3. Gerekli Kütüphaneleri Yükleyin
pip install -r requirements.txt

### 4.Veritabanı Migrasyonlarını Çalıştırın
python manage.py migrate

### 5.Süper Kullanıcı (Yönetici) Oluşturun
python manage.py createsuperuser

### 6. Projeyi Başlatın
python manage.py runserver 
 
# Uygulamayı tarayıcıdan  http://127.0.0.1:8000/ adresinden admin panaline de http://127.0.0.1:8000/admin/ burdan erişebilirsiniz 
