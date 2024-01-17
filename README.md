# automatizesanas_kursa_darbs\

### Pārtikas produktu uzturvērtības skaitītājs

Jānis Bečs 231RDB015

## Ievads

Būdams fiziski aktīvs cilvēks, kurš regulāri apmeklē svaru zāli un seko līdzi savam uzturam, es nolēmu sev atvieglot kādu no šiem ikdienas procesiem. Tā arī radās iedeja par pārtikas produktu uzturvērtības skaitītāju.

## Projekta uzdevums

Atvieglot ikdienas procecu, kas saistīts ar pārtikas produktu uzturvērtību (kaloriju, proteīna, ogļhidrātu un tauku) skaitīšanu.

## Programmas lietošanas pamācība

Kad prasīs 'Cik g apēdāt:' jums jāievada TIKAI skaitlis!
Lūdzu rakstiet vispārīgākus produktu nosaukumus, piem., 'vistas cepetis'->'vista', 'piena spēks'->'proteīna piens' un rakstiet tikai vienu produkta nosaukumu uz katru jautājumu. Pārbaudiet vai produkts ir uzrakstīts pareizi.
Kad visi produkti sarakstīti, uz jautājumu 'Ko ēdāt:' ievadiet atbildi 'x'. Tas izbeigs jautājumu jautāšanu un sāks uzturvērtību aprēķinus.
Programma automātiski aprēķinās kopējo kaloriju, tauku, ogļhidrātu, proteīnu daudzumu.
Kopējo uzturvērtību daudzumu izvadīs uz ekrāna un saglabās Excel failā 'results.xlsx'.
Jūs varat startēt programmu neierobežotu reižu skaitu, Excel failā atbilstošās vērtības tiks pieskaitītas atbilstošā datuma rindā.
Vairāku ierakstu gadījumā, programma var apstrādāt datus ilgāku laika posmu.

## Programmas darbība

# 'main.py'

Programma darbība sākas palaižot 'main.py'. Tiek importēti faili 'search_2.py', 'translate.py', 'excel.py'. Katrs no šiem failiem satur funkcijas, kas paredzētas nosaukumam atbilstošās darbības izpildei. 'main.py' sākumā tiek definēti saraksti, kur tiks saglabāti ēdienu latviskie nosaukumi un ēdinu svars gramos, kā arī tiek definēti mainīgie uzturvērtību saglabāšanai -> tiek izvadīts īss programmas darbības apraksts. -> while true cikls, kas paredzēts pārtikas produktu latviskiem nosaukumiem un svaram gramos. -> tiek izsaukta importētā funkcijas, kas nodod un atgriež List kā argumentu(tiek atgriezts List ar pārtikas produktu nosaukumiem angļu valodā) -> for cikls, kur katra cikla sākumā tiek izsaukta 'mekletajs' funkcija no importētā faila 'search_2', kas nodod Lista i elementu kā argumentu un atgriež listu ar atbilstošā pārtikas produkta uzturvērtību'(g uz 100g produkta). -> tiek aprēķināts uzturvērtību daudzums ņemot vērā ievadītu ēdiena daudzumu gramos -> katra cikla beigās tiek izsaukta write_to_file funkcija, kas tika importēta no faila 'excel.py', funkcija paredzēta lai katra pārtikas produkta uzturvērtības ierakstu saglabātu/pieskaitītu atbilstošā datuma rindai. Rezultāti tiek saglabāti results.xlsx failā, gadījumā, ja fails nav izveidots, tas tiek izveidots. Ja atbilstošās dienas rinda ir tukša, tā tiek pievienota, gadījumā ja tā jau eksistē, tad uzturvērtības tiek jau pieskaitītas klāt eksistējošajām vērtībām -> Kad viss sekmīgi izpildīts, tiek izvadīts kopējais uzturvielu daudzums un programmas sekmīgas darbības apstiprinošs teksts.

# 'translate.py'

