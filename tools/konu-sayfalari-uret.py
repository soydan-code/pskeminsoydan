#!/usr/bin/env python3
"""Konu sayfalarını (tools/konular.py) ve /calisma-alanlari merkez sayfasını üretir.

Şablon olarak psikolog-kadikoy-suadiye.html kullanılır; böylece üst menü, alt
bilgi, çerez onayı ve Google etiketi sitenin geri kalanıyla aynı kalır.
Görünen SSS ile FAQPage şeması aynı veriden üretildiği için ayrışamaz.

    python3 tools/konu-sayfalari-uret.py
"""
import html, json, pathlib, re, sys

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "tools"))
from konular import KONULAR, GRUPLAR, GUNCELLEME  # noqa: E402

SITE = "https://www.metapsikoloji.tr"
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


def tarih_yazi(tarih):
    y, a, g = tarih.split("-")
    return f"{int(g)} {AYLAR[int(a) - 1]} {y}"


def guncel(k):
    """Sayfanın son güncelleme tarihi: ilk yayından önce olamaz."""
    return max(k["yayin"], GUNCELLEME)


sablon = (KOK / "psikolog-kadikoy-suadiye.html").read_text(encoding="utf-8")
bas = sablon[:sablon.index('<main id="icerik">')]
son = sablon[sablon.index("</main>") + len("</main>"):]
cta_m = re.search(r'<div class="cta-satir".*?</div>', sablon, re.S).group(0)


def cta(etiket):
    return re.sub(r'aria-label="[^"]*"', f'aria-label="{etiket}"', cta_m, count=1)


def duz(metin):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", metin))).strip()


def bas_hazirla(title, desc, url, tur="article"):
    h = bas
    h = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title, False)}</title>", h)
    for ad in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        h = re.sub(rf'<meta {ad} content=".*?">', f'<meta {ad} content="{html.escape(desc)}">', h)
    for ad in ('property="og:title"', 'name="twitter:title"'):
        h = re.sub(rf'<meta {ad} content=".*?">', f'<meta {ad} content="{html.escape(title)}">', h)
    h = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{url}">', h)
    h = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{url}">', h)
    h = re.sub(r'<meta property="og:type" content=".*?">', f'<meta property="og:type" content="{tur}">', h)
    return h


def son_hazirla(graf):
    blok = '<script type="application/ld+json">\n' + json.dumps(
        {"@context": "https://schema.org", "@graph": graf}, ensure_ascii=False, indent=2) + "\n</script>"
    return re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _: blok, son, count=1, flags=re.S)


YAZAR = {"@type": "Person", "@id": f"{SITE}/#kisi", "name": "Emin Soydan", "jobTitle": "Psikolog", "url": f"{SITE}/"}
mevcut = {k["slug"]: k for k in KONULAR}

LOKASYON = """
      <h2 id="nerede">Nerede görüşüyoruz?</h2>
      <p>
        Yüz yüze görüşmeler <a href="/psikolog-macka-nisantasi-besiktas">Nişantaşı'nda</a>,
        Osmanbey (M2) metrosuna yürüme mesafesindeki görüşme odasında yapılıyor.
        Anadolu yakasındaysanız <a href="/psikolog-kadikoy-suadiye">Kadıköy / Suadiye</a>
        ya da <a href="/psikolog-umraniye-cekmekoy-sancaktepe">Ümraniye / Çarşı (M5)</a>
        seçenekleri de var; dilerseniz <a href="/online-terapi">online</a> da
        sürdürebiliriz. Ücretler için <a href="/seans-ucretleri">seans ücretleri</a>
        sayfasına bakabilirsiniz.
      </p>"""

