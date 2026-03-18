# House Prices Prediction Project

Bu proje, konut fiyatlarını tahmin etmek için hazırlanmış başlangıç seviyesi bir **uçtan uca veri bilimi / makine öğrenmesi çalışmasıdır**.  
Projede veri analizi, eksik veri işlemleri, özellik mühendisliği, kategorik verilerin dönüştürülmesi ve farklı regresyon modellerinin karşılaştırılması yapılmıştır.

## Proje Amacı

Bu projenin amacı, evlere ait yapısal ve kategorik özellikleri kullanarak satış fiyatını tahmin etmektir.  
Çalışma boyunca veri ön işleme, model kurma ve performans değerlendirme adımları uygulanmıştır.

## Kullanılan Veri Seti

Projede aşağıdaki dosyalar kullanılmıştır:

- `train.csv` → eğitim verisi
- `test.csv` → test verisi
- `sample_submission.csv` → örnek çıktı formatı
- `data_description.txt` → değişken açıklamaları

Bu veri seti, ev özelliklerine göre fiyat tahmini yapılan klasik bir regresyon problemidir.

## Proje Yapısı

```bash
HOUSE PRICES/
├── .gitignore
├── data_description.txt
├── LICENSE
├── main.py
├── README.md
├── requirement.txt

1. Veri Yükleme ve İnceleme
    * Veri setleri okundu

    * Temel istatistikler incelendi

    * Eksik veriler analiz edildi

    * Hedef değişken (SalePrice) gözlemlendi

2. Veri Ön İşleme

    * Eksik veriler uygun yöntemlerle dolduruldu

    * Kategorik değişkenler dönüştürüldü

    * Gerekli sütunlar düzenlendi

    * Bazı değişkenler üzerinde dönüşüm işlemleri uygulandı

3. Özellik Mühendisliği

    * Yeni anlamlı özellikler üretildi

    * Model performansını artırabilecek birleşik değişkenler oluşturuldu

4. Modelleme

Projede farklı regresyon modelleri denenmiştir. Örnek olarak:

    * Linear Regression

    * Random Forest Regressor

    * Decision Tree Regressor

5. Değerlendirme

Modeller aşağıdaki ölçütlerle karşılaştırılmıştır:

    * RMSE (Root Mean Squared Error)

    * R² Score

    * Cross Validation

Kullanılan Kütüphaneler

Projede şu Python kütüphaneleri kullanılmıştır:

    * pandas

    * numpy

    * matplotlib

    * seaborn

    * scikit-learn

Kurulum

Projeyi kendi bilgisayarında çalıştırmak için:

git clone https://github.com/Zeynep35/house-prices-project.git
cd house-prices-project
pip install -r requirements.txt

Çalıştırma

Ana dosyayı çalıştırmak için:

python main.py

Örnek İş Akışı

Projede genel akış şu şekildedir:

    1. Veri setini yükle

    2. Eksik verileri kontrol et

    3. Ön işleme uygula

    4. Özellik mühendisliği yap

    5. Veriyi eğitim / test olarak ayır

    6. Modelleri eğit

    7. Performansları karşılaştır

    8. En iyi modeli seç

Güçlü Yönler

    * Başlangıç seviyesi için kapsamlı veri hazırlama süreci içerir

    * Birden fazla model karşılaştırılmıştır

    * Cross-validation kullanılmıştır

    * Gerçek bir regresyon problemi üzerinde çalışılmıştır

Geliştirilebilecek Noktalar

Bu proje ileride şu açılardan geliştirilebilir:

    * Kodun src/ klasörüne modüler şekilde ayrılması

    * Pipeline ve ColumnTransformer kullanılması

    * Hyperparameter tuning eklenmesi

    * Feature importance analizi yapılması

    * Son tahminlerin ayrı bir çıktı dosyasına yazdırılması

    * Modelin kaydedilmesi

Hedef

Bu proje, veri bilimi ve makine öğrenmesi öğrenme sürecinde pratik yapmak ve temel bir portföy projesi oluşturmak amacıyla hazırlanmıştır.

Not

Bu çalışma, profesyonel üretim ortamı için değil; öğrenme, deneme ve portföy geliştirme amacıyla hazırlanmıştır.
Buna rağmen veri analizi, preprocessing, feature engineering ve modelleme adımlarını bir arada göstermesi açısından faydalı bir başlangıç projesidir.

Dataset yüklenmedi. Denemek isteyenler Kaggle'dan yükleyebilir. 
Dataset: House Prices - Advanced Regression Techniques (Kaggle)
[House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)