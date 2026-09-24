# Arama motorlarında görünme: yapılacaklar

Sitenin kod tarafı hazır. Aşağıdakiler **panel işlemleri**; koddan yapılamaz,
site sahibinin hesaplarıyla bir kez yapılması gerekir. Sıra, etkiye göredir.

---

## Durum: yönlendirmeler tamam (24.09.2026)

Site sahibi Vercel'de beş alan adının da **Valid Configuration** olduğunu
gördü ve httpstatus.io ile doğruladı:

    https://metapsikoloji.com.tr      308 -> 200
    https://www.metapsikoloji.com.tr  308 -> 200
    https://metapsikoloji.tr          308 -> 200
    http://metapsikoloji.com.tr       308 -> 308 -> 200  (önce https, sonra www)

Hepsi `https://www.metapsikoloji.tr/` adresinde bitiyor, sertifika hatası
yok. Aşağıdaki 0 ve 1 numaralı bölümler artık tarihçe olarak duruyor.

Kalan panel işi: Search Console'da eski `metapsikoloji.com.tr` mülkü için
**Ayarlar -> Adres değişikliği**.

---

## 0-A. Veridyen panelinde "@" tuzağı (23.09.2026'da yaşandı)

Veridyen'in DNS formu **`@` işaretini kök alan adı diye yorumlamıyor**, onu
harfi harfine bir alt alan adı sanıyor. İsim alanına `@` yazılınca kayıt
`metapsikoloji.tr` için değil, `@.metapsikoloji.tr` diye gerçek bir isim
için açılıyor. Panelde kayıt görünüyor, her şey doğru sanılıyor, ama kök
alan adı hâlâ boş kalıyor.

DNS'e sorulduğunda görülen tam olarak buydu:

    @.metapsikoloji.tr   ->  216.198.79.1, 76.76.21.21
    metapsikoloji.tr     ->  (adres yok, yalnızca SOA)

**Doğrusu:** bu panelde İsim alanına tam ana makine adı yazılır. Nitekim
mevcut CNAME satırı da `www.metapsikoloji.tr` olarak duruyor, `www` olarak
değil. Kök için ya alanı **boş bırakın** ya da **`metapsikoloji.tr`** yazın.
Panel ikisini de kabul etmiyorsa destek kaydı açıp "kök (apex) A kaydı
eklenmesini" isteyin.

**Aynı isimde iki A kaydı olmasın.** `76.76.21.21` Vercel'in eski adresi,
`216.198.79.1` güncel olanıdır. İkisi birden durursa ziyaretçilerin yarısı
eskisine düşer. Yalnızca `216.198.79.1` kalmalı.

---

## 0. ACİL: metapsikoloji.tr (www'suz hâli) hiç açılmıyor

21.09.2026 tarihinde DNS kayıtları kontrol edildi. Durum:

| Adres | Nereye gidiyor |
|---|---|
| `www.metapsikoloji.tr` | Vercel (çalışıyor) |
| `metapsikoloji.tr` | **Hiçbir yere. A kaydı yok.** |
| `metapsikoloji.com.tr` | `45.151.250.13` (eski hosting) |
| `www.metapsikoloji.com.tr` | `45.151.250.13` (eski hosting) |

Yani birisi tarayıcıya `metapsikoloji.tr` yazdığında **site açılmıyor**, hata
alıyor. Sadece başına `www.` koyarsa açılıyor.

Bu yalnızca bir konfor sorunu değil, **sitenin aramada çıkmamasının başlıca
sebebi olabilir.** Çünkü sitedeki bütün adres bildirimleri www'suz hâli
gösteriyor:

- `<link rel="canonical" href="https://metapsikoloji.tr/">`
- `sitemap.xml` içindeki adresler
- Open Graph (`og:url`) etiketleri
- JSON-LD yapısal verideki bütün adresler

