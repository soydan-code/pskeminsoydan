"""Konu sayfalarının içeriği. Sayfaları üretmek için:

    python3 tools/konu-sayfalari-uret.py

Kurallar: unvan yalnız "Psikolog"; "tedavi" ve teşhis koyan dil yok;
uydurma istatistik, vaat ya da garanti yok; uzun çizgi (—) kullanılmaz.
Kaynaklar yalnız köklü kurumlar ve hakemli yayınlar.
"""

GUNCELLEME = "2026-10-29"

K_WHO_DEP = ("Dünya Sağlık Örgütü (WHO), Depressive disorder (depression) bilgi notu",
             "https://www.who.int/news-room/fact-sheets/detail/depression")
K_WHO_ANX = ("Dünya Sağlık Örgütü (WHO), Anxiety disorders bilgi notu",
             "https://www.who.int/news-room/fact-sheets/detail/anxiety-disorders")
K_NIMH_DEP = ("ABD Ulusal Ruh Sağlığı Enstitüsü (NIMH), Depression",
              "https://www.nimh.nih.gov/health/topics/depression")
K_NIMH_ANX = ("ABD Ulusal Ruh Sağlığı Enstitüsü (NIMH), Anxiety Disorders",
              "https://www.nimh.nih.gov/health/topics/anxiety-disorders")
K_NIMH_GAD = ("ABD Ulusal Ruh Sağlığı Enstitüsü (NIMH), Generalized Anxiety Disorder",
              "https://www.nimh.nih.gov/health/publications/generalized-anxiety-disorder-gad")
K_NICE_DEP = ("NICE, Depression in adults: treatment and management (NG222)",
              "https://www.nice.org.uk/guidance/ng222")
K_NICE_ANX = ("NICE, Generalised anxiety disorder and panic disorder in adults (CG113)",
              "https://www.nice.org.uk/guidance/cg113")
K_DSM = ("Amerikan Psikiyatri Birliği (APA), DSM-5-TR",
         "https://www.psychiatry.org/psychiatrists/practice/dsm")
K_SHEDLER = ("Shedler, J. (2010). The efficacy of psychodynamic psychotherapy. American Psychologist, 65(2), 98-109",
             "https://doi.org/10.1037/a0018378")

GRUPLAR = [
    ("duygudurum", "Depresyon ve duygudurum"),
    ("kaygi", "Kaygı ve anksiyete"),
]

ACIL = ('<p class="acil-not"><strong>Kendinize zarar verme ya da yaşamınıza son verme '
        'düşünceleriniz varsa beklemeyin:</strong> 112\'yi arayın ya da en yakın acil '
        'servise başvurun.</p>')

