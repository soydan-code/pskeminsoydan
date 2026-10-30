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

K_NIMH_PANIK = ("ABD Ulusal Ruh Sağlığı Enstitüsü (NIMH), Panic Disorder: When Fear Overwhelms",
                "https://www.nimh.nih.gov/health/publications/panic-disorder-when-fear-overwhelms")
K_NIMH_SOSYAL = ("ABD Ulusal Ruh Sağlığı Enstitüsü (NIMH), Social Anxiety Disorder: More Than Just Shyness",
                 "https://www.nimh.nih.gov/health/publications/social-anxiety-disorder-more-than-just-shyness")
K_NIMH_STRES = ("ABD Ulusal Ruh Sağlığı Enstitüsü (NIMH), I'm So Stressed Out! Fact Sheet",
                "https://www.nimh.nih.gov/health/publications/so-stressed-out-fact-sheet")
K_NICE_SOSYAL = ("NICE, Social anxiety disorder: recognition, assessment and treatment (CG159)",
                 "https://www.nice.org.uk/guidance/cg159")
K_NHS_SAGLIK = ("NHS (İngiltere Ulusal Sağlık Servisi), Health anxiety",
                "https://www.nhs.uk/mental-health/conditions/health-anxiety/")
K_WHO_STRES = ("Dünya Sağlık Örgütü (WHO), Stress: soru ve cevaplar",
               "https://www.who.int/news-room/questions-and-answers/item/stress")
K_WHO_ERGEN = ("Dünya Sağlık Örgütü (WHO), Mental health of adolescents bilgi notu",
               "https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health")
K_MILROD = ("Milrod, B. ve ark. (2007). A randomized controlled clinical trial of psychoanalytic psychotherapy for panic disorder. American Journal of Psychiatry, 164(2), 265-272",
            "https://doi.org/10.1176/ajp.2007.164.2.265")
K_LEICH = ("Leichsenring, F. ve ark. (2013). Psychodynamic therapy and cognitive-behavioral therapy in social anxiety disorder. American Journal of Psychiatry, 170(7), 759-767",
           "https://doi.org/10.1176/appi.ajp.2013.12081125")

GRUPLAR = [
    ("duygudurum", "Depresyon ve duygudurum"),
    ("kaygi", "Kaygı ve anksiyete"),
]

ACIL = ('<p class="acil-not"><strong>Kendinize zarar verme ya da yaşamınıza son verme '
        'düşünceleriniz varsa beklemeyin:</strong> 112\'yi arayın ya da en yakın acil '
        'servise başvurun.</p>')

