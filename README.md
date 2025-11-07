 MLflow + Jenkins Pipeline Demo

Bu proje, **Yapay Zeka ve Veri Mühendisliği** alanında bir **MLOps otomasyon hattı (CI/CD pipeline)** örneğidir.  
Amaç, makine öğrenimi modellerini **Jenkins** üzerinden otomatik olarak eğitmek,  
ve deney sonuçlarını **MLflow** ile izleyip yönetmektir.

---

## 🇹🇷 **Proje Açıklaması (Türkçe)**

Bu çalışma, **Jenkins** ile CI/CD entegrasyonu yaparak, makine öğrenimi eğitim süreçlerini otomatik hale getirir.  
Her model eğitimi, belirli parametrelerle (örnek: `alpha`, `l1_ratio`) başlatılır ve sonuçlar MLflow üzerinde kaydedilir.  
Proje, **MLOps kavramının** temel prensiplerini göstermektedir.

###  İçerik

### 🔧 Kullanılan Teknolojiler
- **Python 3.11+**
- **Jenkins (Pipeline + Declarative Syntax)**
- **MLflow (Tracking & Model Registry)**
- **scikit-learn**, **pandas**, **pytest**

###  Çalıştırma Adımları
1. Jenkins üzerinde pipeline'ı çalıştırın.  
   (Pipeline otomatik olarak `train.py` dosyasını çağırır ve modeli eğitir.)
2. Eğitim tamamlandıktan sonra MLflow arayüzünü başlatın:
   ```bash
   mlflow ui --backend-store-uri "file:///C:/ProgramData/Jenkins/.jenkins/workspace/mlflow-jenkins-demo/mlruns" --host 127.0.0.1 --port 5001
   Örnek Çıktılar

Eğitim parametreleri: alpha=0.9, l1_ratio=0.2

MLflow’da kayıtlı run ID’leri: sedate-cod-288, kindly-colt-224

Jenkins üzerinden “SUCCESS” pipeline sonucu