KONULAR = [
 dict(
  slug="nisantasi-depresyon", grup="duygudurum", ad="Depresyon",
  title="Depresyon Psikoloğu Nişantaşı | Psikolog Emin Soydan",
  desc="Nişantaşı'nda depresyon için yüz yüze ve online psikolojik destek. Belirtiler, depresyonun kaynakları ve psikodinamik psikoterapi sürecine dair anlaşılır bir rehber.",
  h1="Nişantaşı'nda Depresyon İçin Psikolojik Destek",
  giris="Sabahları yataktan kalkmak bir dağa tırmanmak gibi gelebilir; eskiden sevdiğiniz şeyler rengini yitirmiş olabilir. Depresyon çoğu zaman sessiz yaşanır ve kişi bunu kendi zayıflığı sanır. Nişantaşı'ndaki görüşme odasında bu ağırlığı birlikte anlamaya ve taşımaya alan açıyorum.",
  bolumler=[
   ("Depresyon nasıl hissettirir?", """
      <p>Depresyon yalnızca üzüntü değildir. Dünya Sağlık Örgütü ve ABD Ulusal Ruh
      Sağlığı Enstitüsü gibi kaynaklar, en az iki hafta boyunca günün büyük bölümünde
      süren çökkün bir ruh hâlini ya da ilgi ve zevk kaybını depresyonun temel
      işaretleri arasında sayar. Bunlara çoğu zaman şunlar eşlik eder:</p>
      <ul>
        <li>Uykuda belirgin değişiklik: uyuyamamak ya da çok uyumak</li>
        <li>Enerji düşüklüğü, sürekli yorgun hissetmek</li>
        <li>İştahta ya da kiloda değişim</li>
        <li>Değersizlik ya da yoğun suçluluk duyguları</li>
        <li>Dikkat toplamakta ve karar vermekte zorlanmak</li>
        <li>Geleceğe dair umutsuzluk</li>
        <li>Bazen yaşamın anlamını yitirdiğine dair düşünceler</li>
      </ul>
      <p>Bu işaretlerin hepsi herkeste görülmez. Kimi insan depresyonu daha çok
      bedeninde, kimisi tahammülsüzlük ve öfke olarak yaşar. Ama ortak bir nokta
      vardır: hayat, olması gerekenden çok daha ağır gelir.</p>"""),
   ("Depresyon nereden gelir?", """
      <p>Depresyonun tek bir nedeni yoktur. Biyolojik yatkınlık, yaşam olayları,
      kayıplar, uzun süreli stres ve ilişkilerdeki örüntüler birlikte rol oynar.
      Psikodinamik bakış bu tabloya bir soru daha ekler: Bu çöküntü, kişinin
      hayatında hangi anlamı taşıyor?</p>
      <p>Bazen depresyon yası tutulamamış bir kaybın, bazen dışa söylenemeyen
      öfkenin içe dönmesinin, bazen de uzun süre başkalarının beklentilerine göre
      yaşamanın yorgunluğudur. Winnicott'un "sahte kendilik" dediği, dışarıya karşı
      ayakta tutulan ama içeriden boşalan hâl de çoğu zaman bu ağırlığın bir
      parçasıdır. Bunları anlamak, yükün kendisini hafifletmeye başlar.</p>"""),
   ("Depresyonun pek bilinmeyen yüzleri", """
      <p>Depresyon her zaman ağlamak ya da yataktan çıkamamak biçiminde görünmez.
      Bazı insanlar işlerini yürütmeye, sosyal hayatlarını sürdürmeye devam eder;
      dışarıdan bakan biri hiçbir şey fark etmez. İçeride ise her şey bir
      zorunluluğa dönüşmüştür ve günün sonunda geriye yalnızca tükenmişlik kalır.</p>
      <p>Kimi zaman depresyon bedende konuşur: geçmeyen yorgunluk, baş ve sırt
      ağrıları, hiçbir şeyden tat alamama. Kimi zaman da öfke, alınganlık ve
      tahammülsüzlük olarak belirir, özellikle gençlerde ve erkeklerde bu görünüm
      daha sık fark edilir. Hangi biçimde olursa olsun, yaşadığınız şey "abartı"
      ya da "nankörlük" değildir; anlaşılmayı bekleyen bir ruhsal durumdur.</p>"""),
   ("Yakınınız depresyondaysa", """
      <p>Sevdiğiniz biri depresyondaysa en çok işe yarayan şey, çoğu zaman
      çözüm önermek değil, yanında kalabilmektir. "Biraz çıksan geçer" gibi
      cümleler iyi niyetli olsa da kişiyi daha yalnız bırakabilir. Onu dinlemek,
      destek almasını yargılamadan teşvik etmek ve gerektiğinde ilk görüşmeye
      giden yolu kolaylaştırmak çok değerlidir. Kendi yorgunluğunuzu da ihmal
      etmeyin; bir yakını taşımak da destek gerektirebilir.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Bu duygular iki haftadan uzun sürüyorsa, işinizi, ilişkilerinizi ya da
      gündelik bakımınızı zorlaştırıyorsa destek almak için iyi bir zamandır.
      "Daha kötüsünü yaşayanlar var" diye beklemek, yükü yalnız taşıma süresini
      uzatır.</p>
      """ + ACIL),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmeler bir tanışmadır: sizi buraya getiren şeyi, hayatınızın şimdiki
      hâlini ve geçmişten bugüne uzanan izleri birlikte dinleriz. Görüşmeler 50
      dakika sürer ve genellikle haftada bir yapılır.</p>
      <p>Psikodinamik psikoterapide amaç yalnızca belirtileri azaltmak değil, onları
      besleyen örüntüleri anlamaktır. Bu yaklaşımı inceleyen araştırmalar,
      kazanımların seanslar bittikten sonra da sürme eğiliminde olduğunu gösteriyor
      (Shedler, 2010).</p>
      <p>İngiltere'nin klinik rehber kurumu NICE, depresyonun şiddetine göre
      psikoterapinin tek başına ya da ilaçla birlikte önerilebileceğini belirtir.
      İlaç değerlendirmesi psikiyatri hekiminin alanıdır; gerekli gördüğüm durumlarda
      bir psikiyatriste yönlendirir, süreci birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Depresyon ile üzüntü arasındaki fark nedir?",
    "Üzüntü bir kayba ya da hayal kırıklığına verilen doğal bir tepkidir ve zamanla hafifler. Depresyonda ise çökkünlük ya da ilgi kaybı haftalarca sürer, hayatın pek çok alanına yayılır ve gündelik işleyişi etkiler."),
   ("Depresyon için ilaç kullanmam gerekir mi?",
    "Her depresyon ilaç gerektirmez. İlaç kararı psikiyatri hekiminin değerlendirmesiyle verilir. Psikoterapi tek başına ya da ilaçla birlikte sürdürülebilir; gerekli gördüğümde sizi bir psikiyatriste yönlendiririm."),
   ("Psikoterapi ne kadar sürer?",
    "Süre kişiden kişiye değişir. İlk görüşmelerde birlikte bir çerçeve belirler, düzenli aralıklarla nerede olduğumuzu gözden geçiririz."),
   ("Online görüşme depresyonda işe yarar mı?",
    "Birçok kişi için online görüşme, yüz yüze görüşmeyle aynı süre ve sıklıkta sürdürülebilir. Evden çıkmanın zorlaştığı dönemlerde sürekliliği korumaya da yardım eder."),
  ],
  kaynaklar=[K_WHO_DEP, K_NIMH_DEP, K_NICE_DEP, K_SHEDLER],
  ilgili=["nisantasi-anksiyete", "nisantasi-yas-ve-kayip", "nisantasi-tukenmislik-sendromu", "nisantasi-mevsimsel-depresyon"],
 ),
 dict(
  slug="nisantasi-anksiyete", grup="kaygi", ad="Anksiyete ve kaygı",
  title="Anksiyete ve Kaygı Psikoloğu Nişantaşı | Psikolog Emin Soydan",
  desc="Nişantaşı'nda anksiyete ve kaygı için yüz yüze ve online psikolojik destek. Kaygının bedende ve zihinde nasıl yaşandığı, ne zaman destek alınmalı ve süreç.",
  h1="Nişantaşı'nda Anksiyete ve Kaygı İçin Psikolojik Destek",
  giris="Kalbin hızlandığı, zihnin bir türlü susmadığı, gelmemiş felaketlerin şimdiden yaşandığı anlar... Kaygı herkesin tanıdığı bir duygudur; ama kimi zaman hayatın direksiyonuna geçer. Nişantaşı'ndaki görüşme odasında kaygının size ne anlatmaya çalıştığını birlikte dinliyoruz.",
  bolumler=[
   ("Kaygı ne zaman bir yüke dönüşür?", """
      <p>Kaygı, bizi tehlikeye karşı hazırlayan doğal bir alarm sistemidir. Bir
      sınavdan önce, önemli bir görüşmede ya da belirsizlik karşısında hissedilen
      gerginlik çoğu zaman işe yarar. Sorun, alarm gerçek bir tehlike olmadan sık sık
      çalmaya başladığında ya da tehlike geçtikten sonra susmadığında ortaya çıkar.</p>
      <p>Dünya Sağlık Örgütü ve NIMH gibi kaynaklar anksiyeteyi tek bir tablo olarak
      değil, bir aile olarak ele alır. <a href="/nisantasi-yaygin-anksiyete">Yaygın
      anksiyete</a>, panik atak, sosyal kaygı, agorafobi ve belirli fobiler bu ailenin
      farklı yüzleridir.</p>"""),
   ("Kaygı bedende ve zihinde nasıl yaşanır?", """
      <p>Bedende:</p>
      <ul>
        <li>Çarpıntı, nefesin daraldığı hissi</li>
        <li>Kaslarda gerginlik, baş ağrısı</li>
        <li>Mide bulantısı ya da sindirim şikâyetleri</li>
        <li>Uykuya dalmakta zorlanma</li>
        <li>Huzursuzluk, yerinde duramama</li>
      </ul>
      <p>Zihinde:</p>
      <ul>
        <li>"Ya olursa?" diye başlayan, durmayan düşünceler</li>
        <li>Dikkati toplayamama</li>
        <li>Kötü bir şey olacakmış hissi</li>
        <li>Kaygı uyandıran durumlardan kaçınma</li>
      </ul>
      <p>Kaçınmak kısa vadede rahatlatır ama zamanla dünyayı daraltır. Kaygının en
      çok yorduğu şeylerden biri de budur: yaşanabilecek alan giderek küçülür.</p>"""),
   ("Kaygıyla baş etmeye çalışırken sık kurulan tuzaklar", """
      <p>Kaygıyla yaşayan pek çok insan, onu yatıştırmak için zamanla bazı
      alışkanlıklar geliştirir. Bunlar o an işe yarar ama uzun vadede kaygıyı
      besleyebilir:</p>
      <ul>
        <li><strong>Kaçınmak:</strong> Zorlayan yerlere gitmemek, telefonları açmamak,
        kararları ertelemek.</li>
        <li><strong>Sürekli güvence aramak:</strong> Aynı soruyu yakınlarınıza
        tekrar tekrar sormak, internette belirti araştırmak.</li>
        <li><strong>Her şeyi kontrol etmeye çalışmak:</strong> Planlamak, listeler
        yapmak, beklenmedik hiçbir şeye yer bırakmamak.</li>
        <li><strong>Hissi bastırmak:</strong> Alkol, aşırı çalışma ya da ekran
        başında saatler geçirmek.</li>
      </ul>
      <p>Bunları fark etmek bir başarısızlık itirafı değildir. Aksine, kaygının
      sizinle nasıl bir ilişki kurduğunu görmenin ilk adımıdır. Psikoterapide
      bu döngüyü yargılamadan, birlikte incelemek mümkündür.</p>"""),
   ("Psikodinamik bakış: Kaygı neyi haber veriyor?", """
      <p>Psikodinamik yaklaşımda kaygı, ortadan kaldırılması gereken bir arıza
      olmaktan çok bir habercidir. Çoğu zaman bastırılmış bir isteğe, dile
      getirilemeyen bir öfkeye ya da eski bir kaybın yeniden yaşanma ihtimaline
      işaret eder. Seanslarda belirtilerle birlikte kaygının hangi anlarda, kimlerin
      yanında ve hangi sözcüklerle ortaya çıktığına da bakarız.</p>
      <p>Aramızda kurulan ilişki de bu çalışmanın bir parçasıdır. Kaygınızın seans
      odasında nasıl dolaştığını "şimdi ve burada" birlikte görmek, hayatınızın başka
      alanlarında neler olduğunu anlamaya yardım eder.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Kaygı işinizi, ilişkilerinizi, uykunuzu ya da sevdiğiniz şeyleri
      yapabilmenizi kısıtlıyorsa, bazı yerlere gitmekten ya da bazı insanlarla
      konuşmaktan kaçınmaya başladıysanız, biriyle konuşmak iyi gelebilir.</p>
      <p>Göğüs ağrısı ya da nefes darlığı gibi bedensel belirtiler ilk kez ortaya
      çıktıysa, önce bir hekim değerlendirmesi yaptırmanızı öneririm.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, kaygının ne zaman ve nasıl
      başladığını, hayatınızda neleri etkilediğini konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>NICE rehberleri, anksiyetede psikoterapiyi temel seçeneklerden biri olarak
      sayar. İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğümde bir psikiyatristle birlikte çalışırız.</p>"""),
  ],
  sss=[
   ("Kaygı ile anksiyete aynı şey mi?",
    "Gündelik dilde aynı anlamda kullanılırlar. Anksiyete daha çok kaygının sürekli ve yoğun hâle gelip hayatı kısıtladığı durumlar için kullanılır."),
   ("Kaygı tamamen geçer mi?",
    "Kaygı insan olmanın bir parçasıdır ve tamamen yok olması hedeflenmez. Amaç, kaygının hayatınızı yönetmesi yerine onu anlayabilir ve taşıyabilir hâle gelmenizdir."),
   ("İlk görüşmeye hazırlanmam gerekir mi?",
    "Hazırlanmanız gereken bir şey yok. Aklınıza gelenle başlayabiliriz; nereden başlayacağımızı birlikte buluruz."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır. Dışarı çıkmanın zorlaştığı dönemlerde sürekliliği korumaya da yardım eder."),
  ],
  kaynaklar=[K_WHO_ANX, K_NIMH_ANX, K_NICE_ANX, K_SHEDLER],
  ilgili=["nisantasi-yaygin-anksiyete", "nisantasi-panik-atak", "nisantasi-sosyal-fobi", "nisantasi-depresyon"],
 ),
 dict(
  slug="nisantasi-yaygin-anksiyete", grup="kaygi", ad="Yaygın anksiyete",
  title="Yaygın Anksiyete Bozukluğu | Nişantaşı Psikolog Emin Soydan",
  desc="Yaygın anksiyete bozukluğu için Nişantaşı'nda yüz yüze ve online psikolojik destek. Sürekli endişenin işaretleri, ardındaki dinamikler ve psikoterapi süreci.",
  h1="Yaygın Anksiyete Bozukluğu: Nişantaşı'nda Psikolojik Destek",
  giris="Her şey yolundayken bile içinizde bir şeylerin ters gideceğine dair bir his varsa, zihniniz bir endişeden ötekine atlıyor ve bir türlü dinlenemiyorsa yalnız değilsiniz. Bu sürekli tetikte olma hâline yaygın anksiyete adı verilir.",
  bolumler=[
   ("Yaygın anksiyete nedir?", """
      <p>Yaygın anksiyete bozukluğu; iş, sağlık, aile ya da para gibi gündelik
      konular hakkında, kontrol edilmesi zor ve aşırı bir endişenin uzun süre, çoğu
      gün devam etmesiyle tanımlanır. Tanı ölçütlerinde bu süre en az altı ay olarak
      belirtilir (APA, DSM-5-TR).</p>
      <p>Endişe belirli bir şeye bağlı değildir. Bir konu çözüldüğünde yerini hemen
      bir başkası alır. Bu yüzden yaygın anksiyete, <a href="/nisantasi-anksiyete">kaygı
      ailesinin</a> en "sessiz" ama en yorucu üyelerinden biridir.</p>"""),
   ("Nasıl hissettirir?", """
      <ul>
        <li>Huzursuzluk, gerginlik ya da "diken üstünde" olma hâli</li>
        <li>Çabuk yorulma</li>
        <li>Dikkati toplayamama, zihnin aniden boşalması</li>
        <li>Tahammülsüzlük, çabuk sinirlenme</li>
        <li>Kaslarda gerginlik</li>
        <li>Uykuya dalmakta ya da uykuyu sürdürmekte zorlanma</li>
        <li>Küçük kararları bile ertelemek, sürekli güvence aramak</li>
      </ul>
      <p>Pek çok insan bu hâli yıllarca "ben zaten endişeli biriyim" diyerek
      kişiliğinin bir parçası sayar. Oysa sürekli endişe kişiliğin kendisi değil,
      zamanla yerleşmiş bir işleyiş biçimidir ve üzerinde çalışılabilir.</p>"""),
   ("Endişeyle yaşamanın görünmeyen bedeli", """
      <p>Yaygın anksiyete çoğu zaman dışarıdan fark edilmez. Kişi işine gider,
      sorumluluklarını yerine getirir, hatta çevresindekilere "her şeyi düşünen,
      tedbirli biri" olarak görünür. Bedeli ise içeride ödenir: dinlenemeyen bir
      zihin, gevşeyemeyen bir beden, tatillerde bile kapanmayan bir alarm.</p>
      <p>Zamanla bu hâl ilişkilere de yansır. Sürekli güvence istemek yakınları
      yorabilir; her olasılığı önceden düşünmek, anın tadını çıkarmayı
      zorlaştırır. Bazen de uzun süren endişenin ardından bir çöküntü, bir
      <a href="/nisantasi-depresyon">depresif dönem</a> gelir. Bu yüzden yaygın
      anksiyeteyi "idare edilebilir bir huy" olarak görmek yerine, ciddiye alınmayı
      hak eden bir yük olarak görmek önemlidir.</p>"""),
   ("Endişenin ardında ne olabilir?", """
      <p>Psikodinamik bakış, sürekli endişeyi çoğu zaman bir korunma çabası olarak
      görür. Zihin, olası her felaketi önceden düşünerek kontrol duygusunu korumaya
      çalışır. Bu, daha derindeki bir korkuyla, belki çaresizlikle, terk edilmeyle
      ya da kendi isteklerinin sonuçlarıyla yüzleşmekten kaçınmanın bir yolu
      olabilir.</p>
      <p>Erken dönemde güvenli ve öngörülebilir bir ortamın eksik kaldığı durumlarda,
      dünyayı sürekli denetlemek bir hayatta kalma biçimine dönüşebilir. Seanslarda
      bu örüntünün nereden geldiğini ve bugün size neye mal olduğunu birlikte
      anlamaya çalışırız.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Endişe aylardır süren bir arka plan gürültüsüne dönüştüyse, uykunuzu, işinizi
      ya da ilişkilerinizi etkiliyorsa, ya da sürekli birilerinden "merak etme, bir
      şey olmaz" duymaya ihtiyaç duyuyorsanız destek almak için iyi bir zamandır.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde endişelerinizin içeriğini, ne zaman yoğunlaştığını ve
      hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika sürer ve
      genellikle haftada bir yapılır.</p>
      <p>NICE rehberleri yaygın anksiyetede psikoterapiyi temel seçeneklerden biri
      olarak önerir; ilaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir. Gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Yaygın anksiyete ile normal endişe arasındaki fark nedir?",
    "Herkes zaman zaman endişelenir. Yaygın anksiyetede endişe aşırıdır, kontrol edilmesi zordur, birçok konuya yayılır ve uzun süre devam ederek gündelik yaşamı belirgin biçimde etkiler."),
   ("Bu hâl kişiliğimin bir parçası değil mi?",
    "Uzun süredir yaşandığı için öyle hissettirebilir. Ama sürekli endişe zamanla yerleşmiş bir işleyiş biçimidir ve psikoterapide üzerinde çalışılabilir."),
   ("İlaç kullanmam gerekir mi?",
    "Her durumda gerekmez. İlaç kararı psikiyatri hekiminin değerlendirmesiyle verilir; gerekli gördüğümde sizi bir psikiyatriste yönlendiririm."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
  ],
  kaynaklar=[K_NIMH_GAD, K_DSM, K_NICE_ANX, K_SHEDLER],
  ilgili=["nisantasi-anksiyete", "nisantasi-panik-atak", "nisantasi-saglik-anksiyetesi", "nisantasi-gelecek-kaygisi"],
 ),
]
