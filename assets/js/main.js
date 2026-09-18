(function () {
  'use strict';

  var ALICI = 'psikologeminsoydan@gmail.com';

  /* ---- Mobil menü ---- */
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('anaMenu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.querySelector('.sr-only').textContent = open ? 'Menüyü kapat' : 'Menüyü aç';
    });

    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---- İletişim formu ----
     Sunucu yok. mailto bağlantısı, e-posta uygulaması tanımlı olmayan
     cihazlarda sessizce başarısız olduğu için mesaj her durumda sayfada
     gösterilir; ziyaretçi kopyalayıp gönderebilir. */
  var form = document.getElementById('iletisimFormu');
  if (!form) return;

  var not = document.getElementById('formNot');
  var sonuc = document.getElementById('formSonuc');
  var onizleme = document.getElementById('formOnizleme');
  var mailtoBag = document.getElementById('formMailto');
  var kopyalaBtn = document.getElementById('formKopyala');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var zorunlu = [form.ad, form.eposta, form.mesaj];
    var eksik = false;

    zorunlu.forEach(function (alan) {
      var bos = !alan.value.trim();
      alan.classList.toggle('invalid', bos);
      if (bos) eksik = true;
    });

    if (form.eposta.value.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.eposta.value.trim())) {
      form.eposta.classList.add('invalid');
      not.textContent = 'E-posta adresi geçerli görünmüyor.';
      not.classList.add('hata');
      form.eposta.focus();
      return;
    }

    if (eksik) {
      not.textContent = 'Lütfen ad, e-posta ve mesaj alanlarını doldurun.';
      not.classList.add('hata');
      zorunlu.filter(function (a) { return !a.value.trim(); })[0].focus();
      return;
    }

    not.classList.remove('hata');

    var govde = [
      'Ad Soyad: ' + form.ad.value.trim(),
      'E-posta: ' + form.eposta.value.trim(),
      'Görüşme tercihi: ' + form.tercih.value,
      '',
      form.mesaj.value.trim()
    ].join('\n');

    var konu = 'Görüşme talebi — ' + form.ad.value.trim();
    var baglanti = 'mailto:' + ALICI +
      '?subject=' + encodeURIComponent(konu) +
      '&body=' + encodeURIComponent(govde);

    onizleme.textContent = 'Kime: ' + ALICI + '\nKonu: ' + konu + '\n\n' + govde;
    mailtoBag.href = baglanti;
    sonuc.hidden = false;
    not.textContent = 'Mesajınız aşağıda hazır.';
    sonuc.scrollIntoView({ block: 'nearest' });

    window.location.href = baglanti;
  });

  kopyalaBtn.addEventListener('click', function () {
    var metin = onizleme.textContent;
    var bildir = function (ok) {
      kopyalaBtn.textContent = ok ? 'Kopyalandı' : 'Kopyalanamadı';
      setTimeout(function () { kopyalaBtn.textContent = 'Metni kopyala'; }, 2500);
    };

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(metin).then(function () { bildir(true); }, function () { bildir(false); });
      return;
    }

    // Eski tarayıcılar ve güvensiz bağlam için yedek yöntem
    var alan = document.createElement('textarea');
    alan.value = metin;
    alan.setAttribute('readonly', '');
    alan.style.position = 'fixed';
    alan.style.opacity = '0';
    document.body.appendChild(alan);
    alan.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
    document.body.removeChild(alan);
    bildir(ok);
  });
})();
