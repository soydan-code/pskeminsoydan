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

İletişim bilgileri, çalışma saatleri ve iptal politikası eklendi. Geriye
kalan:

- Sosyal medya hesapları (Instagram, LinkedIn vb.)

Adres artık Google işletme kaydına yönleniyor
(`https://maps.app.goo.gl/txqexG4cu7dfvaj76`). Bağlantıyı site sahibi
verdi; ağ kısıtı nedeniyle buradan açıp doğrulayamadım.

`iptal-politikasi.html` içeriği site sahibinin kendi kararlarıyla yazıldı:
ödeme seansa gelirken ya da hemen ardından, iptal bildirimi en az bir hafta
önce, haber verilmeyen görüşmeler için ücret alınmaz (sık tekrarlarda ödeme
anlaşması yeniden gözden geçirilir).

**Yazım kuralı:** Sitede uzun çizgi (—) parantez işareti olarak
kullanılmayacak. Gerektiğinde virgül ya da normal parantez tercih edilir.

Eğitim geçmişi, aldığınız formasyonların kurum adları ve mesleki üyelikler de
eklenebilir — şu an metinde yalnızca "3,5 yılı aşan psikanalitik ve dinamik
formasyonlar" ifadesi geçiyor, kurum adı yok.

## 3. SEO için yapılmayanlar

Site sahibinin Google Ads anahtar kelime listesinde olup **siteye bilerek
eklenmeyenler** ve sebepleri:

- **Bütüncül psikoterapi** — site sahibinin kararıyla çıkarıldı; odak
  "psikodinamik psikoterapi".
- **İlişki terapisi** — çift çalışması yapılmıyor. İlişkiler yalnızca bireysel
  çalışma teması olarak geçiyor.
- **"tedavi" ifadeleri** — psikolog unvanıyla "tedavi" iddiası hukuken riskli.
  "Psikolojik destek / çalışma" tercih edildi.
- **Yönetici** — hangi hizmete karşılık geldiği belirsiz, site sahibine soruldu,
  yanıt bekleniyor.

Sonradan eklenenler: **EMDR** (eğitim teyit edildi, travma çalışması ve uygun
vakalarla sınırlı olarak), **Kadıköy** (yüz yüze lokasyonlardan biri olduğu
teyit edildi), **metapsikoloji / Psikoterapist Emin Soydan** (marka ve unvan
varyantları şemaya `alternateName` olarak girildi).

**Tutarsızlık uyarısı:** SSS "Kadıköy ve Nişantaşı merkezli birkaç lokasyon"
diyor ama iletişim bölümünde tek adres görünüyor. Kadıköy adresini de eklemek
ya da etiketi değiştirmek isterseniz söylemeniz yeterli.

## 4. Karar bekleyen başlıklar

- **Marka adı:** Üst menüde "metapsikoloji", altında "Psikolog Emin Soydan"
  duruyor. Kişisel adınızı öne almak isterseniz tek satırlık değişiklik.
- **Unvan:** Yüksek lisans tamamlanmadığı için "Uzman Psikolog" yerine
  "Psikolog" kullanıldı. Tez savunmasından sonra güncellenebilir.
- **Blog:** Yazılarınız varsa ayrı bir bölüm eklenebilir.

## 5. Teknik notlar

- Site tamamen statiktir; Vercel'de derleme adımı gerektirmez.
- İletişim formu sunucu kullanmaz, mesajı ziyaretçinin e-posta uygulamasında
  açar. Doğrudan gelen kutunuza düşmesini isterseniz Formspree benzeri bir
  servise bağlanabilir.
- Açık ve koyu tema ziyaretçinin sistem tercihine göre otomatik çalışır.
- Sayfadaki sayılar (7+ yıl, 5.000+ seans) metne sabit yazıldı; zamanla
  güncellenmesi gerekir.
