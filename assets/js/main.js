(function () {
  'use strict';

  // Mobil menü
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('anaMenu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // İletişim formu: sunucu olmadığı için mesajı e-posta uygulamasında açar.
  var ALICI = 'psikologeminsoydan@gmail.com';
  var form = document.getElementById('iletisimFormu');
  var not = document.getElementById('formNot');

  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var ad = form.ad.value.trim();
    var eposta = form.eposta.value.trim();
    var mesaj = form.mesaj.value.trim();

    [form.ad, form.eposta, form.mesaj].forEach(function (alan) {
      alan.classList.toggle('invalid', !alan.value.trim());
    });

    if (!ad || !eposta || !mesaj) {
      not.textContent = 'Lütfen ad, e-posta ve mesaj alanlarını doldurun.';
      return;
    }

    var govde = [
      'Ad Soyad: ' + ad,
      'E-posta: ' + eposta,
      'Görüşme tercihi: ' + form.tercih.value,
      '',
      mesaj
    ].join('\n');

    window.location.href =
      'mailto:' + ALICI +
      '?subject=' + encodeURIComponent('Randevu talebi — ' + ad) +
      '&body=' + encodeURIComponent(govde);

    not.textContent = 'E-posta uygulamanız açılıyor. Açılmazsa doğrudan ' + ALICI + ' adresine yazabilirsiniz.';
  });
})();
