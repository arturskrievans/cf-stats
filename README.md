# cf-stats
Lietojumprogrammatūras automatizēšanas rīki 1. semestra gala projekts.

Projekta uzdevums - atjautības programmēšanas uzdevumu saita "codeforces" datu apkopošana tālākai produktīvai saita izmantošanai.

Codeforces ir populārs "competitive programming" saits, kas satur vairākus tūkstošus atjautības uzdevumus, kurus var atrisināt izmantojot programmēšanas prasmes
savā iecienītākajā valodā. Uzdevumu grūtība ir pavisma dažāda un pielāgojama katra pašreizējām spējām. It īpaši jauniem studentiem, tai skaitā arī man, kuri, iespējams, vēl nejūtas
ļoti pašpārliecināti par savām kodēšanas prasmēs un loģikas izmantošanu kompleksāku problēmu atrisināšanā, šīs platformas izmantošana var būt gana izdevīga.

Saita problēmas satur vairākas datorzinātnē populāri izmantotas tēmas/algoritmus - binary search, hashing, data structures, game theory, dfs, utt.
Projekta ideja ir sekojoša - balstoties uz pagaidu profila reitingu (ja tāds ir) un visneveiksmīgāk, retāk apskatītajām tēmām/algoritmiem, izvirzīt kādu skaitu (piemēram 10) 
random problēmas, kuras spētu pastiprināt lietotāja zināšanas noteiktajās tēmās. Kā arī apkopot visus datus excel, kur lietotājs varēs skatīt savu progresu - kādu algoritmu 
pielietošana tam padodas labāk vai sliktāk. 

Lai gan, protams, visu aprakstīto var sasniegt "manuāli", iet cauri katrai lapai un skaitīt atrisināto problēmu tēmu skaitu, kā arī procentuāli rēķināt veiksmīgi atrisinātās problēmas
var aizņemt diezgan daudz laiku, neminot vēl par random problēmu izvēli, balstoties uz iepriekšējiem datiem. Tādēļ šis projekts tiks veidots izmantojot lietojumprogrammatūras automatizēšanas
kursā iegūtās zināšanas par tēmām kā web scraping un excel datu manipulāciju.

Programmas funkcionalitāte.

Programmai, kas sasniedz visu iepriekš aprakstīto ir sekojoša funkcionalitāte:
1. Nolasīt no codeforces mājaslapas visas iespējamās problēmu tēmas/algoritmus, saglabāt rezultātus pagaidu vārdnīcās.
2. Prasīt lietotājam ievadīt savu saita username un nolasīt viņa profila reitingu. Noteikt reitingam tuvu intervālu (piemēram [800-1200]), balstoties uz kuru
   vēlāk tiks meklētas jaunas problēmas.
3. Iziet cauri visām lietotāja problēmu iesniegumu lapām. No katra iesnieguma saskaitīt tā statusu (veiksmīgi atrisināta problēma vai nē) , kā arī saskaitīt
   konkrēto problēmu tēmu skaitu un saglabāt vārdnīcā.
4. Balstoties uz iepriekšējiem datiem (reitinga diapazonas, algoritma iesneiguma skaita,...) random veidā atrast 10 atbilstošas problēmas, kuras vēl nav atrisinātas
   un spētu pastiprināt lietotaja zināšanas kādā tēmā.
5. Visus datus apkopot excel tabulu veidā. (Var labāk saprast un apskatīt atverot 'user_statistics.xlsx', kur tika izvēlēts random profils ar vidēji daudz atrisinājumiem).

Bilde ar excel formātu:
![user_data](https://github.com/arturskrievans/cf-stats/assets/96594474/5495aec8-1981-4f46-8541-1403544561a9)

Mainot dažus programmas parametrus var arī iegūt plašāku informāciju par konkrēta lietotāja datiem:
![user_data2](https://github.com/arturskrievans/cf-stats/assets/96594474/366b2d74-d4ea-4e0b-9f90-b8590c0df031)

Bibliotēku izvēle.

Lai izpildītu 1.-4. web scraping punktus tika izvēlēta bs4 bibliotēka kopā ar 'requests' bibliotēku.
Selenium vietā tika izvēlēts bs4, jo visi vajadzīgie dati netiek ielādēti dinamiskā veidā - viss projektam vajadzīgais bija pieejams html kodā. Tas vienkāršoja elementu 
atrašanu, kā arī paātrināja pašu programmu.
Navigācija starp saita lapām tika paveikta nolasot 'href' vērtību un ar 'requests', 'bs4' bibliotēku palīdzību ielādējot nākamās lapas html.
Konkrētu elementu atrašana tika paveikta ar 'bs4' bibliotēkas funkcionalitāti 'soup.find(element)'.

!! Tā kā pats codeforces saits mēdz būt diezgan lēns - slow load and response time (it īpašī online olimpiāžu laikā ), pat bs4 izmantošana var aizņemt kādu laiku. It īpaši, ja kāds
profils ir ļoti aktīvs ar vairākiem desmitiem lapu (katra lapa satur 50 linkus ar problēmām, kuras jāapskata) , programmas izpilde vai aizņemt pat dažas min.  !!

Piektā punkta izpildei tika izmantota openpyxl bibliotēka.
Bibliotēka tika izvēlēta, jo tā ļauj vienkārši lasīt, rakstīt, modificēt excel vērtības, kā arī tā tika daudz apskatīta kursa laikā.
Atkarībā no datu masīvu lieluma, konkrētās excel šūnās tabulu veidā tika ierakstīti visi web scraping ceļā iegūtie dati.


Programmatūras izmantošanas metodes.

Programmu var izmantot vienā veidā - ievadot savu lietotājvārdu un apskatot apkopotos rezultātus excel failā.
Programmas mērķauditorija ir codeforces lietotāji, kuri vēlas attīstīt savas problēmu risināšanas, kā arī kodēšanas prasmes.





