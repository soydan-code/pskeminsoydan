# metapsikoloji — site notları

Statik tek sayfa site. Derleme adımı yok; Vercel doğrudan `index.html` dosyasını
servis eder.

## Dosya düzeni

- `index.html` — tüm sayfa
- `assets/css/style.css` — tema değişkenleri en üstte (`--font-*`, renkler)
- `assets/js/main.js` — mobil menü ve iletişim formu (mailto)
- `ICERIK.md` — hâlâ eksik olan içerik ve varlıkların listesi

## Renk paleti

Renkler sitenin kendi fotoğraflarından (Boğaz, gün batımı, Kız Kulesi)
türetildi ve `style.css` içindeki `:root` bloğunda tanımlı: derin deniz
`#0d2a4d`, deniz `#165290`, orta mavi `#2e73b4`, gök `#6ca7cf`, kehribar
`#c49a72`, koyu kehribar `#9a5f2c` (çağrı butonları). Logonun gül tonu
`#dd376c` yalnızca üstteki gradyan şeritte, markayla bağı korumak için durur.

Koyu tema gece Boğaz'ıdır: zemin `#0a1a2e`, vurgu gök mavisi `#8cc3ec`,
çağrı kehribar `#e0a66a`.

## Fotoğraflı bölümler

`.photo-section` sınıfı fotoğrafın üzerine sabit koyu bir perde koyar ve
bölüm içindeki renk değişkenlerini açık tonlarla ezer; böylece metin hem
temadan hem de fotoğrafın hangi bölgesine denk geldiğinden bağımsız olarak
okunur kalır. Şu an hero (gün batımı), `#koltuk` (Kız Kulesi) ve `#online`
(sahil) bu sınıfı kullanır.

Yeni bir fotoğraflı bölüm eklerken perdeyi ölçerek doğrulayın: bölümdeki
metinleri gizleyip ekran görüntüsü alın ve **en parlak zemin pikselini**
bulun; en soluk metin rengi (`#d8e4f0`) o piksele karşı en az 4.5:1 vermeli.
Kız Kulesi karesinin göğü parlak olduğu için o bölüm ayrıca koyulaştırıldı.

## Erişilebilirlik

Yeni renk eklerken WCAG AA kontrastı (normal metin 4.5:1, büyük metin 3:1)
açık ve koyu temanın ikisinde de sağlanmalı. `.nav a` gibi genel seçicilerin
`.btn` rengini ezmemesine dikkat edin — bu daha önce menüdeki butonu okunmaz
hâle getirmişti.

## SEO

Alan adı `metapsikoloji.tr`. Canonical, `sitemap.xml`, `robots.txt` ve Open
Graph etiketleri bu adrese göre yazıldı; alan adı değişirse hepsi güncellenmeli.
Vercel `cleanUrls` açık, bu yüzden iç bağlantılar `.html` uzantısız yazılır
(`/iptal-politikasi`).

`index.html` sonundaki JSON-LD bloğunda `FAQPage` şeması var ve **sayfadaki
görünür SSS metniyle birebir aynı olmak zorunda**. Google, şemayla görünen
içeriğin uyuşmamasını yaptırım sebebi sayar. SSS'de bir soru ya da yanıt
değiştirildiğinde şemayı elle düzenlemeyin, şunu çalıştırın:

    python3 tools/sss-semasi-guncelle.py

Arama motorlarına kaydolma adımları (Search Console, Bing, Yandex, IndexNow,
alan adı yönlendirmesi) `SEO-ADIMLAR.md` dosyasında. Kök dizindeki
`e3017c05809369738e58a7ad7ff55537.txt` IndexNow anahtar dosyasıdır, silinmemeli.

Marka adı "metapsikoloji" hem üst bilgide hem alt bilgide logo **görseli**
olarak geçiyor. Alt bilgiye ayrıca görünür metin olarak eklendi; arama
motorları için görsel alt metni tek başına zayıf bir sinyal.

## Çerez onayı ve ölçüm

