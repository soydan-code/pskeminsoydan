# metapsikoloji — site notları

Statik tek sayfa site. Derleme adımı yok; Vercel doğrudan `index.html` dosyasını
servis eder.

## Dosya düzeni

- `index.html` — tüm sayfa
- `assets/css/style.css` — tema değişkenleri en üstte (`--font-*`, renkler)
- `assets/js/main.js` — mobil menü ve iletişim formu (mailto)
- `ICERIK.md` — hâlâ eksik olan içerik ve varlıkların listesi

## Renk paleti

Renkler logodan türetildi ve `style.css` içindeki `:root` bloğunda tanımlı:
lacivert `#21245f` (birincil), indigo `#382e87` (bağlantılar), mavi `#4577bf`,
gök mavisi `#5ea4cb`, magenta `#dd376c` (çağrı butonları, `#c9295c` olarak
koyulaştırılmış hâliyle), adaçayı `#a9d6a8` (yumuşak zeminler).

Yeni renk eklerken WCAG AA kontrastı (normal metin 4.5:1, büyük metin 3:1) açık
ve koyu temanın ikisinde de sağlanmalı. `.nav a` gibi genel seçicilerin `.btn`
rengini ezmemesine dikkat edin — bu daha önce menüdeki butonu okunmaz hâle
getirmişti.

## Metin yazarken üslup

Site sahibi: 2019'da mezun, 7 yılı aşkın klinik deneyim ve 5.000+ seans saati olan
psikoterapist. 3,5 yılı aşan psikanalitik/psikodinamik formasyon. Yapay zekânın
girişimciler üzerindeki psikolojik etkileri üzerine tezli yüksek lisans sürüyor.
14 yaş üzeri ergenler ve yetişkinlerle **bireysel** dinamik psikoterapi yürütüyor —
çift ve aile çalışması yapmıyor, çocuk danışan kabul etmiyor.

Kuramsal zemin üç katmanlı:

- **Winnicott** — seans, sahte kendilik savunmalarının gevşeyebildiği bir
  "kucaklayıcı çevre"dir. Destekleyici zemin sürekli isimlendirilir, imgelenir.
- **Aktarım Odaklı Terapi (TFP)** — "şimdi ve burada" kurulan terapist–danışan
  ilişkisi sürecin pusulasıdır.
- **Lacan** — özne dilin içinde kurulur; sözcüklerin ardındaki gösterenler,
  ötekinin bakışı ve arzunun dolaylı yolları dinlenir.

Ton: sıcak, güven veren, metaforik, şiirsel bir psikanalitik duyarlılık.
Didaktik, soğuk ya da reçete veren bir uzman dili **kullanılmaz**. "Şu 5 adımı
uygulayın" türü vaatler, garanti edilen sonuçlar ve pazarlama dili bu sitede yer
almaz.

## Uydurulmayacak bilgiler

Eğitim kurumları, sertifika adları, üyelikler, seans ücreti, seans süresi,
görüşme sıklığı, telefon ve adres — bunlar yalnızca site sahibinden geldiğinde
yazılır. Gelene kadar `.todo` sınıfıyla işaretli yer tutucu olarak kalır.
