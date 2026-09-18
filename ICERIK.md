# Doldurulacak içerikler

Metinlerin büyük kısmı yerleştirildi. Aşağıdakiler hâlâ bekliyor.

## 1. Marka varlıkları

| Ne | Nereye gelecek | Durum |
|---|---|---|
| Logo | `assets/img/logo.png` | ✅ Eklendi (beyaz zemin saydamlaştırıldı) |
| Favicon | `assets/img/favicon.png` | ✅ Logodaki psi işaretinden üretildi |
| Marka renkleri | `style.css` → `:root` | ✅ Logodan çekildi |
| Portre fotoğrafı | `assets/img/portre.jpg` | Yer tutucu kutu duruyor |
| Font adı | `style.css` → `--font-heading`, `--font-body` | Şu an Lora + Manrope |

Logodan alınan renkler: lacivert `#21245f`, indigo `#382e87`, mavi `#4577bf`,
gök mavisi `#5ea4cb`, magenta `#dd376c`, adaçayı `#a9d6a8`.

Fontunuzu hâlâ çekemedim (siteleriniz ağ kısıtı nedeniyle açılmıyor). Font adını
yazmanız yeterli; `--font-heading` ve `--font-body` satırlarında değişiyor.

Portre fotoğrafını `assets/img/portre.jpg` olarak eklerseniz `index.html`
içindeki yer tutucu kutunun yerine geçer (ilgili satır yorum olarak duruyor).

## 2. Bekleyen bilgiler

Sayfada kesik çizgili rozetlerle görünen alanlar:

- Seans süresi ve görüşme sıklığı
- Seans ücreti ve iptal politikası
- Telefon numarası
- Ofis adresi (ve varsa harita bağlantısı)
- Çalışma saatleri
- Sosyal medya hesapları

Eğitim geçmişi, aldığınız formasyonların kurum adları ve mesleki üyelikler de
eklenebilir — şu an metinde yalnızca "3,5 yılı aşan psikanalitik ve dinamik
formasyonlar" ifadesi geçiyor, kurum adı yok.

## 3. Karar bekleyen başlıklar

- **Marka adı:** Üst menüde "metapsikoloji", altında "Psikolog Emin Soydan"
  duruyor. Kişisel adınızı öne almak isterseniz tek satırlık değişiklik.
- **Unvan:** Yüksek lisans tamamlanmadığı için "Uzman Psikolog" yerine
  "Psikolog" kullanıldı. Tez savunmasından sonra güncellenebilir.
- **Blog:** Yazılarınız varsa ayrı bir bölüm eklenebilir.

## 4. Teknik notlar

- Site tamamen statiktir; Vercel'de derleme adımı gerektirmez.
- İletişim formu sunucu kullanmaz, mesajı ziyaretçinin e-posta uygulamasında
  açar. Doğrudan gelen kutunuza düşmesini isterseniz Formspree benzeri bir
  servise bağlanabilir.
- Açık ve koyu tema ziyaretçinin sistem tercihine göre otomatik çalışır.
- Sayfadaki sayılar (7+ yıl, 5.000+ seans) metne sabit yazıldı; zamanla
  güncellenmesi gerekir.
