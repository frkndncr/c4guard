# C4Guard - Dosya Arama Uygulaması

C4Guard, kullanıcılara belirtilen bir dizinde dosya araması yapma ve sistem kaynak durumunu izleme imkanı sunan bir web uygulamasıdır. Proje, kullanıcıların istedikleri dosyaları hızlı ve etkili bir şekilde bulmalarını sağlarken, sistem kaynaklarının (CPU, bellek ve disk kullanımı) durumunu da gösterir. Ayrıca, bulunan dosyaların tehlike durumunu belirlemek için VirusTotal entegrasyonu içerir.

## Özellikler

- **Dosya Arama**: Kullanıcıların belirttikleri dizinde dosya araması yapma.
- **Sonuç Listesi**: Bulunan dosyaların isimleri, boyutları, durumları ve tehlike durumları hakkında detaylı bilgi.
- **Sistem Durumu İzleme**: Uygulama, sistemin CPU, bellek ve disk kullanımlarını anlık olarak gösterir.
- **VirusTotal Entegrasyonu**: Bulunan dosyaların güvenlik durumunu kontrol etme.
- **Kullanıcı Dostu Arayüz**: Modern ve responsive bir tasarım ile kullanıcı dostu bir deneyim.

## Gereksinimler

Uygulama, aşağıdaki yazılımlar ve kütüphaneler ile çalışır:

- **Python**: 3.6 veya üzeri
- **Gerekli Kütüphaneler**:
  - Flask: Web uygulaması geliştirme için
  - aiohttp: Asenkron HTTP istemcisi
  - beautifulsoup4: HTML ve XML dosyalarını parse etmek için
  - numpy: Sayısal hesaplamalar için
  - aiohappyeyeballs: Asenkron DNS çözümü

## Kullanım
  Uygulama açıldığında, "Kök Dizin" alanına aramak istediğiniz dizini yazın (örn. C:\Users\DELL\Desktop\).

  "Dosya Adı" alanına aradığınız dosyanın adını yazın (örn. dosya.pdf).

  "Ara" butonuna tıklayarak arama işlemini başlatın.
  Uygulama, belirtilen dizinde dosyaları tarayacak ve sonuçları "Sonuçlar" bölümünde listeleyecektir.
  "Sistem Durumu" bölümünde, sistem kaynak kullanımına dair anlık bilgiler görüntülenecektir.
  Sonuçlar Tablosu
  Arama sonuçları, dosya adı, boyut (KB), sonuç durumu, tehlike durumu ve VirusTotal linki ile birlikte tablo halinde gösterilecektir.

## Kurulum

1. **Depoyu Klonlama**: 
   ```bash
   git clone https://github.com/frkndncr/c4guard.git
   cd c4guard

2. **Gerekli Kütüphaneleri Yükleme**:
   ```bash
   pip install -r requirements.txt

3. **Gerekli Kütüphaneleri Yükleme**:
   ```bash
   python app.py

4. **Paketleri Kaldırma**:
   ```bash
    python uninstall.py

