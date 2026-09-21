# Arama motorlarında görünme: yapılacaklar

Sitenin kod tarafı hazır. Aşağıdakiler **panel işlemleri**; koddan yapılamaz,
site sahibinin hesaplarıyla bir kez yapılması gerekir. Sıra, etkiye göredir.

---

## 0. ACİL: metapsikoloji.tr (www'suz hâli) hiç açılmıyor

20.09.2026 tarihinde DNS kayıtları kontrol edildi. Durum:

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

### metapsikolojii.com (çift i)

Aramada bu adres de sizin adınıza çıkıyor ("Düzce Psikolog"). Sizinse aynı
yöntemlerden biriyle o da yönlendirilmeli. Değilse ya da artık kullanmıyorsanız
bana söyleyin, bu maddeyi çıkarayım.

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
