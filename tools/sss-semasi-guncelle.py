#!/usr/bin/env python3
"""index.html içindeki FAQPage şemasını sayfadaki görünür SSS metninden yeniden üretir.

Google, yapısal veri ile görünen içeriğin uyuşmamasını yaptırım sebebi sayar.
SSS bölümünde bir soru ya da yanıt değiştirildiğinde bu betik çalıştırılmalı:

    python3 tools/sss-semasi-guncelle.py
"""
import html
import io
import json
import re

DOSYA = "index.html"


def duz_metin(parca: str) -> str:
    """HTML parçasını şemaya konacak düz metne çevirir."""
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", parca))).strip()


def main() -> None:
    sayfa = io.open(DOSYA, encoding="utf-8").read()

    bolum = sayfa[sayfa.index('id="sss"'):sayfa.index('id="iletisim"')]
    sorular = [
        {"@type": "Question", "name": duz_metin(soru),
         "acceptedAnswer": {"@type": "Answer", "text": duz_metin(yanit)}}
        for soru, yanit in re.findall(r"<summary>(.*?)</summary>\s*<p>(.*?)</p>", bolum, re.S)
    ]
    if not sorular:
        raise SystemExit("SSS bölümünde soru bulunamadı; şema güncellenmedi.")

    kalip = re.compile(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)', re.S)
    eslesme = kalip.search(sayfa)
    if not eslesme:
        raise SystemExit("JSON-LD bloğu bulunamadı.")

    graf = json.loads(eslesme.group(2))
    for varlik in graf["@graph"]:
        if varlik.get("@type") == "FAQPage":
            varlik["mainEntity"] = sorular
            break
    else:
        raise SystemExit("Grafta FAQPage bulunamadı.")

    yeni = eslesme.group(1) + json.dumps(graf, ensure_ascii=False, indent=2) + eslesme.group(3)
    io.open(DOSYA, "w", encoding="utf-8").write(sayfa[:eslesme.start()] + yeni + sayfa[eslesme.end():])
    print(f"FAQPage şeması güncellendi: {len(sorular)} soru")


if __name__ == "__main__":
    main()