Google etiketi (GA4, `G-00PCBRRYYT`) **onaya bağlıdır ve bu bozulmamalıdır.**
Üç HTML dosyasının `<head>` bölümünde yalnızca izin varsayılanları tanımlıdır
(hepsi `denied`); `gtag.js` orada yüklenmez. Etiketi yükleyen tek yer
`main.js` içindeki `etiketiYukle`, o da ziyaretçi şeritte kabul ettiğinde
ya da daha önce kabul etmişse çalışır.

Sonuç: JavaScript çalışmazsa şerit görünmez ve izleme de olmaz. Güvenli taraf
budur, tersine çevirmeyin.

Şerit `main.js` tarafından oluşturulur, HTML'de durmaz; böylece üç sayfada tek
bir metin vardır. Alt bilgideki "Çerez tercihleri" düğmesi de aynı yerden
eklenir, kararı değiştirmek için bu düğme kullanılır.

Karar `localStorage` içinde `cerez-onayi-v1` anahtarıyla saklanır. Metin ya da
kapsam değişirse anahtarın sonundaki sürümü artırın; eski onaylar geçersiz olur
ve şerit herkese yeniden sorar.

Ölçümle ilgili bir değişiklik yapıldığında `gizlilik-politikasi.html`
içindeki çerez listesi ve açıklamalar da güncellenmeli. O sayfa sitenin
gerçekte ne yaptığını anlatır; ikisinin ayrışması hem yanlış beyan olur hem de
KVKK açısından sorun yaratır.

## İletişim kısayolları

WhatsApp, telefon ve sosyal medya bağlantıları üç yerde: hero butonları,
iletişim bölümünün üstündeki hızlı erişim satırı ve alt bilgideki ikonlar.
Ayrıca `#yuzenWa` yüzen düğmesi var; `main.js` bunu ilk ekranda ve iletişim
bölümü görünürken gizler, arada gösterir. Düğme WhatsApp yeşili değil marka
lacivertidir; paletle çakışmaması için böyle seçildi.

Bağlantılar tek yerde değil, HTML'e gömülü. Numara ya da hesap değişirse
`index.html` ve `iptal-politikasi.html` içinde ve JSON-LD'nin `sameAs`
alanında güncellenmeli.

## Önbellek ve statik dosyalar

Dosya adlarında içerik özeti (hash) yok. Bu yüzden `vercel.json` içinde CSS ve
JS `no-cache` ile servis edilir; her istekte doğrulanır, değişmemişse 304 döner.
Görseller bir hafta önbelleklenir.

Bu kural bir kere ihlal edildi ve site bozuldu: CSS bir gün önbelleğe alınmıştı,
yeni HTML eski stille eşleşti ve `.ikon` kuralı bulunmayınca satır içi SVG'ler
300×150 varsayılan boyutunda açıldı, butonlar dev dairelere dönüştü. İki önlem
var, ikisini de bozmayın:

1. Satır içi SVG'lerde **`width` ve `height` öznitelikleri bulunur**. CSS
   gelmese bile ikon makul boyutta kalır. Yeni ikon eklerken bunları da yazın.
2. CSS ya da JS'te davranış değiştiren bir düzenleme yaptığınızda `index.html`
   ve `iptal-politikasi.html` içindeki `?v=` sürüm numarasını artırın.

## Metin yazarken üslup

Site sahibi: 2019'da mezun, 7 yılı aşkın klinik deneyim ve 5.000+ seans saati olan
psikoterapist. 3,5 yılı aşan psikanalitik/psikodinamik formasyon. Yapay zekânın
girişimciler üzerindeki psikolojik etkileri üzerine tezli yüksek lisans sürüyor.
14 yaş üzeri ergenler ve yetişkinlerle **bireysel** dinamik psikoterapi yürütüyor —
çift ve aile çalışması yapmıyor, çocuk danışan kabul etmiyor.

EMDR eğitimi var. Bu yöntem **ana çerçeve değil**: ağırlıklı olarak travma ve
TSSB çalışmalarında, ayrıca vakanın uygun olduğu durumlarda danışan talebiyle
kullanılıyor. Sürecin çerçevesi her hâlükârda psikodinamik psikoterapidir.

Yüz yüze görüşmeler Kadıköy ve Nişantaşı merkezli birkaç lokasyonda yapılıyor;
iletişim bölümündeki adres bunlardan biridir (Google işletme kaydı).

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
