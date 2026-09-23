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

  /* ---- Yüzen WhatsApp düğmesi ----
     İlk ekranda gizli kalır ki hero'yu kapatmasın; iletişim bölümü ekrana
     geldiğinde de gizlenir, çünkü orada zaten aynı düğme var. */
  var yuzen = document.getElementById('yuzenWa');
  if (yuzen) {
    yuzen.hidden = false;
    yuzen.classList.add('gizli');

    var iletisim = document.getElementById('iletisim');
    var iletisimGorunur = false;

    var tazele = function () {
      var yeterinceKaydi = window.scrollY > window.innerHeight * 0.6;
      yuzen.classList.toggle('gizli', !yeterinceKaydi || iletisimGorunur);
    };

    if (iletisim && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (girisler) {
        iletisimGorunur = girisler[0].isIntersecting;
        tazele();
      }, { rootMargin: '0px 0px -25% 0px' }).observe(iletisim);
    }

    window.addEventListener('scroll', tazele, { passive: true });
    tazele();
  }

  /* ---- Çerez onayı ve Google etiketi ----
     Etiket index.html'de yüklenmez; orada yalnızca izinler "reddedildi"
     olarak tanımlanır. Ziyaretçi kabul edene kadar Google'a hiçbir istek
     gitmez, hiçbir çerez yazılmaz. Kabul gelirse etiket buradan yüklenir. */
  var OLCUM_KIMLIGI = 'G-00PCBRRYYT';
  var ONAY_ANAHTARI = 'cerez-onayi-v1';

  var onayOku = function () {
    try { return localStorage.getItem(ONAY_ANAHTARI); } catch (e) { return null; }
  };
  var onayYaz = function (deger) {
    try { localStorage.setItem(ONAY_ANAHTARI, deger); } catch (e) { /* gizli sekme */ }
  };

  var gtagCagir = function () {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  };

  var etiketYuklendi = false;
  var etiketiYukle = function () {
    if (etiketYuklendi) return;
    etiketYuklendi = true;

    gtagCagir('consent', 'update', {
      ad_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'granted',
      analytics_storage: 'granted'
    });

    var betik = document.createElement('script');
    betik.async = true;
    betik.src = 'https://www.googletagmanager.com/gtag/js?id=' + OLCUM_KIMLIGI;
    document.head.appendChild(betik);

    gtagCagir('js', new Date());
    gtagCagir('config', OLCUM_KIMLIGI);
  };

  // Vazgeçildiğinde daha önce yazılmış Google çerezlerini temizler.
  var cerezleriSil = function () {
    var parcalar = document.cookie ? document.cookie.split(';') : [];
    var alanlar = [location.hostname, '.' + location.hostname];
    var kok = location.hostname.split('.').slice(-2).join('.');
    if (kok !== location.hostname) alanlar.push('.' + kok);

    parcalar.forEach(function (parca) {
      var ad = parca.split('=')[0].trim();
      if (!/^(_ga|_gid|_gat|_gcl)/.test(ad)) return;
      alanlar.forEach(function (alan) {
        document.cookie = ad + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=' + alan;
      });
      document.cookie = ad + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
    });
  };

  var serit = null;

  var seritKapat = function () {
    if (serit) serit.hidden = true;
    document.body.classList.remove('cerez-acik');
  };

  var seritKur = function () {
    if (serit) { serit.hidden = false; document.body.classList.add('cerez-acik'); return; }

    serit = document.createElement('div');
    serit.className = 'cerez-serit';
    serit.id = 'cerezSerit';
    serit.setAttribute('role', 'region');
    serit.setAttribute('aria-label', 'Çerez tercihi');
    serit.innerHTML =
      '<div class="cerez-ic">' +
        '<div>' +
          '<p class="cerez-baslik">Çerezler</p>' +
          '<p class="cerez-metin">Sitenin nasıl kullanıldığını anlamak ve reklam ' +
          'çalışmalarını ölçmek için Google Analytics çerezlerini kullanmak istiyorum. ' +
          'Bunlar siz kabul etmeden çalışmaz; reddetmeniz sitenin hiçbir bölümünü ' +
          'etkilemez. Ayrıntılar <a href="/gizlilik-politikasi">Gizlilik ve Çerez ' +
          'Politikası</a> sayfasında.</p>' +
        '</div>' +
        '<div class="cerez-dugmeler">' +
          '<button type="button" class="btn btn-sm" id="cerezKabul">Kabul ediyorum</button>' +
          '<button type="button" class="btn btn-sm btn-ghost" id="cerezRed">Reddet</button>' +
        '</div>' +
      '</div>';

    document.body.appendChild(serit);
    document.body.classList.add('cerez-acik');

    serit.querySelector('#cerezKabul').addEventListener('click', function () {
      onayYaz('kabul');
      etiketiYukle();
      seritKapat();
    });

    serit.querySelector('#cerezRed').addEventListener('click', function () {
      onayYaz('red');
      cerezleriSil();
      gtagCagir('consent', 'update', {
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied',
        analytics_storage: 'denied'
      });
      seritKapat();
    });
  };

  if (onayOku() === 'kabul') {
    etiketiYukle();
  } else if (onayOku() !== 'red') {
    seritKur();
  }

  /* Alt bilgiye "Çerez tercihleri" düğmesi eklenir. JavaScript çalışmazsa
     düğme hiç görünmez; zaten o durumda verilecek bir karar da yoktur. */
  var altMenu = document.querySelector('.site-footer nav ul');
  if (altMenu) {
    var madde = document.createElement('li');
    var ayarDugmesi = document.createElement('button');
    ayarDugmesi.type = 'button';
    ayarDugmesi.className = 'link-btn';
    ayarDugmesi.textContent = 'Çerez tercihleri';
    ayarDugmesi.addEventListener('click', function () {
      seritKur();
      var kabul = document.getElementById('cerezKabul');
      if (kabul) kabul.focus();
    });
    madde.appendChild(ayarDugmesi);
    altMenu.appendChild(madde);
  }

  /* ---- Dönüşüm olayları ----
     Google Ads'in "dönüşüm" diye sayabileceği tek şey buradan gider:
     ziyaretçinin gerçekten iletişime geçme hareketi. Tek bir olay adı
     (generate_lead) kullanılır, hangi yoldan gelindiği method parametresinde
     durur; Ads tarafında tek bir dönüşüm eylemi tanımlamak bunun için yeter.

     Onay yoksa hiçbir şey gönderilmez. Şart burada bir kere kontrol edilir. */
  var olcumBildir = function (yontem) {
    if (onayOku() !== 'kabul') return;
    gtagCagir('event', 'generate_lead', { method: yontem });
  };

  document.addEventListener('click', function (e) {
    var hedef = e.target;
    if (!hedef || typeof hedef.closest !== 'function') return;

    var bag = hedef.closest('a[href]');
    if (!bag) return;

    var adres = bag.getAttribute('href') || '';
    if (adres.indexOf('https://wa.me/') === 0) olcumBildir('whatsapp');
    else if (adres.indexOf('tel:') === 0) olcumBildir('telefon');
    else if (adres.indexOf('mailto:') === 0) olcumBildir('eposta');
  });

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
    olcumBildir('form');

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
