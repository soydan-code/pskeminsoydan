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

- (Hepsi tamamlandı)

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

İletişim bölümü ikiye ayrıldı: **Ofisler** (Maçka ve Kadıköy, harita
bağlantılı) ve **Yasal adres** (Vişnezade, dokununca açılıyor). Kadıköy
bağlantısı site sahibinden geldi; ağ kısıtı nedeniyle açıp doğrulayamadım.

İkinci ofis **Suadiye** olarak adlandırıldı.

**Eksik:** Suadiye ofisinin açık adresi yok, bu yüzden yapısal veride ayrı bir
konum olarak tanımlanamadı (şu an yalnızca `hasMap` bağlantısı ve `areaServed`
var). Açık adres gelirse ikinci bir `LocalBusiness` kaydı açılabilir; yerel
aramada Kadıköy/Suadiye için bu daha güçlü olur.

**İletişim kısayolları:** WhatsApp bağlantısı hazır mesaj içeriyor
(`wa.me/905436339213?text=...`). Numara `+` olmadan yazılır, wa.me böyle
bekler. LinkedIn ve Instagram hem alt bilgide ikon olarak hem iletişim
listesinde metin olarak, ayrıca şemada `sameAs` alanında.

## 3.5 Ölçüm ve gizlilik

Google Analytics 4 etiketi (`G-00PCBRRYYT`) eklendi, çerez onayına bağlı
çalışıyor. `gizlilik-politikasi.html` sayfası bunu ve sitenin geri kalanını
anlatıyor.

Sayfada uydurulan bilgi yok; yazılanların hepsi sitenin gerçekte yaptığı
şeylerden çıkarıldı (Vercel barındırma, Google Fonts, mailto formu, dış
bağlantılar). VERBİS kaydı, şirket unvanı ya da vergi bilgisi gibi
doğrulanmamış hiçbir şey yazılmadı.

Sitedeki dönüşüm olayları eklendi: WhatsApp, telefon, e-posta ve iletişim
formu, hepsi `generate_lead` adıyla, `method` parametresiyle ayrışıyor.

**Eksik (panel işi, kodla yapılamaz):** GA4 ile Google Ads hesabının
birbirine bağlanması ve `generate_lead` olayının Ads tarafında dönüşüm
olarak içe aktarılması. Bu iki adım tamamlanmadan reklam raporlarında
dönüşüm görünmez.

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
- Sayfadaki sayılar (7+ yıl, 5.000+ seans, 3,5 yıl formasyon, 500+ saat
  süpervizyon) metne sabit yazıldı; zamanla güncellenmesi gerekir.
