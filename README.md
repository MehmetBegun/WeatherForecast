# Weather Forecast
Basit bir Python uygulamasıyla OpenWeatherMap API’yi kullanarak istediğiniz şehrin güncel hava durumunu ve sıcaklığını getirir.

## Özellikler
- Şehir adıyla anlık hava durumu sorgulama  
- JSON parse hatası ve API hata mesajlarını kullanıcıya bildirir  
- `requests` kütüphanesiyle HTTP istekleri  

## Gereksinimler
- Python 3.6+  
- `requests` kütüphanesi  
- OpenWeatherMap API anahtarı  

## Kurulum
1. Depoyu klonlayın veya dosyaları indirin:  
   git clone https://github.com/kullanici/WeatherFetcher.git
   cd WeatherFetcher
   
Gerekli paketi yükleyin:
pip install requests

## Kullanım
python weather.py
İstendiğinde şehir adını (ör. Istanbul) yazın.
Ekrana “Sıcaklık: XX°C”, “Hava Durumu: …” gibi bilgiler basılır.

## Hata Yönetimi

Geçersiz API anahtarı, yanlış şehir adı veya JSON parse hatası durumunda ekranda anlamlı bir uyarı mesajı gösterilir.

## Dosya Yapısı
WeatherFetcher/
├── weather.py       # Ana kod
└── README.md        # Bu dosya
