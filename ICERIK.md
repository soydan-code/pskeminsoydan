# Doldurulacak içerikler

Metinlerin büyük kısmı yerleştirildi. Aşağıdakiler hâlâ bekliyor.

## 1. Marka varlıkları

| Ne | Nereye gelecek | Durum |
|---|---|---|
| Logo | `assets/img/logo.png` | ✅ Eklendi (beyaz zemin saydamlaştırıldı) |
| Favicon | `assets/img/favicon.png` | ✅ Logodaki psi işaretinden üretildi |
| Marka renkleri | `style.css` → `:root` | ✅ Logodan çekildi |
| Portre fotoğrafı | `assets/img/portre.jpg` | ✅ Eklendi (hero'da çerçeveli) |
| Arka plan fotoğrafları | `assets/img/bg-*.jpg` | ✅ Üç bölümde kullanılıyor |
| Font adı | `style.css` → `--font-heading`, `--font-body` | Şu an Lora + Manrope |

Palet artık sitenin kendi fotoğraflarından geliyor: derin deniz `#0d2a4d`,
deniz `#165290`, orta mavi `#2e73b4`, gök `#6ca7cf`, kehribar `#c49a72`.
Logonun gül tonu `#dd376c` üstteki gradyan şeritte korunuyor.

Fontunuzu hâlâ çekemedim (siteleriniz ağ kısıtı nedeniyle açılmıyor). Font adını
yazmanız yeterli; `--font-heading` ve `--font-body` satırlarında değişiyor.

Fotoğraflar 1500 piksel genişliğe küçültülüp sıkıştırıldı (her biri ~100-130 KB).
Başka bir kare kullanmak isterseniz aynı ada kaydetmeniz yeterli; bölümün
perdesini kontrast için yeniden ölçmek gerekebilir.

## 2. Bekleyen bilgiler

Sayfada kesik çizgili rozetlerle görünen alanlar:

- İptal politikası (seans süresi, sıklık ve ücret yaklaşımı eklendi)
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