Fails satur funkciju, kas paredzēta pārtikas produktu nosaukumu pārtulkošanai no latviešu uz angļu valodu. Funkcija 'tulkosana' ņem List(pārtikas produktu nosaukumi latviešu valodā) kā argumentu un atgriež List(pārtikas produktu nosaukumi angļu valodā). Programmas sākumā tiek importētas time un selenium bibliotēkas -> tiek definēta hipersaite mājaslapai, kas tiks izmantota webscreaping -> tiek ielādēta mājaslpa -> piekrīt noteikumiem -> atver valodu izvēles sadaļu -> izvēlas latviešu valodu -> atver otru izvēles sadaļu -> izvēlas angļu valodu -> izmanto for ciklu lai iegūtu pārtikas produktu nosaukumus angļu valodā -> atgriež pārtikas produktu nosaukumus angļu valodā

# 'search_2.py'

Fails satur funkcijas, kas paredzēta pārtikas produktu uzturvērtības iegūšanai. -> Programmas sākumā tiek importēta selenium bibliotēka -> tiek definēta hipersaite mājaslapai, kas tiks izmantota webscreaping ->
'mekletajs' funkcijai tiek nodots viens pārtikas produkta nosaukums angliski -> atrod search lauciņu -> ievada pārtikas produkta nosaukumu -> nospiež search pogu -> izsauc funkciju 'uzturvertiba', kas katram uzturvērtības mainīgajam piešķirs vērtību -> funkcijā 'uzturvertiba' mēģina atrast atbilstošo uzturvērtības vērtību (pārtikas produkta nosaukums un uzturvērtības tips ir ņemts kā arguments) -> sekmīgas atrašanas gadījumā tiek atgriezta uzturvērtība uz 100g produkta (noapaļota ar vienu ciparu aiz komata) / nesekmīgas atrašanas gadījumā tiek vēlreiz izsaukta funkcija 'mekletajs' šoreiz bez pēdējā string elementa (piem. 'apples'->'apple') -> tā rekursīvās funckijas notiek līdz tiek atrastas visas nepieciešamās uzturvērtības -> funkcija 'mekletajs' atgriež Listu ar atbilstošajām uzturvērtībām

# 'search.py'

Šis fails netiek izmantots programmā, jo mājaslapa pēc programmas pabeigšanas sāka strādāt kļūdaini, tāpēc nācās visu pārtaisīt uz citas mājaslapas bāzes, citā failā 'search_2.py'. "search.py" satur visu funkcionalitāti kā 'search_2.py' izņemot rekursīvās funkcijas. Šis fails programmas darbībā netiek pielietots.

# 'excel.py'

Fails satur funkciju, kas paredzēta pārtikas produkta uzturvērtības pieraksīšanai Excel datnē -> Programmas sākumā tiek importēta pandas un datetime bibliotēka -> 'write_to_file' funkcija ņem 4 mainīgos (uzturvērtības) kā argumentus -> tiek izveidots 'results.xlsx' fails, ja tas vēl nav izveidots -> tiek izveidots un saglabāts jauns ieraksts, ja esošajā datumā vēl nav bijis neviens ieraksts -> ja esošajā datumā jau ir veikts ieraksts, tad mainīgo vērtības tiek pieskaitītas jau pie failā esošajām vērtībām un tiek saglabātas.

## Projektā izmantotās mājaslapas

# Projektā tika izmantotas 3 mājaslapasa(pašas programmas izpildei 2):

https://caloriecontrol.org/healthy-weight-tool-kit/food-calorie-calculator/
https://www.livofy.com/fitness-health-calculators/food-calorie-calculator
https://www.google.com/search?q=tulkot%C4%81js&oq=&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIOCAAQRRgnGDkYgAQYigUyBggBEEUYOzIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDINCAUQABiDARixAxiABDINCAYQABiDARixAxiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDI5MDBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8

## Projektā izmantotās bibliotēkas:

selenium
time
pandas
