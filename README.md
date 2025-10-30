# MLflow + Jenkins Pipeline Demo

Bu proje, Jenkins üzerinden otomatik model eğitimi ve MLflow üzerinden deney takibini gösteren bir **MLOps pipeline** örneğidir.

## 🚀 Çalıştırma
1. Jenkins üzerinde pipeline çalıştırılır.
2. MLflow arayüzü şu komutla açılır:
   ```bash
   mlflow ui --backend-store-uri "file:///C:/ProgramData/Jenkins/.jenkins/workspace/mlflow-jenkins-demo/mlruns" --host 127.0.0.1 --port 5001
Tarayıcıdan http://127.0.0.1:5001
 adresine gidilerek deney sonuçları görüntülenir.
