# Arama motorlarında görünme: yapılacaklar

Sitenin kod tarafı hazır. Aşağıdakiler **panel işlemleri**; koddan yapılamaz,
site sahibinin hesaplarıyla bir kez yapılması gerekir. Sıra, etkiye göredir.

---

## 1. metapsikoloji.com.tr adresini metapsikoloji.tr'ye yönlendirin

**En yüksek etkili adım bu.** `metapsikoloji.com.tr` şu anda Google'da
"Nişantaşı Psikolog | Metapsikoloji" başlığıyla **zaten çıkıyor**. Yeni site
sıfırdan sıra beklerken, eski site aynı marka sorgusunu tutuyor ve ikisi
birbirini zayıflatıyor.

Kalıcı (301) yönlendirme kurulursa eski adresin biriktirdiği güven yeni adrese
aktarılır. Alan adı sağlayıcısının panelinden ya da eski sitenin sunucusundan
yapılır.

Aynı durum `metapsikolojii.com` (çift i) için de geçerliyse o da yönlendirilmeli.

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