for k in KONULAR:
    url = f"{SITE}/{k['slug']}"
    bolumler = "".join(f"\n      <h2>{b}</h2>{icerik}\n" for b, icerik in k["bolumler"])
    # Henüz yayımlanmamış konu sayfasına giden metin içi bağlantı düz yazıya döner;
    # o sayfa üretildiğinde bağlantı kendiliğinden açılır.
    bolumler = re.sub(r'<a href="/(nisantasi-[a-z0-9-]+)">(.*?)</a>',
                      lambda m: m.group(0) if m.group(1) in mevcut else m.group(2), bolumler)
    sss = "".join(f"""
      <details>
        <summary>{q}</summary>
        <p>{c}</p>
      </details>""" for q, c in k["sss"])
    ilgili = [s for s in k["ilgili"] if s in mevcut and s != k["slug"]]
    ilgili_html = ""
    if ilgili:
        ilgili_html = '\n    <nav class="ilgili" aria-label="İlgili konular">\n      <h2>İlgili konular</h2>\n      <ul>' + "".join(
            f'\n        <li><a href="/{s}">{mevcut[s]["ad"]}</a></li>' for s in ilgili) + \
            '\n        <li><a href="/calisma-alanlari">Tüm çalışma alanları</a></li>\n      </ul>\n    </nav>\n'
    kaynak = "".join(f'\n        <li><a href="{u}" target="_blank" rel="noopener">{html.escape(ad, False)}</a></li>'
                     if u else f'\n        <li>{html.escape(ad, False)}</li>' for ad, u in k["kaynaklar"])
    main = f'''<main id="icerik">
  <div class="wrap narrow">

    <header class="page-head">
      <p class="eyebrow">Çalışma alanları</p>
      <h1>{k['h1']}</h1>
      {cta('Hızlı iletişim')}
      <p class="page-intro">{k['giris']}</p>
      <p class="yazar">Yazan: <a href="/#hakkimda">Psikolog Emin Soydan</a> &middot; Son güncelleme: <time datetime="{guncel(k)}">{tarih_yazi(guncel(k))}</time></p>
    </header>

    <article class="policy">{bolumler}{LOKASYON}
    </article>

    <section id="sss" aria-labelledby="sss-baslik">
      <h2 id="sss-baslik">Sık sorulan sorular</h2>{sss}
    </section>
{ilgili_html}
    <section class="kaynakca" aria-labelledby="kaynak-baslik">
      <h2 id="kaynak-baslik">Kaynaklar</h2>
      <p>Bu sayfadaki genel bilgiler aşağıdaki kaynaklara dayanır. Sayfa bilgilendirme amaçlıdır; tanı ya da kişisel değerlendirme yerine geçmez.</p>
      <ul>{kaynak}
      </ul>
    </section>

    <section class="cta-kapanis" aria-label="İletişim">
      <p>Sorularınız ve uygun görüşme saatleri için:</p>
      {cta('Sayfa sonu iletişim')}
    </section>

    <a class="page-back" href="/calisma-alanlari">&larr; Tüm çalışma alanları</a>
  </div>
</main>'''
    graf = [
        {"@type": "WebPage", "@id": url, "url": url, "name": k["title"], "headline": k["h1"],
         "description": k["desc"], "inLanguage": "tr-TR", "about": {"@type": "Thing", "name": k["ad"]},
         "author": YAZAR, "datePublished": k["yayin"], "dateModified": guncel(k), "isPartOf": {"@id": f"{SITE}/#site"},
         "citation": [u or ad for ad, u in k["kaynaklar"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Çalışma alanları", "item": f"{SITE}/calisma-alanlari"},
            {"@type": "ListItem", "position": 3, "name": k["h1"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": duz(q), "acceptedAnswer": {"@type": "Answer", "text": duz(c)}}
            for q, c in k["sss"]]},
    ]
    (KOK / f"{k['slug']}.html").write_text(bas_hazirla(k["title"], k["desc"], url) + main + son_hazirla(graf), encoding="utf-8")
    print("yazıldı:", k["slug"])

# Merkez sayfa
url = f"{SITE}/calisma-alanlari"
gruplar = ""
for kod, ad in GRUPLAR:
    sayfalar = [k for k in KONULAR if k["grup"] == kod]
    if not sayfalar:
        continue
    gruplar += f'\n      <h2>{ad}</h2>\n      <ul class="konu-liste">' + "".join(
        f'<li><a href="/{k["slug"]}">{k["ad"]}</a></li>' for k in sayfalar) + "</ul>\n"
title = "Çalışma Alanları | Nişantaşı Psikolog Emin Soydan"
desc = "Depresyon, kaygı ve daha fazlası: Nişantaşı, Kadıköy ve Ümraniye'de yüz yüze, ayrıca online yürüttüğüm bireysel psikodinamik terapi çalışma alanları."
main = f'''<main id="icerik">
  <div class="wrap narrow">

    <header class="page-head">
      <p class="eyebrow">Çalışma alanları</p>
      <h1>Çalışma Alanları</h1>
      {cta('Hızlı iletişim')}
      <p class="page-intro">14 yaş ve üzeri gençler ve yetişkinlerle bireysel olarak, psikodinamik bir çerçevede çalışıyorum. Aşağıda, danışanların sıklıkla getirdiği konuları ve bu konulara nasıl yaklaştığımı anlatan sayfaları bulabilirsiniz.</p>

    </header>

    <article class="policy">{gruplar}{LOKASYON}
    </article>

    <section class="cta-kapanis" aria-label="İletişim">
      <p>Sorularınız ve uygun görüşme saatleri için:</p>
      {cta('Sayfa sonu iletişim')}
    </section>

    <a class="page-back" href="/">&larr; Ana sayfaya dön</a>
  </div>
</main>'''
graf = [{"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": f"{SITE}/"},
    {"@type": "ListItem", "position": 2, "name": "Çalışma alanları", "item": url}]}]
(KOK / "calisma-alanlari.html").write_text(bas_hazirla(title, desc, url, "website") + main + son_hazirla(graf), encoding="utf-8")
print("yazıldı: calisma-alanlari")

# Ana sayfadaki tema kartları: yayımlanmış sayfası olan kart tıklanabilir olur
ana = KOK / "index.html"
s = ana.read_text(encoding="utf-8")
bas_i = s.index('<div class="grid-cards">', s.index('id="temalar"'))
son_i = s.index("</section>", bas_i)
bolum = s[bas_i:son_i]
eslesme = {k["tema_karti"]: k["slug"] for k in KONULAR if k.get("tema_karti")}


def kart(m):
    ic = m.group(2)
    baslik = duz(re.search(r"<h3>(.*?)</h3>", ic, re.S).group(1))
    aciklama = re.search(r"<p>(.*?)</p>", ic, re.S).group(1)
    slug = eslesme.get(baslik)
    if not slug:
        return f'<article class="service">\n          <h3>{baslik}</h3>\n          <p>{aciklama}</p>\n        </article>'
    return (f'<article class="service bagli">\n          <h3><a class="kart-bag" href="/{slug}">{baslik}</a></h3>\n'
            f'          <p>{aciklama}</p>\n          <span class="kart-ok" aria-hidden="true">Devamını oku &rarr;</span>\n        </article>')


bolum = re.sub(r'<article class="service( bagli)?">(.*?)</article>', kart, bolum, flags=re.S)
ana.write_text(s[:bas_i] + bolum + s[son_i:], encoding="utf-8")
print("ana sayfa kartları:", ", ".join(f"{k} -> /{v}" for k, v in eslesme.items()))

# Hizmet sayfalarındaki "Hangi konularda çalışıyorum" listesi: maddeler ana sayfa
# kartlarıyla aynı adı taşır, aynı eşleşmeyle bağlanır; karşılığı olmayan düz kalır.
def madde(m):
    ad = duz(m.group(1))
    slug = eslesme.get(ad)
    return f'<li><a href="/{slug}">{ad}</a></li>' if slug else f"<li>{ad}</li>"


for ad in ["psikolog-macka-nisantasi-besiktas", "psikolog-kadikoy-suadiye",
           "psikolog-umraniye-cekmekoy-sancaktepe", "online-terapi"]:
    yol = KOK / f"{ad}.html"
    s = yol.read_text(encoding="utf-8")
    yeni = re.sub(r'(<ul class="konu-liste">)(.*?)(</ul>)',
                  lambda m: m.group(1) + re.sub(r"<li>(.*?)</li>", madde, m.group(2), flags=re.S) + m.group(3),
                  s, flags=re.S)
    if yeni != s:
        yol.write_text(yeni, encoding="utf-8")
print("hizmet sayfası konu listeleri bağlandı")

# Sitemap
sm = KOK / "sitemap.xml"
t = sm.read_text(encoding="utf-8")
for slug, oncelik, tarih in [("calisma-alanlari", "0.7", GUNCELLEME)] + [(k["slug"], "0.7", guncel(k)) for k in KONULAR]:
    loc = f"<loc>{SITE}/{slug}</loc>"
    if loc in t:
        t = re.sub(re.escape(loc) + r"\s*<lastmod>[^<]*", f"{loc}\n    <lastmod>{tarih}", t)
    else:
        t = t.replace("</urlset>", f"  <url>\n    {loc}\n    <lastmod>{tarih}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{oncelik}</priority>\n  </url>\n</urlset>")
sm.write_text(t, encoding="utf-8")
print("sitemap güncellendi")
