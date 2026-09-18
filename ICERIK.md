# Doldurulacak içerikler

Bu dosya, siteyi tamamlamak için sizden gelmesi gereken bilgileri listeler.
Metinleri buraya yapıştırmanız ya da sohbette iletmeniz yeterli; ilgili yerlere
ben yerleştiririm.

## 1. Marka varlıkları

| Ne | Nereye gelecek | Durum |
|---|---|---|
| Logo (SVG veya yüksek çözünürlüklü PNG) | `assets/img/logo.svg` | Geçici logo kullanılıyor |
| Portre fotoğrafı | `assets/img/portre.jpg` | Yer tutucu kutu duruyor |
| Font adı | `assets/css/style.css` içindeki `--font-heading` ve `--font-body` | Şu an Lora + Manrope |
| Marka renkleri | `style.css` içindeki `--accent` ve `--accent-soft` | Şu an koyu yeşil (#2f6b5f) |

Logoyu ve fotoğrafı bu depoya yükleyebilir ya da bana gönderebilirsiniz.

## 2. Metinler

Aşağıdaki bölümlerde şu an genel bir tanıtım metni var. Kendi sitelerinizdeki
yazıları gönderirseniz bunların yerine geçer:

- **Hakkımda** — biyografi, eğitim geçmişi, aldığınız terapi eğitimleri,
  süpervizyon ve mesleki üyelikler. *(Bu bilgileri uydurmadım, boş bıraktım.)*
- **Uzmanlık alanları** — çalıştığınız konuların kendi ifadelerinizle listesi.
- **Terapi süreci** — sürecin sizde nasıl işlediği.
- **Sık sorulan sorular** — özellikle seans ücreti ve iptal politikası.

## 3. İletişim bilgileri

- Telefon numarası
- Ofis adresi (ve varsa harita bağlantısı)
- Çalışma saatleri
- Sosyal medya hesapları (Instagram, LinkedIn vb.)
- İletişim formunun gideceği e-posta — şu an `psikologeminsoydan@gmail.com`
  (`assets/js/main.js` içindeki `ALICI` değişkeni)

## 4. Teknik notlar

- Site tamamen statiktir; Vercel'de derleme adımı gerektirmez.
- İletişim formu sunucu kullanmaz, mesajı ziyaretçinin e-posta uygulamasında
  açar. Doğrudan gelen kutunuza düşmesini isterseniz Formspree benzeri bir
  servise bağlayabilirim.
- Açık ve koyu tema, ziyaretçinin sistem tercihine göre otomatik çalışır.
