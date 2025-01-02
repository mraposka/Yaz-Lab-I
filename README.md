---

### Proje Açıklaması:

Bu proje, `.csv` dosyalarındaki zaman serilerini işleyip, bu verilerle bir yapay zeka modelini eğitip, tahminler yapmanızı sağlar. Ayrıca, verileri temizleyip birleştirir, ardından tahminlerde bulunur.

---

### 1. **Gereksinimler**:

Projenin çalışabilmesi için aşağıdaki Python paketlerinin yüklü olması gerekmektedir:

- **numpy**: Matematiksel hesaplamalar için.
- **torch**: PyTorch, makine öğrenmesi için kullanılır.
- **matplotlib**: Grafik çizimleri için.
- **sklearn**: Veriyi normalleştirmek için kullanılır.

Yüklemek için terminalde şu komutları çalıştırabilirsiniz:

```bash
pip install numpy torch matplotlib scikit-learn
```

---

### 2. **Dosya Yapısı**:

Projenin temel dosya yapısı şu şekilde olmalıdır:

```
(project/) 
├── clean.py
├── data.txt
├── output/
│ ├── combined/
│ │ ├── main.py
│ │ ├── f1a-clean.csv # Processed CSV files 
│ │ ├── f1b-clean.csv # Processed CSV files 
│ ├── f1a.csv # Processed CSV files 
└── f1b.csv # Processed CSV files 

```

- **data.txt**: Analiz edilecek ham veri dosyası.
- **clean.py**: Veriyi temizleme ve birleştirme işlemlerini yapan Python dosyası.
- **main.py**: Modelin eğitimini ve tahmin işlemlerini yapan Python dosyası.
- **output/combined/**: İşlenmiş ve birleştirilmiş CSV dosyalarını içeren klasör.

---

### 3. **Veri Temizleme ve Birleştirme (clean.py)**:

Veriyi temizleme ve birleştirme işlemini `clean.py` dosyası yapar.

- **Veri Okuma**: `data.txt` dosyasındaki veriler okunur.
- **Veri Temizleme**: Gereksiz boşluklar, tarih ve saat formatları düzeltilir.
- **CSV Dosyası Oluşturma**: Temizlenen veriler her bir sürücü için ayrı CSV dosyalarına yazılır.
- **CSV Birleştirme**: Oluşan CSV dosyaları birleştirilir.

**Kullanım:**

1. `data.txt` dosyanızı hazırlayın (zaman verilerini içeren dosya).
2. `clean.py` dosyasını çalıştırın:

```bash
python clean.py
```

Bu işlem, verilerinizi temizler ve her bir sürücü için ayrı CSV dosyaları oluşturur. Bu dosyalar `output/combined/` klasörüne kaydedilecektir.

---

### 4. **Model Eğitimi ve Tahmin (main.py)**:

`main.py`, CSV dosyalarındaki verileri okuyarak bir zaman serisi tahmini yapmak için bir yapay zeka modeli kullanır.

- **Veri Okuma**: Her bir CSV dosyasındaki zaman verilerini okur.
- **Özellik Çıkartma**: Zaman serisi verilerini alır, normalleştirir ve model için uygun formata dönüştürür.
- **Model Eğitimi**: Yapay zeka modeli eğitilir.
- **Tahmin**: Eğitilen model ile tahminler yapılır.

**Kullanım:**

1. `output/combined/` klasöründe `.csv` dosyalarının bulunduğundan emin olun.
2. `main.py` dosyasını çalıştırın:

```bash
python main.py
```

Bu işlem, tüm CSV dosyalarını okur ve her biri için zaman serisi tahminleri yapar. Sonuçlar ekranda gösterilecektir ve ayrıca her bir veri için MSE (Mean Squared Error), MAE (Mean Absolute Error) gibi istatistiksel sonuçlar da hesaplanır.

---

### 5. **Sonuçlar ve Grafikler**:

Model eğitildikten sonra şu bilgiler ekranda gösterilecektir:

- **MSE** (Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **MAPE** (Mean Absolute Percentage Error)
- **R-Squared**

Ayrıca, gerçek veriler ve tahminler arasındaki farkları görselleştiren grafikler de çizilecektir.

---

### 6. **Hızlı Başlangıç Örneği**:

1. Verilerinizi **data.txt** dosyasına ekleyin.
2. Temizleme ve CSV oluşturma işlemini başlatın:

```bash
python clean.py
```

3. Ardından **main.py** dosyasını çalıştırarak tahminleri elde edin:

```bash
python output/combined/main.py
```

---
