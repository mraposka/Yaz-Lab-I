Formula 1 Telemetri Verileri Analizi

Bu proje, Formula 1 yarışlarının geçmiş yıllara ait verilerini dinamik bir web arayüzünden otomatik olarak toplamak için tasarlanmıştır. Yalnızca Node.js kullanılarak, belirli bir yıl, pist, yarış ve sürücü kombinasyonuna göre verilere ulaşılmış ve detaylı analiz için işlenebilir formatta kaydedilmiştir.

Özellikler
Dinamik web arayüzünden veri toplama.
Yıl, pist, yarış ve sürücü bazında seçim yapma.
Grafik üzerindeki verileri mouse hareketleriyle tarayarak yakalama.
Toplanan verileri .txt formatında dışa aktarma.
Kullanılan Teknolojiler
Node.js: Web tarayıcısını kontrol etmek, dinamik seçimler yapmak ve verileri toplamak için temel araç.
Puppeteer: Tarayıcı otomasyonu ve HTML elementlerinin yakalanması.
Custom Tooltip Handler (tooltip.js): Grafik üzerindeki verileri yakalamak için özel bir JavaScript modülü.
Çalışma Prensibi
Seçim Aşamaları

Kullanıcı belirtilen kombinasyona göre yıl, pist, yarış, ve pilot seçimlerini sırasıyla yapar. Örneğin, Done for 4,1,2,16 şeklinde bir seçimde:
Yıl: 4. indeks → 2020
Pist: 1. indeks
Yarış: 2. indeks
Pilot: 16. indeks
Grafik Verilerinin Yakalanması

Grafik üzerinde veriler yalnızca mouse hareketi sırasında görüntülendiği için, otomatik olarak grafik div’inin solundan sağına doğru her 1 piksel ilerleme yapılarak veriler yakalanır.
İlerleme sırasında eksik veri kalmaması adına, en sağ noktadan 0.5 piksel sola geri hareket yapılır.
Tooltip Verilerinin İşlenmesi

Mouse hareket ettikçe grafik üzerindeki bilgiler, custom-tooltip sınıfına sahip HTML elementleri olarak oluşturulur.
tooltip.js, bu elementlerin içindeki <p> etiketlerini seçerek verileri yakalar ve konsola yazdırır.
Node.js Üzerinden Verilerin Kaydedilmesi

Tarayıcı konsolunda yazılan veriler, Node.js ile page.on('console') olay dinleyicisi aracılığıyla yakalanır ve bir .txt dosyasına kaydedilir.
Çoklu İndeksleme ve Paralel İşleme

Veri toplama işlemi uzun sürdüğü için, farklı indexX.js dosyaları oluşturularak farklı yıl indekslerinden başlanmıştır. Örneğin:
index6.js → 5. yıldan başlayarak veri toplar.
index5.js → 4. yıldan başlayarak veri toplar.