Google siteyi bulduğunda "asıl adres burası" denen adrese gidiyor ve **açılmayan
bir adresle karşılaşıyor**. Bu durumda sayfayı dizine ekleyemez.

### Çözüm

1. Vercel → proje → **Settings → Domains** listesinde `metapsikoloji.tr`
   (www'suz hâli) **ekli mi** bakın. Ekli değilse ekleyin.
2. Vercel o satırın altında bir **A kaydı** gösterecek (bugünlerde
   `216.198.79.1` gibi bir adres). Alan adının DNS panelinde şu kaydı açın:

   | Tür | Ad / Host | Değer |
   |---|---|---|
   | A | `@` (bazı panellerde boş bırakılır) | *Vercel'in gösterdiği IP* |

3. Kaydı girdikten sonra Vercel'deki satır **Valid Configuration** (yeşil)
   olmalı. Olmuyorsa değer yanlış girilmiştir.

`@` yerine `metapsikoloji.tr` yazmanız gereken paneller de var; panel
hangisini istiyorsa o. Bazı sağlayıcılarda kök alan adına A yerine
**ALIAS / ANAME** kaydı açılır; o da olur, Vercel'in CNAME değerini girin.

Doğrulama: birkaç saat sonra tarayıcıya www olmadan `metapsikoloji.tr` yazın.
Açılıyorsa tamam.

### Daha kolay yol: ad sunucularını Vercel'e taşımak

`metapsikoloji.tr` bölgesinde **www CNAME'inden başka hiçbir kayıt yok**;
23.09.2026'da kontrol edildi, MX de yok TXT de yok. Yani bu alan adıyla
e-posta alınmıyor ve hiçbir doğrulama kaydı durmuyor.

Bu, ad sunucularını Vercel'e taşımayı **risksiz** hâle getiriyor. Taşımanın
normalde tek tehlikesi eski kayıtların kaybolmasıdır; kaybolacak kayıt yok.

Taşınırsa kök A kaydını elle açma derdi tamamen biter, Vercel kökü de www'yu
da kendisi ayarlar. Yapılışı: alan adı Vercel projesine eklenir, Vercel'in
gösterdiği ad sunucuları (`ns1.vercel-dns.com` benzeri) İHS panelinde
tanımlanır. Sonrasında DNS kayıtları Veridyen'de değil Vercel'de yönetilir.

**Not:** ileride bu alan adıyla e-posta alınacaksa MX kayıtları Vercel
tarafında tanımlanmalı. Bugün için böyle bir kayıt olmadığı için taşıma
hiçbir şeyi bozmaz.

### Bunu yönlendirmelerden ÖNCE yapın

Sıra önemli. Yönlendirme, ziyaretçiyi `https://metapsikoloji.tr/` adresine
gönderir. O adres şu an açılmadığı için, yönlendirmeyi önce açarsanız:

- eski site de kapanır,
- yeni site zaten www'suz hâliyle açılmıyordur,
- ve **hiçbir adresiniz çalışmaz.**

Önce bu bölümü bitirin, www'suz adresin açıldığını gözünüzle görün, ancak
ondan sonra 1. bölümdeki yönlendirmeleri devreye alın.

---

## 1. metapsikoloji.com.tr adresini metapsikoloji.tr'ye yönlendirin

**En yüksek etkili adım bu.** `metapsikoloji.com.tr` şu anda Google'da
"Nişantaşı Psikolog | Metapsikoloji" başlığıyla **zaten çıkıyor**. Yeni site
sıfırdan sıra beklerken, eski site aynı marka sorgusunu tutuyor ve ikisi
birbirini zayıflatıyor.

Kalıcı yönlendirme kurulunca eski adresin yıllar içinde biriktirdiği güven yeni
adrese aktarılır ve marka aramasında yeni site çıkmaya başlar.

### Önce karar verin

Yönlendirme kurulduğu anda **eski sitedeki içerik yayından kalkar**; o adrese
gelen herkes yeni siteye düşer. Amaç zaten bu, ama başlamadan önce:

- Eski sitede tutmak istediğiniz yazı, görsel ya da sayfa varsa kopyasını alın.
- **Google Ads reklamlarınızın hangi adrese gittiğini kontrol edin.** Eski adrese
  gidiyorlarsa yönlendirme çalışır ama her tıklama fazladan bir sıçrama yapar;
  reklamların iniş adresini doğrudan `metapsikoloji.tr` yapmak daha iyidir.
- Eski alan adını **iptal etmeyin, elinizde tutun**. Süresi dolarsa yönlendirme
  de biter ve aktardığınız değer kaybolur. En az birkaç yıl yenilenmeli.

### Yol A: Vercel üzerinden (önerilen)

Yeni site zaten Vercel'de olduğu için en temizi bu. Sunucu ayarı gerekmez.

**Doğru sayfada olduğunuzdan emin olun.** Vercel'de iki ayrı "Domains" ekranı
var ve karıştırılması çok kolay:

| Ekran | Nereden açılır | Ne yapar |
|---|---|---|
| **Hesap/takım Domains'i** | Üst menü → Domains | Alan adı **satın alma** ekranı |
| **Proje Domains'i** | Projeye tıklayın → Settings → Domains | Elinizdeki alan adını **bağlama** ekranı |

Add Domain dediğinizde karşınıza satın alınabilir alan adları çıkıyorsa
büyük ihtimalle üstteki hesap ekranındasınız. Önce **projenin adına tıklayın**,
sonra Settings → Domains yolunu izleyin.

Bunu yaptığınız hâlde kutu hâlâ satın alma öneriyorsa:

- Alan adını **uzantısıyla birlikte tam** yazın: `metapsikoloji.com.tr`
  (yalnızca `metapsikoloji` yazarsanız Vercel bunu "satın alınacak isim" sanar
  ve boştaki uzantıları sıralar).
- Açılan listede fiyat etiketi olan satırları değil, **tam olarak yazdığınız
  adı gösteren** satırı seçin. Düğmesinde `Add` / `Connect` / `Use existing`
  benzeri bir ifade olur, fiyat yazmaz.
- Pencerenin üstünde sekme varsa (`Buy` / `Transfer In` / `Add Existing`),
  **Add Existing**'i seçin.
- `.com.tr` uzantısı nic.tr yönetiminde olduğu için Vercel'den **satın
  alınamaz**. Yani satın alma listesinde bu adı hiçbir zaman göremezsiniz;
  doğru yol her hâlükârda "mevcut alan adını bağla" yoludur.

Alan adı projeye eklendikten sonra yönlendirmeyi açın:

1. Domains listesinde `metapsikoloji.com.tr` satırının sağındaki **Edit**
   (ya da üç nokta) düğmesine basın
2. **Redirect to** seçeneğini işaretleyip hedef olarak `metapsikoloji.tr`
   seçin, tür olarak **308 (Permanent)**
3. Aynı işlemi `www.metapsikoloji.com.tr` için de tekrarlayın
4. Vercel her iki satırın altında birer DNS kaydı gösterir. Bunları eski alan
   adının DNS panelinde açmanız gerekir (aşağıda ayrıntılı)
5. DNS yayılması genelde birkaç saat, bazen 24 saat sürer

> **Önemli:** "Redirect to" seçeneği yalnızca hedef alan adı (`metapsikoloji.tr`)
> **aynı projeye** bağlıysa listede görünür. Görünmüyorsa önce onun bağlı
> olduğunu doğrulayın.

### DNS kayıtlarını girmek (Yol A'nın 6. adımı)

Vercel'de yönlendirmeyi tanımlamak tek başına hiçbir şey yapmaz. Vercel
"bu alan adı bana gelirse şunu yaparım" der; **alan adını Vercel'e
yönlendiren şey DNS kaydıdır.** O kayıt girilene kadar eski site yayında
kalır.

#### Önce DNS'i nerede yöneteceğinizi bulun

Alan adını aldığınız firmanın panelinde **Ad Sunucuları / Nameservers**
bölümüne bakın:

- Ad sunucuları **alan adı firmasınınsa** (`ns1.firmaadi.com` gibi), DNS
  kayıtlarını o firmanın panelinde düzenlersiniz.
- Ad sunucuları **hosting firmasınınsa**, kayıtları hosting panelinde
  (cPanel → Zone Editor gibi) düzenlersiniz.

Yanlış panelde yaptığınız değişiklik hiçbir işe yaramaz; tek karışma noktası
budur.

#### Girilecek kayıtlar

`metapsikoloji.com.tr` şu anda `45.151.250.13` adresine, yani eski hostinge
bakıyor. Yapılacak iş **yeni kayıt eklemek değil, var olan kaydı
değiştirmektir**:

| Tür | Ad / Host | Eski değer | Yeni değer |
|---|---|---|---|
| A | `@` (ya da boş) | `45.151.250.13` | *Vercel'in gösterdiği IP* |
| CNAME | `www` | eski hostingi gösteriyor | *Vercel'in gösterdiği CNAME* |

**Eskisini silmeden yenisini eklemeyin.** Aynı isimde iki A kaydı olursa
ziyaretçilerin bir kısmı eski siteye, bir kısmı yenisine düşer; arama
motorları da kararsız kalır.

`www` satırında hâlihazırda bir A kaydı varsa onu silip yerine CNAME açın;
aynı isimde hem A hem CNAME bulunamaz.

#### Dokunmayacağınız kayıtlar

Bu alan adıyla e-posta kullanıyorsanız (`...@metapsikoloji.com.tr`),
**MX kayıtlarına ve e-postayla ilgili TXT kayıtlarına (SPF, DKIM, DMARC)
kesinlikle dokunmayın.** A kaydını değiştirmek e-postayı etkilemez, MX'i
silmek ise gelen kutunuzu durdurur.

#### Sonucu kontrol edin

Vercel'in Domains listesinde her iki satır da **Valid Configuration**
(yeşil) göstermelidir. Birkaç saat geçtiği hâlde göstermiyorsa değer
yanlış girilmiştir; Vercel'deki değeri kopyala-yapıştır yapın, elle
yazmayın.

> 308, Google açısından 301 ile aynı anlama gelir: kalıcı taşınma. İkisi de
> değeri aktarır.

**Vercel yolu sıkıntı çıkarırsa sorun değil.** Aşağıdaki Yol C (alan adı
firmasının kendi yönlendirme aracı) SEO açısından birebir aynı sonucu verir ve
`.com.tr` alan adları için çoğu zaman daha kolaydır.

### Yol B: Eski site kendi sunucusunda kalacaksa

Eski site bir paylaşımlı hostingde (cPanel gibi) duruyorsa, kök dizindeki
`.htaccess` dosyasına şunu ekleyin:

```apache
RewriteEngine On
RewriteCond %{HTTP_HOST} ^(www\.)?metapsikoloji\.com\.tr$ [NC]
RewriteRule ^ https://metapsikoloji.tr/ [R=301,L]
```

Bu kural **her sayfayı** yeni sitenin ana sayfasına gönderir. Yeni site tek
sayfa olduğu için eski adreslerin birebir karşılığı yok; doğrusu budur. Eski
sitede öne çıkan birkaç sayfa varsa onları ayrıca eşleyebiliriz, adreslerini
bana iletmeniz yeterli.

### Yol C: Alan adı firmasının yönlendirme özelliği

Çoğu firmada "Yönlendirme / Forwarding" diye bir alan vardır. Kullanacaksanız
**mutlaka "Kalıcı (301)"** seçin.

**"Çerçeveli / maskeli yönlendirme" (masked / frame forwarding) seçeneğini
seçmeyin.** O seçenek adres çubuğunda eski adresi bırakıp içeriği çerçeve
içinde gösterir; arama motorları bunu taşınma saymaz, hiçbir değer aktarılmaz.

### Yönlendirmeyi doğrulayın

Kurduktan sonra <https://httpstatus.io> adresine `http://metapsikoloji.com.tr`
yazın. Görmeniz gereken zincir:

```
301 (ya da 308)  ->  https://metapsikoloji.tr/   200
```

Tarayıcıda denerseniz adres çubuğunun `metapsikoloji.tr` olarak değişmesi
gerekir. Eski adres kalıyorsa maskeli yönlendirme kurulmuştur, düzeltilmeli.

### Yönlendirmeden sonra: Adres değişikliği bildirimi

Her iki alan adı da Google Search Console'da doğrulanmışsa, eski mülkü seçip
**Ayarlar → Adres değişikliği** aracıyla taşınmayı Google'a bildirin. Bu,
aktarımı belirgin biçimde hızlandırır.

### metapsikolojii.com (çift i) — iptal edildi

Site sahibi 23.09.2026'da bu alan adının ve hostinginin **iptalini verdi**.
Yönlendirme kurulmayacak; `vercel.json`'daki kuralları da bu yüzden
kaldırıldı.

Bilinmesi gerekenler:

- **İptal, adresin hemen kapanması demek değildir.** Alan adı ve hosting
  genelde ödenmiş dönemin sonuna kadar açık kalır. Nitekim tarama anında
  hâlâ `89.252.134.195` adresini gösteriyordu.
- Süresi dolduğunda adres yayından kalkar. O ana kadar eski içerik
  erişilebilir olmaya devam edebilir.
- **Süresi dolduktan sonra alan adı serbest kalır** ve isteyen herkes
  alabilir. Marka adına benzeyen bir alan adının başkasının eline geçmesi
  ileride sorun çıkarabilir. Elde tutmak istemiyorsanız yapılacak bir şey
  yok, ama bu ihtimali bilerek karar verilmiş olsun.
- Google bu adresi zamanla dizinden düşürür. Trafik yönlendirilmediği için
  oradaki birikim yeni siteye aktarılmayacak, kaybolacak. İptal kararı
  verilirken bu bilinçli olarak göze alındı.

#### Alan adlarının son hâli

| Alan adı | Rolü |
|---|---|
| `www.metapsikoloji.tr` | **Asıl adres.** Site burada yayınlanır |
| `metapsikoloji.tr` | Yönlendirme → asıl adres (kök A kaydı bekliyor) |
| `metapsikoloji.com.tr` | Kalıcı yönlendirme → asıl adres (İHS üzerinden kuruldu) |
| `metapsikolojii.com` | İptal edildi, yönlendirilmeyecek |

`metapsikoloji.com.tr` aramada zaten çıkan alan adı olduğu için önemlidir,
**yıllarca elde tutulmalı**; süresi dolarsa yönlendirme ölür ve aktarılan
değer kaybolur.

## 1-A. İHS yönlendirmesinin iki kusuru (24.09.2026 testi)

Site sahibi tarayıcıda test etti, sonuçlar şöyle:

- `http://metapsikoloji.com.tr` açıldı ve **adres çubuğu `metapsikoloji.tr`
  oldu**. Yani maskeli (çerçeveli) yönlendirme değil, o tehlike yok.
- `https://www.metapsikoloji.com.tr` ise
  **`NET::ERR_CERT_COMMON_NAME_INVALID`** verdi.
- httpstatus.io, `http://metapsikoloji.com.tr` için tek satır ve
  **`200`** gösterdi, hiç yönlendirme basamağı yok.

Bu ikisi birlikte tek bir şeye işaret ediyor: İHS'in yönlendirme sunucusu
**gerçek bir 301 döndürmüyor**. `200` ile gerçek bir sayfa veriyor, sayfanın
içinde meta refresh ya da JavaScript yönlendirmesi var; adres çubuğunu
değiştiren o. httpstatus.io yalnızca HTTP düzeyindeki yönlendirmeleri
izlediği için `200`de kalıyor.

Neden sorun:

1. **Sertifika yok.** Chrome artık önce HTTPS deniyor; Google'ın dizinindeki
   eski adresler de büyük ihtimalle `https://`. Googlebot sertifika hatasına
   çarpınca yönlendirmeyi hiç göremez, aktarım gerçekleşmez. Ayrıca marka
   alan adında kırmızı "saldırganlar" uyarısı çıkması güven açısından kötü.
2. **Meta refresh 301 değildir.** Google bunu zayıf ve güvenilmez bir sinyal
   sayar; 301'in aktardığı değeri aktarmaz.

### Çözüm: .com.tr'yi de Vercel'e almak

`metapsikoloji.com.tr` bölgesinde de **MX ve TXT kaydı yok** (24.09.2026'da
kontrol edildi), yani taşımada kaybolacak bir şey yok.

1. Vercel projesine `metapsikoloji.com.tr` ve `www.metapsikoloji.com.tr`
   eklenir
2. İHS'te DNS, Vercel'i gösterecek şekilde ayarlanır (kök için A, www için
   CNAME; değerleri Vercel gösterir)
3. İHS'in kendi yönlendirme özelliği kapatılır

Sonuç: Vercel ücretsiz SSL sertifikasını kendisi üretir, `vercel.json`
içindeki kural da **gerçek 308** döndürür ve yolu korur
(`/iptal-politikasi` gibi adresler karşılığına gider). İki kusur da tek
hamlede kapanır.

## 1-B. Alan adları kütüğü (23.09.2026 DNS taraması)

Son tarama 23.09.2026, 11:30.

| Alan adı | Ad sunucusu | Durum |
|---|---|---|
| `www.metapsikoloji.tr` | veridyen | Çalışıyor, **asıl adres** |
| `metapsikoloji.tr` | veridyen | Kök A kaydı açıldı (`216.198.79.1`, 24.09.2026) |
| `metapsikoloji.com.tr` | ihsdns | Vercel'e taşındı: A `216.198.79.1`, 308 → www (24.09.2026) |
| `www.metapsikoloji.com.tr` | ihsdns | CNAME → Vercel; ftp, mail ve MX kayıtları silindi |
| `metapsikolojii.com` (çift i) | guzelhosting | **Site sahibi iptal etti.** Süresi dolana kadar yayında kalabilir |
| `metapsikoloji.com` (tek i) | domaincontrol (GoDaddy) | Çalışıyor, `160.153.137.218`, **sahibi teyit edilmedi** |

`@.metapsikoloji.tr` kayıtları silinmiş (artık NXDOMAIN), yani 0-A'daki tuzak
fark edilip temizlenmiş. Ama kök için yeni kayıt henüz açılmamış: kök hâlâ
yalnızca SOA döndürüyor. **Bu iş bitmedi.**

`metapsikoloji.com.tr` yönlendirmesi İHS üzerinden kuruldu. DNS tarafı doğru
görünüyor. Yönlendirmenin **türü** buradan doğrulanamıyor (ağ kısıtı); 301
mi yoksa maskeli mi olduğu tarayıcıda adres çubuğuna bakılarak ya da
httpstatus.io ile kontrol edilmeli. Maskeli yönlendirme hiçbir değer aktarmaz.

İHS yönlendirmesi kullanıldığı için `vercel.json`'daki `metapsikoloji.com.tr`
kuralları devreye girmez; trafik Vercel'e uğramıyor. Kurallar zararsız,
ileride DNS Vercel'e taşınırsa yedek olarak durur.

`metapsikoloji.com` ile `metapsikolojii.com` **iki ayrı alan adıdır**, ayrı
firmalarda duruyorlar. Hangisinin site sahibine ait olduğu netleşmeden
ikincisine dokunulmamalı.

### Yönlendirmeler kodda hazır bekliyor

`vercel.json` içindeki host koşullu `redirects` kuralları şu alan adlarını
`https://www.metapsikoloji.tr/` adresine kalıcı (308) olarak gönderir:

    metapsikoloji.tr
    metapsikoloji.com.tr
    www.metapsikoloji.com.tr

Bu kurallar bugün hiçbir şey yapmıyor, çünkü o alan adları Vercel'e
gelmiyor. Her biri için yapılacak iki şey var: alan adını Vercel projesine
eklemek ve DNS'te Vercel'i göstermek. İkisi tamamlanan alan adının
yönlendirmesi kendiliğinden çalışmaya başlar, panelde ayrıca yönlendirme
tanımlamak gerekmez.

## 2. Google Search Console

1. <https://search.google.com/search-console> → "Mülk ekle" → **Alan adı** türü
2. İstenen TXT kaydını alan adı DNS ayarlarına ekleyin
3. Doğrulandıktan sonra **Site haritaları** → `sitemap.xml` gönderin
4. Üstteki arama kutusuna `https://metapsikoloji.tr/` yazıp
   **"Dizine eklenmesini iste"** deyin

Bu son adım olmadan yeni bir sitenin taranması haftalar alabilir.

## 3. Bing Webmaster Tools

<https://www.bing.com/webmasters> → "Google Search Console'dan içe aktar"
seçeneği var, doğrulamayı tekrar yapmaya gerek kalmaz.

## 4. Yandex Webmaster

<https://webmaster.yandex.com.tr> → site ekle → DNS ya da HTML etiketiyle
doğrulayın → site haritasını gönderin. Türkiye'de Yandex payı küçük değil.

## 5. IndexNow (Bing + Yandex'e anında bildirim)

Anahtar dosyası sitede hazır: `/e3017c05809369738e58a7ad7ff55537.txt`

Site yayına alındıktan sonra şu adresi bir kez tarayıcıda açmak yeterli:

```
https://api.indexnow.org/indexnow?url=https://metapsikoloji.tr/&key=e3017c05809369738e58a7ad7ff55537
```

`200` ya da `202` yanıtı başarılı demektir. İçerik değiştikçe tekrar açılabilir.
Google IndexNow kullanmaz, onun için 2. adım gerekir.

## 6. Siteye bağlantı verin

Arama motorları yeni siteleri **başka sitelerdeki bağlantılar üzerinden** bulur.
Hiçbir yerden bağlantı almayan bir site, site haritası gönderilse bile geç
taranır. En hızlı ve doğal olanlar:

- **Instagram biyografisi** (`psk.eminsoydan`) → metapsikoloji.tr
- **LinkedIn profili** → "Web sitesi" alanına ekleyin
- **Google İşletme Profili** → "Web sitesi" alanına ekleyin
- Varsa üye olduğunuz psikolog rehberleri, dernek sayfaları

## 7. Google İşletme Profili

Yerel aramalarda ("Nişantaşı psikolog") haritadaki kayıt siteden daha belirleyici.
Kategori "Psikolog", hizmetler tek tek girilmeli, fotoğraf eklenmeli ve **danışan
yorumu toplanmalı**.

---

## Ne kadar sürer?

| Adım | Etki süresi |
|---|---|
| IndexNow (Bing, Yandex) | Saatler |
| Search Console "dizine ekle" | 1 gün ile 1 hafta |
| Marka sorgusunda ilk sıralar | 2 hafta ile 2 ay |
| Rekabetçi sorgular ("nişantaşı psikolog") | 3 ay ve üzeri |

`metapsikoloji` ve `Psikolog Emin Soydan` marka sorguları olduğu için en hızlı
gelenler bunlar olacak; yeter ki 1. adımdaki çakışma çözülsün.