KONULAR = [
 dict(
  slug="nisantasi-depresyon", grup="duygudurum", ad="Depresyon", tema_karti="Depresif duygudurum",
  title="Depresyon Psikoloğu Nişantaşı | Psikolog Emin Soydan",
  desc="Nişantaşı'nda depresyon için yüz yüze ve online psikolojik destek. Belirtiler, depresyonun kaynakları ve psikodinamik psikoterapi sürecine dair bir rehber.",
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
  slug="nisantasi-anksiyete", grup="kaygi", ad="Anksiyete ve kaygı", tema_karti="Kaygı ve panik",
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
 dict(
  slug="nisantasi-panik-atak", grup="kaygi", ad="Panik atak",
  title="Panik Atak ve Panik Bozukluk | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda panik atak ve panik bozukluk için yüz yüze ve online psikolojik destek. Atak anında neler olur, neden tekrarlar ve psikoterapi süreci.",
  h1="Panik Atak ve Panik Bozukluk: Nişantaşı'nda Psikolojik Destek",
  giris="Birden kalbiniz çarpmaya, nefesiniz daralmaya başlar; ölecekmiş ya da aklınızı kaybedecekmiş gibi hissedersiniz. Birkaç dakika sonra geçer ama geride bir korku bırakır: Ya yine olursa? Panik atak yaşayan pek çok insan bu korkuyla hayatını giderek daraltır. Bu daralmayı birlikte genişletmeye çalışıyoruz.",
  bolumler=[
   ("Panik atak nedir?", """
      <p>Panik atak, aniden başlayan ve dakikalar içinde zirveye ulaşan yoğun bir
      korku ya da sıkıntı dalgasıdır. NIMH ve DSM-5-TR'de tarif edildiği biçimiyle
      atağa çoğu zaman şunlardan birkaçı eşlik eder:</p>
      <ul>
        <li>Çarpıntı, kalbin göğüste vurduğunu hissetmek</li>
        <li>Nefes darlığı ya da boğuluyormuş hissi</li>
        <li>Göğüste sıkışma, terleme, titreme</li>
        <li>Baş dönmesi, sersemlik, bayılacakmış gibi olmak</li>
        <li>Uyuşma, karıncalanma, üşüme ya da ateş basması</li>
        <li>Kendine ya da çevreye yabancılaşma hissi</li>
        <li>Kontrolü kaybetme, delirme ya da ölme korkusu</li>
      </ul>
      <p>Tek bir panik atak geçirmek pek çok insanın başına gelebilir. Ataklar
      tekrarladığında ve "bir sonraki" atak korkusu hayatı yönlendirmeye
      başladığında, buna panik bozukluk adı verilir.</p>"""),
   ("Atak geçtikten sonra: Beklenti kaygısı", """
      <p>Panik atağın en yorucu yanı çoğu zaman atağın kendisi değil, ardından
      gelen bekleyiştir. Kişi bedenini sürekli dinlemeye, her çarpıntıda alarm
      vermeye başlar. Atağın yaşandığı yerlerden, toplu taşımadan, kalabalıktan,
      yalnız kalmaktan kaçınmak zamanla bir yaşam biçimine dönüşebilir. Bazen bu
      kaçınma <a href="/nisantasi-agorafobi">agorafobiye</a> uzanır.</p>
      <p>Ataklar gerçekten çok korkutucudur ama kendi başlarına tehlikeli değildir.
      Bunu bilmek önemlidir; yine de bilmek çoğu zaman yetmez. Korkunun neden bu
      kadar güçlü olduğunu anlamak gerekir.</p>"""),
   ("Psikodinamik bakış: Beden neyi söylüyor?", """
      <p>Panik atak çoğu zaman "durduk yere" geliyormuş gibi yaşanır. Oysa
      psikodinamik çalışmada, atakların sıklıkla dile getirilemeyen duygularla,
      özellikle de ayrılık, öfke ya da bağımlı olma korkusuyla ilişkili olduğu
      görülür. Zihnin söyleyemediğini beden bağırarak söyler.</p>
      <p>Panik bozukluk için geliştirilmiş psikodinamik psikoterapiyi inceleyen
      kontrollü bir araştırma, bu yaklaşımın atakları ve kaçınmayı azaltmada etkili
      olabildiğini göstermiştir (Milrod ve ark., 2007). Seanslarda atakların hangi
      dönemlerde, hangi ilişkilerin gölgesinde başladığını birlikte izleriz.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Ataklar tekrar ediyorsa, bir sonraki atak korkusuyla bazı yerlere gitmekten
      vazgeçtiyseniz ya da sürekli bedeninizi kontrol ederek yaşıyorsanız destek
      almak için iyi bir zamandır.</p>
      <p>Göğüs ağrısı, nefes darlığı gibi belirtiler ilk kez ortaya çıktıysa önce
      bir hekim değerlendirmesiyle bedensel nedenlerin dışlanmasını öneririm. Bu,
      hem güvenliğiniz hem de içinizin rahat etmesi için önemlidir.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Panik atak tehlikeli mi, ölebilir miyim?",
    "Panik atak son derece korkutucu olsa da kendi başına hayati tehlike oluşturmaz. Yine de belirtiler ilk kez ortaya çıktıysa bedensel bir neden olmadığından emin olmak için bir hekime görünmek önemlidir."),
   ("Panik atak ne kadar sürer?",
    "Atak genellikle dakikalar içinde zirveye ulaşır ve sonra yavaş yavaş söner. Ardından yorgunluk ve tedirginlik bir süre devam edebilir."),
   ("Panik atak ile panik bozukluk aynı şey mi?",
    "Hayır. Tek bir panik atak birçok insanın başına gelebilir. Panik bozuklukta ataklar tekrarlar ve yeni bir atak korkusu kişinin davranışlarını ve hayatını belirgin biçimde etkiler."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
  ],
  kaynaklar=[K_NIMH_PANIK, K_DSM, K_NICE_ANX, K_MILROD],
  ilgili=["nisantasi-agorafobi", "nisantasi-anksiyete", "nisantasi-saglik-anksiyetesi", "nisantasi-yaygin-anksiyete"],
 ),
 dict(
  slug="nisantasi-sosyal-fobi", grup="kaygi", ad="Sosyal fobi",
  title="Sosyal Fobi ve Sosyal Kaygı | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda sosyal fobi (sosyal kaygı) için yüz yüze ve online psikolojik destek. Başkalarının bakışından duyulan korku, kaçınma ve psikoterapi süreci.",
  h1="Sosyal Fobi (Sosyal Kaygı): Nişantaşı'nda Psikolojik Destek",
  giris="Bir toplantıda söz almak, yeni insanlarla tanışmak ya da bir kafede tek başına oturmak... Kimileri için sıradan olan bu anlar, sizin için günler öncesinden başlayan bir sıkıntıya dönüşebilir. Sosyal kaygı, utangaçlıktan çok daha fazlasıdır ve yalnız taşınmak zorunda değildir.",
  bolumler=[
   ("Sosyal fobi nedir?", """
      <p>Sosyal fobi, diğer adıyla sosyal kaygı, başkalarının gözü önünde olunan
      durumlarda yargılanma, küçük düşme ya da reddedilme korkusunun yoğun ve
      sürekli hâle gelmesidir. NIMH'in tanımladığı biçimiyle bu korku, kişinin
      gündelik yaşamını, işini ve ilişkilerini belirgin biçimde etkiler.</p>
      <p>Kimi insan yalnızca konuşma yapmak ya da sınav gibi performans
      durumlarında zorlanır (bkz. <a href="/nisantasi-performans-anksiyetesi">performans
      anksiyetesi</a>); kimisi ise neredeyse bütün sosyal ortamlarda tetikte
      hisseder.</p>"""),
   ("Nasıl hissettirir?", """
      <ul>
        <li>Bir sosyal durumdan günler önce başlayan endişe</li>
        <li>Kızarma, terleme, titreme, sesin titremesi ve bunların fark edileceği korkusu</li>
        <li>Konuşurken zihnin boşalması</li>
        <li>Sonrasında yaşananları tekrar tekrar zihinde oynatmak, "neden öyle dedim" diye sorgulamak</li>
        <li>Göz teması kurmakta, yemek yerken izlenmekte zorlanmak</li>
        <li>Telefon açmaktan, toplantılardan, davetlerden kaçınmak</li>
      </ul>
      <p>Kaçınma, zamanla fırsatları da daraltır: kabul edilmeyen bir terfi, gidilmeyen
      bir buluşma, söylenmeyen bir fikir. Bu yüzden sosyal kaygı çoğu zaman
      sessizce yalnızlığa ve <a href="/nisantasi-depresyon">çökkünlüğe</a> eşlik eder.</p>"""),
   ("Psikodinamik bakış: Ötekinin bakışı", """
      <p>Sosyal kaygının merkezinde ötekinin bakışı vardır. Psikodinamik çalışmada bu
      bakışın kimin bakışı olduğunu birlikte düşünürüz: Belki eleştirel bir ebeveyn
      sesi, belki çocuklukta yaşanan bir utanç, belki de kişinin kendisine yönelttiği
      acımasız bir yargı. Lacan'ın deyişiyle özne, kendisini ötekinin gözünden
      görmeyi öğrenir; bu göz bazen fazlasıyla sert olabilir.</p>
      <p>Sosyal kaygıda psikodinamik psikoterapiyi inceleyen geniş bir kontrollü
      çalışma, bu yaklaşımın anlamlı kazanımlar sağlayabildiğini göstermiştir
      (Leichsenring ve ark., 2013). Seans odası da bir sosyal ortamdır; orada kaygının
      nasıl yaşandığını "şimdi ve burada" görmek, çalışmanın en değerli
      malzemelerinden biridir.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Sosyal kaygı yüzünden işinizde, okulunuzda ya da ilişkilerinizde geri
      adım atıyorsanız, istediğiniz şeylerden vazgeçiyorsanız ya da kaygıyı
      yatıştırmak için alkole başvuruyorsanız destek almak için iyi bir zamandır.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Utangaçlık ile sosyal fobi arasındaki fark nedir?",
    "Utangaçlık bir mizaç özelliğidir ve çoğu zaman hayatı kısıtlamaz. Sosyal fobide ise yargılanma korkusu yoğun ve süreklidir, kişi önemli durumlardan kaçınır ve bu durum gündelik yaşamı belirgin biçimde etkiler."),
   ("Görüşmelerde konuşmakta zorlanırsam ne olur?",
    "Bu çok anlaşılır bir kaygı. Kendi hızınızda ilerleriz; susmak da, zorlanmak da çalışmanın bir parçasıdır. Seans odasında yargılanmadan konuşabilmek, zamanla başka ortamlara da taşınabilen bir deneyimdir."),
   ("Online görüşme sosyal kaygıda daha kolay olur mu?",
    "Bazı kişiler için başlangıçta daha rahat olabilir. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır; hangi biçimin size uygun olduğuna birlikte karar verebiliriz."),
   ("Sosyal fobi kendiliğinden geçer mi?",
    "Sosyal kaygı çoğu zaman uzun yıllar sürebilir ve kaçınma arttıkça yerleşir. Erken destek almak, hayatın daralmasını önlemeye yardım eder."),
  ],
  kaynaklar=[K_NIMH_SOSYAL, K_NICE_SOSYAL, K_DSM, K_LEICH],
  ilgili=["nisantasi-performans-anksiyetesi", "nisantasi-anksiyete", "nisantasi-agorafobi", "nisantasi-kimlik-ve-kendilik"],
 ),
 dict(
  slug="nisantasi-agorafobi", grup="kaygi", ad="Agorafobi",
  title="Agorafobi | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda agorafobi için yüz yüze ve online psikolojik destek. Kaçışın zor göründüğü yerlerden duyulan korku, kaçınma ve psikoterapi süreci.",
  h1="Agorafobi: Nişantaşı'nda Psikolojik Destek",
  giris="Metroya binmek, kalabalık bir alışveriş merkezinde dolaşmak ya da evden tek başına çıkmak giderek zorlaşıyorsa, dünyanız yavaş yavaş küçülüyor olabilir. Agorafobi, bu daralmanın adıdır. Gelmekte zorlandığınız dönemlerde online görüşmeyle başlamak da mümkün.",
  bolumler=[
   ("Agorafobi nedir?", """
      <p>Agorafobi, yalnızca "açık alan korkusu" değildir. DSM-5-TR'deki tanımıyla,
      kaçmanın zor olabileceği ya da kötü bir şey olduğunda yardım bulunamayacağı
      düşünülen durumlardan duyulan yoğun korkudur. Bu durumlar şunlar olabilir:</p>
      <ul>
        <li>Toplu taşıma araçları: metro, otobüs, vapur, uçak</li>
        <li>Açık alanlar: meydanlar, köprüler, otoparklar</li>
        <li>Kapalı yerler: mağazalar, sinemalar, asansörler</li>
        <li>Sıra beklemek ya da kalabalığın içinde olmak</li>
        <li>Evin dışında tek başına bulunmak</li>
      </ul>
      <p>Agorafobi çoğu zaman <a href="/nisantasi-panik-atak">panik ataklarla</a>
      birlikte gelişir: atağın yaşandığı ya da yaşanabileceği yerlerden kaçınmak
      zamanla geniş bir alana yayılır.</p>"""),
   ("Kaçınmanın daralttığı hayat", """
      <p>Kaçınmak her seferinde rahatlatır; bu yüzden güçlü bir döngü kurar. Önce
      bir güzergâhtan vazgeçilir, sonra bir semtten, sonra yalnız çıkmaktan.
      Kişi "güvenli" bir yakının eşliğine giderek daha fazla ihtiyaç duyabilir.
      Bu durum bağımsızlık hissini zedeler, ilişkilere yük bindirir ve çoğu zaman
      utançla birlikte gizlenir.</p>"""),
   ("Psikodinamik bakış: Güvenli alan ve ayrılık", """
      <p>Psikodinamik bakış, agorafobide sıklıkla ayrılık ve özerklik temalarına
      dikkat eder. "Güvenli" yer ya da kişi, bir tür sığınaktır; ondan uzaklaşmak
      korku uyandırır. Winnicott, sağlıklı gelişimin destekleyici bir ortamdan
      yavaş yavaş uzaklaşabilmekle mümkün olduğunu söyler. Seanslarda, bu
      uzaklaşmanın neden bu kadar tehlikeli hissettirdiğini birlikte anlamaya
      çalışırız.</p>
      <p>Seans odası da zamanla bir "kucaklayıcı çevre" işlevi görebilir: dünyaya
      yeniden açılmak için güvenle dönülen bir yer.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Gitmek istediğiniz yerlere korku yüzünden gidemiyorsanız, evden çıkmak için
      birine ihtiyaç duymaya başladıysanız ya da hayatınızın sınırları giderek
      daralıyorsa destek almak için iyi bir zamandır. Ofise gelmek şu an çok zor
      geliyorsa <a href="/online-terapi">online görüşmeyle</a> başlayabiliriz.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Agorafobi ile panik atak arasındaki ilişki nedir?",
    "Agorafobi sıklıkla panik ataklarla birlikte gelişir: atak geçirme korkusu, kaçmanın zor olduğu yerlerden kaçınmaya yol açar. Ancak agorafobi panik atak olmadan da görülebilir."),
   ("Evden çıkamıyorsam görüşmelere nasıl başlarım?",
    "Online görüşmeyle başlayabiliriz. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır; ilerleyen dönemde yüz yüze görüşmeye geçmeyi birlikte değerlendirebiliriz."),
   ("Biri bana eşlik ederse gelebilir miyim?",
    "Evet. Görüşmeye kadar birinin size eşlik etmesi bir başlangıç olabilir. Seansın kendisi ise sizinle birebir yürütülür."),
   ("Agorafobi geçer mi?",
    "Agorafobi uzun sürebilir ve kaçınma arttıkça yerleşir. Psikoterapi, korkunun anlamını anlamaya ve hayatın sınırlarını yeniden genişletmeye yardım edebilir; ilerleyiş kişiden kişiye değişir."),
  ],
  kaynaklar=[K_DSM, K_NIMH_ANX, K_NICE_ANX, K_SHEDLER],
  ilgili=["nisantasi-panik-atak", "nisantasi-anksiyete", "nisantasi-ozgul-fobiler", "nisantasi-sosyal-fobi"],
 ),
 dict(
  slug="nisantasi-ozgul-fobiler", grup="kaygi", ad="Özgül fobiler",
  title="Özgül Fobiler | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda özgül fobiler için yüz yüze ve online psikolojik destek. Yükseklik, uçak, hayvan, iğne gibi belirli korkular ve psikoterapi süreci.",
  h1="Özgül Fobiler: Nişantaşı'nda Psikolojik Destek",
  giris="Uçağa binmek, asansöre girmek, bir köpeğin yanından geçmek ya da kan aldırmak... Bir şeyin gerçek tehlikesiyle orantısız, ama kontrol edilemeyen bir korkusu varsa, bu korku hayatınızda düşündüğünüzden fazla yer kaplıyor olabilir.",
  bolumler=[
   ("Özgül fobi nedir?", """
      <p>Özgül fobi, belirli bir nesne ya da duruma karşı duyulan yoğun ve sürekli bir
      korkudur. DSM-5-TR bu korkuları birkaç grupta toplar:</p>
      <ul>
        <li><strong>Hayvanlar:</strong> köpek, kedi, böcek, örümcek, yılan</li>
        <li><strong>Doğal çevre:</strong> yükseklik, su, fırtına, karanlık</li>
        <li><strong>Kan, iğne ve yaralanma:</strong> kan görmek, iğne, tıbbi işlemler</li>
        <li><strong>Durumsal:</strong> uçak, asansör, tünel, köprü, kapalı alanlar</li>
        <li><strong>Diğer:</strong> boğulma, kusma, yüksek sesler gibi</li>
      </ul>
      <p>Kişi çoğu zaman korkusunun abartılı olduğunu bilir; ama bilmek korkuyu
      durdurmaz. Bu, utanca ve kendini suçlamaya yol açabilir.</p>"""),
   ("Fobi hayatı nasıl etkiler?", """
      <p>Bazı fobiler gündelik yaşamı pek etkilemez; kimse her gün yılanla
      karşılaşmaz. Ama bazıları önemli kararları belirler: uçak korkusu yüzünden
      kaçırılan bir iş fırsatı, iğne korkusu yüzünden ertelenen sağlık kontrolleri,
      asansör korkusu yüzünden reddedilen bir ev. Kan ve iğne fobisinde bayılma da
      görülebilir; bu yüzden tıbbi işlemlerden kaçınmak sağlığı doğrudan
      etkileyebilir.</p>"""),
   ("Psikodinamik bakış: Korkunun yer değiştirmesi", """
      <p>Psikanalitik düşüncede fobi, çoğu zaman başka bir yerden gelen kaygının
      belirli bir nesneye yerleşmesi olarak düşünülür. Adı konamayan, her yere
      yayılabilecek bir korku, belirli bir nesneye bağlanınca kaçınılabilir hâle
      gelir. Bu bir tür çözümdür, ama bedeli ağırdır.</p>
      <p>Seanslarda fobiyle doğrudan çalışırken, korkunun ne zaman başladığına,
      hangi dönemlerde yoğunlaştığına ve hayatınızdaki başka kaygılarla nasıl
      ilişkilendiğine de bakarız. Bazı fobilerde maruz kalmaya dayalı yöntemler çok
      etkilidir; gerekli gördüğümde bu konuda sizi yönlendirebilirim.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Korkunuz önemli kararlarınızı etkiliyorsa, sağlığınızla ilgili işlemleri
      ertelemenize yol açıyorsa ya da korkuyla karşılaşma ihtimali bile günlerinizi
      gölgeliyorsa destek almak için iyi bir zamandır.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Fobi ile normal korku arasındaki fark nedir?",
    "Korku gerçek bir tehlikeye verilen doğal bir tepkidir. Fobide korku, durumun gerçek tehlikesiyle orantısızdır, uzun süre devam eder ve kişi bu durumdan belirgin biçimde kaçınır."),
   ("Fobilerde hangi yaklaşımlar kullanılır?",
    "Özgül fobilerde maruz kalmaya dayalı yöntemler sık kullanılır ve etkilidir. Psikodinamik çalışma ise korkunun hayatınızdaki anlamını ve başka kaygılarla bağını anlamaya yardım eder. Hangi yolun size uygun olduğunu ilk görüşmelerde birlikte değerlendiririz."),
   ("İğne ve kan korkusu neden bayılmaya yol açar?",
    "Kan ve iğne fobisinde, diğer fobilerden farklı olarak, korkunun ardından ani bir tansiyon düşmesi görülebilir; bu da bayılmaya yol açabilir. Tıbbi işlemlerden önce bu durumu sağlık ekibine söylemek önemlidir."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
  ],
  kaynaklar=[K_DSM, K_NIMH_ANX, K_WHO_ANX, K_SHEDLER],
  ilgili=["nisantasi-agorafobi", "nisantasi-panik-atak", "nisantasi-saglik-anksiyetesi", "nisantasi-anksiyete"],
 ),
 dict(
  slug="nisantasi-saglik-anksiyetesi", grup="kaygi", ad="Sağlık anksiyetesi",
  title="Sağlık Anksiyetesi (Hastalık Kaygısı) | Nişantaşı Psikolog",
  desc="Nişantaşı'nda sağlık anksiyetesi için yüz yüze ve online psikolojik destek. Ciddi bir hastalığa yakalanma korkusu, sürekli kontrol ve psikoterapi süreci.",
  h1="Sağlık Anksiyetesi: Nişantaşı'nda Psikolojik Destek",
  giris="Küçük bir ağrı, bir ben, geçmeyen bir öksürük... ve zihin hemen en kötü ihtimale gider. İnternette saatlerce belirti araştırmak, tahlil sonuçları temiz çıksa bile rahatlayamamak çok yorucudur. Sağlık anksiyetesi gerçek bir sıkıntıdır ve ciddiye alınmayı hak eder.",
  bolumler=[
   ("Sağlık anksiyetesi nedir?", """
      <p>Sağlık anksiyetesi, ciddi bir hastalığa sahip olma ya da yakalanma
      korkusunun zihni sürekli meşgul etmesidir. DSM-5-TR'de "hastalık kaygısı"
      başlığı altında ele alınır. NHS'in tarif ettiği gibi kişi:</p>
      <ul>
        <li>Bedenindeki küçük değişimleri sürekli kontrol eder</li>
        <li>İnternette belirti araştırmaktan kendini alıkoyamaz</li>
        <li>Sık sık doktora gider ya da tam tersine doktordan tamamen kaçınır</li>
        <li>Yakınlarından tekrar tekrar güvence ister</li>
        <li>Sağlıkla ilgili haberlerden, dizilerden, konuşmalardan etkilenir</li>
        <li>Temiz çıkan sonuçlara rağmen kısa sürede yeniden endişelenir</li>
      </ul>
      <p>Bu kişiler çoğu zaman "hastalık hastası" diye küçümsenir. Oysa yaşanan
      kaygı gerçektir ve son derece yıpratıcıdır.</p>"""),
   ("Kontrol ve güvence döngüsü", """
      <p>Belirti araştırmak ya da doktora gitmek kısa süreliğine rahatlatır. Ama
      bu rahatlama kalıcı olmaz; bir sonraki belirtiyle kaygı yeniden yükselir ve
      kontrol ihtiyacı artar. Zamanla beden, bir tehdit kaynağı gibi izlenmeye
      başlar. Kaygının kendisi de çarpıntı, mide sıkışması gibi bedensel belirtiler
      yarattığı için döngü kendini besler.</p>"""),
   ("Psikodinamik bakış: Beden ve ölüm korkusu", """
      <p>Sağlık kaygısı çoğu zaman yalnızca bedenle ilgili değildir. Bir yakının
      hastalığı ya da kaybı, çocuklukta hastalıkla ilgili yaşantılar, kontrol
      edilemeyen şeylere tahammül etmekte zorlanmak ya da dile getirilemeyen bir
      ölüm korkusu bu kaygıyı besleyebilir. Psikodinamik çalışmada, endişenin
      neden tam da bu dönemde ve bu biçimde ortaya çıktığını birlikte anlamaya
      çalışırız.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Sağlıkla ilgili endişeler gününüzün önemli bir kısmını alıyorsa, iş ve
      ilişkilerinizi etkiliyorsa ya da doktor ziyaretleri ve tahliller kaygınızı
      kalıcı olarak yatıştırmıyorsa destek almak için iyi bir zamandır.</p>
      <p>Psikolojik destek, tıbbi değerlendirmenin yerine geçmez. Yeni ya da
      değişen belirtiler için hekiminize başvurmayı sürdürmeniz önemlidir.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Sağlık anksiyetesi gerçek bir sorun mu, yoksa abartıyor muyum?",
    "Sağlık anksiyetesi gerçek ve yıpratıcı bir kaygı biçimidir. Abartmak ya da hayal etmek değildir; zihnin tehdidi algılama biçimiyle ilgilidir ve üzerinde çalışılabilir."),
   ("İnternette belirti araştırmayı nasıl bırakabilirim?",
    "Araştırmak kısa süre rahatlatsa da çoğu zaman kaygıyı artırır. Psikoterapide bu ihtiyacın ardındaki duyguyu anlamak, kontrol davranışlarının zamanla azalmasına yardım eder."),
   ("Doktora gitmeyi bırakmalı mıyım?",
    "Hayır. Psikolojik destek tıbbi değerlendirmenin yerine geçmez. Amaç doktordan kaçınmak değil, sağlıkla daha dengeli bir ilişki kurabilmektir."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
  ],
  kaynaklar=[K_NHS_SAGLIK, K_DSM, K_NIMH_ANX, K_SHEDLER],
  ilgili=["nisantasi-yaygin-anksiyete", "nisantasi-panik-atak", "nisantasi-anksiyete", "nisantasi-ozgul-fobiler"],
 ),
 dict(
  slug="nisantasi-sinav-kaygisi", grup="kaygi", ad="Sınav kaygısı",
  title="Sınav Kaygısı | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda 14 yaş ve üzeri gençler ve yetişkinler için sınav kaygısında yüz yüze ve online psikolojik destek. Belirtiler, nedenler ve süreç.",
  h1="Sınav Kaygısı: Nişantaşı'nda Psikolojik Destek",
  giris="Haftalarca çalışıp sınav anında her şeyin silindiğini hissetmek, gece uyuyamamak, sonuç ne olursa olsun kendini yetersiz görmek... Sınav kaygısı yalnızca öğrencilerin değil, meslek sınavlarına hazırlanan yetişkinlerin de sık yaşadığı bir sıkıntıdır.",
  bolumler=[
   ("Sınav kaygısı nasıl hissettirir?", """
      <p>Sınavdan önce biraz gerginlik hissetmek doğaldır ve dikkati toplamaya bile
      yardım eder. Sınav kaygısında ise gerginlik performansı engelleyecek kadar
      yoğunlaşır:</p>
      <ul>
        <li>Sınav öncesinde uykusuzluk, iştahsızlık, mide bulantısı</li>
        <li>Sınav anında zihnin boşalması, bilinen soruları hatırlayamamak</li>
        <li>Çarpıntı, terleme, ellerin titremesi</li>
        <li>"Başaramayacağım", "herkes benden iyi" gibi düşünceler</li>
        <li>Çalışmayı ertelemek ya da tersine durmaksızın çalışıp tükenmek</li>
      </ul>"""),
   ("Sınavın ardındaki beklentiler", """
      <p>Sınav kaygısı çoğu zaman sınavın kendisinden çok, ona yüklenen anlamla
      ilgilidir: ailenin beklentileri, gelecekle ilgili büyük kararlar, kendine
      değer biçmenin tek ölçüsü hâline gelen notlar. Dünya Sağlık Örgütü,
      ergenlikteki ruhsal zorlanmalarda akademik baskının önemli bir etken
      olabileceğine dikkat çeker.</p>
      <p>Psikodinamik çalışmada şu sorular önem kazanır: Başarısızlık sizin için ne
      anlama geliyor? Kimin gözünde değer kaybedeceğinizden korkuyorsunuz? Bazen
      sınav, kişinin kendi isteğiyle başkalarının isteği arasında sıkıştığı bir
      sahneye dönüşür.</p>"""),
   ("Gençler ve aileler için", """
      <p>14 yaş ve üzeri gençlerle bireysel olarak çalışıyorum. Görüşmeler gencin
      kendi alanıdır; gizlilik çerçevesi ve ailenin sürece nasıl dahil olacağı ilk
      görüşmelerde açıkça konuşulur. Ebeveynler için en değerli destek çoğu zaman
      sonuca değil çabaya ilgi göstermek ve gencin kaygısını küçümsemeden
      dinleyebilmektir.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Kaygı bildiklerinizi sınavda göstermenizi engelliyorsa, uykunuzu ve
      sağlığınızı etkiliyorsa ya da sınav dönemleri hayatınızın geri kalanını
      tamamen gölgeliyorsa destek almak için iyi bir zamandır. Sınav tarihine çok
      az kalmışsa bile konuşmak iyi gelebilir.</p>
      """ + ACIL),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Kaç yaşındaki gençlerle çalışıyorsunuz?",
    "14 yaş ve üzeri gençlerle ve yetişkinlerle bireysel olarak çalışıyorum."),
   ("Sınava az kaldı, şimdi başlamanın anlamı var mı?",
    "Evet. Kısa sürede bile kaygıyı konuşabilmek, onu anlamak ve sınav günü için kendinize karşı daha anlayışlı olabilmek fark yaratabilir. Sınav sonrasında da çalışmayı sürdürebiliriz."),
   ("Ebeveyn olarak görüşmelere katılabilir miyim?",
    "Görüşmeler gençle bireysel olarak yürütülür. Ailenin sürece nasıl dahil olacağı ve gizliliğin sınırları ilk görüşmelerde açıkça konuşulur."),
   ("Meslek sınavlarına hazırlanan yetişkinlerle de çalışıyor musunuz?",
    "Evet. Sınav kaygısı yalnızca öğrencilere özgü değildir; uzmanlık, yeterlilik ya da dil sınavlarına hazırlanan yetişkinlerle de çalışıyorum."),
  ],
  kaynaklar=[K_WHO_ERGEN, K_NIMH_ANX, K_NIMH_STRES, K_SHEDLER],
  ilgili=["nisantasi-performans-anksiyetesi", "nisantasi-gelecek-kaygisi", "nisantasi-ergenlik-donemi", "nisantasi-anksiyete"],
 ),
 dict(
  slug="nisantasi-performans-anksiyetesi", grup="kaygi", ad="Performans anksiyetesi",
  title="Performans Anksiyetesi | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda performans anksiyetesi için yüz yüze ve online psikolojik destek. Sahne, sunum, spor ve iş ortamında değerlendirilme kaygısı ve süreç.",
  h1="Performans Anksiyetesi: Nişantaşı'nda Psikolojik Destek",
  giris="Sunumda sesinizin titremesi, sahneye çıkmadan önce ellerinizin buz kesmesi, önemli bir maçta ya da toplantıda bildiğiniz her şeyin bir anda kaybolması... Performans anksiyetesi, en çok önemsediğiniz anlarda kendinizi gösterememenin acısıdır.",
  bolumler=[
   ("Performans anksiyetesi nedir?", """
      <p>Performans anksiyetesi, başkalarının izlediği ya da değerlendirdiği bir
      durumda iyi yapamama korkusunun yoğunlaşmasıdır. Konuşma yapmak, sahnede
      çalmak ya da söylemek, spor müsabakaları, iş görüşmeleri ve sunumlar en sık
      karşılaşılan durumlardır. DSM-5-TR, korkunun yalnızca bu tür performans
      durumlarıyla sınırlı kaldığı biçimi <a href="/nisantasi-sosyal-fobi">sosyal
      kaygının</a> özel bir türü olarak tanımlar.</p>"""),
   ("Nasıl hissettirir?", """
      <ul>
        <li>Performanstan günler önce başlayan gerginlik</li>
        <li>Çarpıntı, ağız kuruluğu, titreme, sesin değişmesi</li>
        <li>Performans sırasında zihnin boşalması</li>
        <li>Hata yapma korkusuyla aşırı hazırlanmak ya da tam tersine ertelemek</li>
        <li>Sonrasında yalnızca hatalara odaklanmak</li>
        <li>Fırsatları geri çevirmek, görünür olmaktan kaçınmak</li>
      </ul>
      <p>Paradoks şudur: Ne kadar çok önemseniyorsa kaygı da o kadar büyür. Bu
      yüzden performans anksiyetesi çoğu zaman en yetenekli ve en özenli
      insanları zorlar.</p>"""),
   ("Mükemmeliyetçilik ve performans", """
      <p>Performans anksiyetesi çoğu zaman mükemmeliyetçilikle el ele gider. Hata
      yapmamak için aşırı hazırlanmak, küçük bir aksaklığı bütün performansı
      geçersiz kılan bir felaket gibi yaşamak ve başarıyı bile "yeterince iyi
      değildi" diye karşılamak bu döngünün parçalarıdır.</p>
      <p>Mükemmeliyetçilik dışarıdan bir erdem gibi görünür; içeride ise sürekli bir
      sınav hâlidir. Psikoterapide bu iç sesin nereden geldiğini ve onunla nasıl
      daha merhametli bir ilişki kurulabileceğini birlikte düşünürüz.</p>"""),
   ("Psikodinamik bakış: İzlenmek ve değer görmek", """
      <p>Performans anı, bir bakışın altında olmak demektir. Psikodinamik çalışmada
      bu bakışın taşıdığı anlamlara bakarız: Takdir edilme isteği, kusursuz olma
      baskısı, gösterilen her şeyin "gerçek ben" sanılması ya da başarının
      birilerini kaybettireceği korkusu. Bazen sahnedeki donma, içerideki bir
      çatışmanın, hem görünmek hem de saklanmak isteğinin dışavurumudur.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Kaygı işinizde ilerlemenizi, sanatsal ya da sportif gelişiminizi
      engelliyorsa, önemli fırsatları geri çeviriyorsanız ya da kaygıyı
      yatıştırmak için alkol veya ilaca başvuruyorsanız destek almak için iyi bir
      zamandır.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Performans anksiyetesi ile sahne heyecanı aynı şey mi?",
    "Sahne heyecanı çoğu kişinin yaşadığı ve çoğu zaman performansı destekleyen bir gerginliktir. Performans anksiyetesinde ise kaygı performansı engelleyecek kadar yoğundur ve kişi bu durumlardan kaçınmaya başlar."),
   ("Sanatçılar ve sporcularla da çalışıyor musunuz?",
    "Evet. Sahne sanatçıları, müzisyenler, sporcular ve sunum yapan profesyonellerle bireysel olarak çalışıyorum."),
   ("Performans öncesi kullanılan ilaçlar hakkında ne düşünüyorsunuz?",
    "İlaç kullanımı psikiyatri hekiminin değerlendirmesiyle karar verilmesi gereken bir konudur. Psikoterapi, kaygının kaynağını anlamaya odaklanır ve gerekli durumlarda psikiyatristle birlikte yürütülebilir."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
  ],
  kaynaklar=[K_DSM, K_NIMH_SOSYAL, K_NICE_SOSYAL, K_LEICH],
  ilgili=["nisantasi-sosyal-fobi", "nisantasi-sinav-kaygisi", "nisantasi-anksiyete", "nisantasi-kimlik-ve-kendilik"],
 ),
 dict(
  slug="nisantasi-gelecek-kaygisi", grup="kaygi", ad="Gelecek kaygısı",
  title="Gelecek Kaygısı | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda gelecek kaygısı için yüz yüze ve online psikolojik destek. Belirsizlik, karar verememe, ekonomik ve kariyer endişeleri ve psikoterapi süreci.",
  h1="Gelecek Kaygısı: Nişantaşı'nda Psikolojik Destek",
  giris="İşim ne olacak, bu ülkede kalmalı mıyım, doğru kararı mı verdim? Belirsizliğin arttığı dönemlerde gelecek, merak edilen bir ufuk olmaktan çıkıp ağır bir yüke dönüşebilir. Bu yükü konuşmak, onu taşınabilir kılmanın ilk adımıdır.",
  bolumler=[
   ("Gelecek kaygısı nedir?", """
      <p>Gelecek kaygısı bir tanı adı değil, giderek daha çok insanın tanıdığı bir
      deneyimdir: kariyer, ekonomi, ilişkiler, sağlık ya da toplumsal belirsizlik
      hakkında sürekli bir tedirginlik. Bu kaygı belirli bir konuya yerleşip uzun
      süre devam ettiğinde <a href="/nisantasi-yaygin-anksiyete">yaygın
      anksiyeteye</a> benzer bir biçim alabilir.</p>"""),
   ("Nasıl hissettirir?", """
      <ul>
        <li>"Ya olmazsa?" diye başlayan, sonu gelmeyen senaryolar</li>
        <li>Karar verememek ya da verilen kararları sürekli sorgulamak</li>
        <li>Şimdiki anın tadını çıkaramamak</li>
        <li>Başkalarıyla kıyaslanma ve geride kalma hissi</li>
        <li>Plan yapmakta zorlanmak ya da tersine her şeyi kontrol etmeye çalışmak</li>
        <li>Uyku sorunları, yorgunluk, isteksizlik</li>
      </ul>"""),
   ("Toplumsal belirsizlik ve bireysel kaygı", """
      <p>Gelecek kaygısı her zaman yalnızca kişisel değildir. Ekonomik dalgalanmalar,
      hızla değişen iş dünyası ya da toplumsal gerginlikler pek çok insanı aynı anda
      etkiler. Böyle dönemlerde kaygı duymak bir zayıflık değil, gerçeğe verilen
      anlaşılır bir tepkidir.</p>
      <p>Yine de aynı koşullar karşısında herkes aynı yükü taşımaz. Psikoterapide
      dış koşulları değiştirmeye çalışmayız; ama bu koşulların sizde neye
      dokunduğunu, hangi eski korkuları uyandırdığını ve size hangi seçenekleri
      görünmez kıldığını birlikte anlayabiliriz.</p>"""),
   ("Psikodinamik bakış: Belirsizlikle yaşamak", """
      <p>Belirsizliğe tahammül etmek herkes için zordur; ama bazı insanlar için
      neredeyse dayanılmazdır. Psikodinamik çalışmada bu dayanılmazlığın kökenine
      bakarız: Erken dönemde öngörülebilir ve güvenli bir zemin ne kadar vardı?
      Hata yapmak ne kadar affedildi? Geleceğe dair kaygı, bazen geçmişte
      yaşanmış bir güvensizliğin bugüne düşen gölgesidir.</p>
      <p>Bazen de gelecek kaygısı, kişinin kendi isteğini bilememesinden beslenir.
      Ne istediğini duymak için önce başkalarının beklentilerinden ayrışmak
      gerekir; psikoterapi bunun için bir alan açar.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Gelecekle ilgili düşünceler bugününüzü yaşamanızı engelliyorsa, önemli
      kararları uzun süredir erteliyorsanız ya da kaygı uykunuzu ve ilişkilerinizi
      etkiliyorsa destek almak için iyi bir zamandır.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Gelecek kaygısı bir hastalık mı?",
    "Hayır, gelecek kaygısı bir tanı adı değildir. Belirsizliğe verilen anlaşılır bir tepkidir; ancak uzun süre devam edip hayatı kısıtladığında destek almak iyi gelebilir."),
   ("Kararlarımı benim yerime vermenize yardım eder misiniz?",
    "Psikoterapide sizin yerinize karar vermem; ama ne istediğinizi, sizi neyin durdurduğunu ve kararlarınızın sizin için anlamını birlikte düşünürüz. Bu, kararı kendiniz verebilmenizi kolaylaştırır."),
   ("Yurt dışında yaşıyorum, görüşebilir miyiz?",
    "Evet, online görüşebiliriz. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
   ("Kaygıyla verimli çalışmak mümkün mü?",
    "Bir miktar kaygı harekete geçirici olabilir. Sorun, kaygının yönlendirici olmaktan çıkıp felç edici hâle gelmesidir. Psikoterapide bu dengeyi yeniden kurmaya çalışırız."),
  ],
  kaynaklar=[K_NIMH_GAD, K_WHO_ANX, K_NICE_ANX, K_SHEDLER],
  ilgili=["nisantasi-yaygin-anksiyete", "nisantasi-kronik-stres", "nisantasi-sinav-kaygisi", "nisantasi-tukenmislik-sendromu"],
 ),
 dict(
  slug="nisantasi-kronik-stres", grup="kaygi", ad="Kronik stres",
  title="Kronik Stres | Nişantaşı Psikolog Emin Soydan",
  desc="Nişantaşı'nda kronik stres için yüz yüze ve online psikolojik destek. Uzun süren stresin bedende ve zihinde bıraktığı izler ve psikoterapi süreci.",
  h1="Kronik Stres: Nişantaşı'nda Psikolojik Destek",
  giris="Yoğun bir dönemin geçip gideceğini düşünürsünüz; ama aylar geçer, yük hafiflemez. Bir süre sonra stres bir tepki olmaktan çıkar ve yaşamın kendisine dönüşür. Kronik stres sessizce birikir; fark edildiğinde çoğu zaman beden ve ilişkiler çoktan yorulmuştur.",
  bolumler=[
   ("Stres ne zaman kronikleşir?", """
      <p>Dünya Sağlık Örgütü stresi, zorlayıcı durumların yol açtığı bir endişe ya
      da gerginlik hâli olarak tanımlar ve herkesin zaman zaman yaşadığı doğal bir
      tepki olduğunu vurgular. Kısa süreli stres bizi harekete geçirir. Sorun, stres
      kaynağı uzun süre devam ettiğinde ya da bedenin alarm sistemi kapanmayı
      unuttuğunda ortaya çıkar. NIMH, uzun süren stresin bedensel ve ruhsal sağlık
      üzerinde birikici etkileri olabileceğine dikkat çeker.</p>
      <p>Uzun süreli iş yükü, bakım verme sorumluluğu, ekonomik zorluk, sağlıksız
      bir ilişki ya da birbirini izleyen kayıplar kronik stresin sık görülen
      kaynaklarıdır.</p>"""),
   ("Bedende ve zihinde izleri", """
      <ul>
        <li>Sürekli yorgunluk, dinlenince de geçmeyen bitkinlik</li>
        <li>Baş ağrıları, kas gerginliği, sindirim sorunları</li>
        <li>Uykuya dalamamak ya da sık uyanmak</li>
        <li>Unutkanlık, dikkati toplayamamak</li>
        <li>Tahammülsüzlük, çabuk öfkelenmek</li>
        <li>Keyif alınan şeylerden uzaklaşmak, sosyal çekilme</li>
        <li>Kafein, alkol, yemek ya da ekranla gevşemeye çalışmak</li>
      </ul>
      <p>Bu belirtiler zamanla <a href="/nisantasi-tukenmislik-sendromu">tükenmişliğe</a>,
      kaygıya ya da <a href="/nisantasi-depresyon">depresyona</a> zemin
      hazırlayabilir.</p>"""),
   ("Psikodinamik bakış: Durmanın neden zor olduğu", """
      <p>Kronik stres çoğu zaman yalnızca dış koşullarla açıklanamaz. Bazı insanlar
      için durmak, hayır demek ya da yardım istemek neredeyse imkânsızdır. Sürekli
      güçlü, yetişen, taşıyan biri olmak, belki de uzun zaman önce öğrenilmiş bir
      hayatta kalma biçimidir. Psikodinamik çalışmada bu biçimin nereden geldiğini ve
      bugün size neye mal olduğunu birlikte anlamaya çalışırız.</p>"""),
   ("Ne zaman destek almalı?", """
      <p>Stres aylardır süreğen hâle geldiyse, bedeniniz sinyal vermeye başladıysa,
      ilişkileriniz yıpranıyorsa ya da dinlenmeye vakit bulsanız bile
      dinlenemiyorsanız destek almak için iyi bir zamandır. Bedensel belirtiler için
      hekiminize de başvurmanızı öneririm.</p>"""),
   ("Psikoterapide süreç nasıl ilerler?", """
      <p>İlk görüşmelerde sizi buraya getiren şeyi, bu deneyimin ne zaman ve nasıl
      başladığını, hayatınızda neleri kısıtladığını konuşuruz. Görüşmeler 50 dakika
      sürer ve genellikle haftada bir yapılır.</p>
      <p>İlaç gerekip gerekmediği psikiyatri hekiminin değerlendirmesiyle
      belirlenir; gerekli gördüğüm durumlarda bir psikiyatriste yönlendirir, süreci
      birlikte yürütürüz.</p>"""),
  ],
  sss=[
   ("Stres ile anksiyete arasındaki fark nedir?",
    "Stres genellikle belirli bir zorlayıcı duruma verilen tepkidir ve durum ortadan kalktığında azalır. Anksiyetede ise kaygı, belirgin bir dış neden olmadan da sürebilir. Uzun süren stres, zamanla anksiyeteye zemin hazırlayabilir."),
   ("Koşullarım değişmeden psikoterapi işe yarar mı?",
    "Bazı koşulları değiştirmek mümkün olmayabilir. Ama koşullarla ilişkinizi, sınırlarınızı ve kendinize nasıl davrandığınızı anlamak stresin yükünü belirgin biçimde değiştirebilir."),
   ("Yoğun çalışıyorum, haftalık görüşmeye vakit ayırabilir miyim?",
    "Görüşmeler 50 dakika sürer. Ofise gelmek zorsa online görüşme de mümkün. Kendinize ayırdığınız bu zaman, çoğu zaman çalışmanın kendisinin bir parçası olur."),
   ("Online görüşebilir miyiz?",
    "Evet. Online görüşmeler yüz yüze görüşmelerle aynı süre ve sıklıkta yapılır."),
  ],
  kaynaklar=[K_WHO_STRES, K_NIMH_STRES, K_NIMH_ANX, K_SHEDLER],
  ilgili=["nisantasi-tukenmislik-sendromu", "nisantasi-gelecek-kaygisi", "nisantasi-anksiyete", "nisantasi-depresyon"],
 ),
]
