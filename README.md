# Zent Presenter & Pacer

Kétképernyős, professzionális prezentációs segédprogram és intelligens súgógép (teleprompter) szekció alapú időgazdálkodással és beépített forgatókönyv-szerkesztővel.

A program kifejezetten előadások, tréningek és bemutatók támogatására készült, ahol fontos a tervezett időkeretek pontos betartása, a mondanivaló precíz felépítése és a zökkenőmentes kivetítés.

---

## Főbb jellemzők

### 1. Szekció alapú időgazdálkodás és tempókövetés
* **Hierarchikus felépítés:** Az előadás logikai szekciókra (blokkokra) oszlik, a szekciók diákból, a diák pedig idézetekből és vázlatpontokból állnak.
* **Szekció időkeret:** Minden szekcióhoz külön megadható a tervezett idő (perc és másodperc).
* **Valós idejű színvisszajelzés:**
  * **Zöld kijelzés:** Amíg az adott szekció tervezett idején belül vagy, a stopper visszaszámlálja a hátralévő időt.
  * **Piros pulzálás:** Az időkeret túllépésekor a stopper azonnal pirosra vált, elindul a túllépési idő mérése és finom vizuális pulzálással figyelmeztet.
* **Dia-számláló a szekcióban:** Folyamatosan mutatja, hogy az adott szekcióból még hány dia van hátra (például: `1 / 4 DIA A SZEKCIÓBAN (3 HÁTRA)`).
* **Globális előadás-idő:** Párhuzamosan mutatja a teljes előadásból eltelt időt a teljes tervezett időkerethez képest, valamint az összesített sietést vagy késést.
* **Készenléti indítás:** Az időmérő alapértelmezetten szüneteltetett (Pause) állapotban indul, így a technikai felkészülés közben nem ketyeg feleslegesen az idő.

### 2. Intelligens súgógép (Prompter) és léptetés
* **Dián belüli gondolatok:** Egy diához több idézet, tételmondat vagy vázlatpont is rendelhető.
* **Prezentációs távirányító (Clicker) támogatás:**
  * A `PageDown`, a jobbra nyíl vagy a szóköz lenyomásakor az aktuális dia **következő idézetére lép**.
  * Ha elérted a dia utolsó idézetét, a következő gombnyomás automatikusan **a következő diára ugrik a kivetítőn**, és megnyitja a következő dia első gondolatát.
  * Szekcióváltáskor a szekció időzítője automatikusan frissül az új szekció idejére.
* **Állítható betűméret:** A prompter szövegmérete a fel/le nyilakkal vagy az `A+` / `A-` gombokkal azonnal növelhető vagy csökkenthető. A beállított méretet a böngésző automatikusan megjegyzi.
* **Következő lépés előnézete:** A kártya alján mindig látható a legközelebbi idézet vagy a következő dia címe, így elkerülhető a bizonytalankodás.

### 3. Kétképernyős kivetítő ablak (Projector)
* **Külön ablak a közönségnek:** A `Kivetítő ablak` gombra kattintva egy letisztult ablak nyílik meg, amelyet áthúzhatsz a kivetítőre vagy külső monitorra.
* **Helyi kommunikáció:** A két ablak közvetlenül a böngésző belső csatornáján (BroadcastChannel) keresztül kommunikál, külső szerver vagy internetkapcsolat nélkül.
* **Teljes képernyő gomb:** A kivetítő ablak jobb felső sarkában található `Teljes képernyő` gombbal egyetlen kattintással válthatsz teljes képernyős módra. A vezérlőgomb 3 másodperc egérnyugalom után automatikusan elhalványul.
* **Fekete kép funkció (Blackout):** A `B` billentyűvel vagy a `Fekete kép` gombbal a kivetített kép bármikor azonnal elsötétíthető, és a közönség figyelme az előadóra irányítható.
* **Képernyő ébrentartás:** A böngésző aktívan megakadályozza, hogy a számítógép képernyője lekapcsoljon vagy zároljon az előadás alatt.

### 4. Beépített Forgatókönyv Szerkesztő
* **Vizuális felület:** Nincs szükség kézi kódolásra vagy JSON szerkesztésre.
* **Dia-előnézetek (Thumbnails):** A szerkesztőben minden dia kártyája mellett megjelenik a PDF adott oldalának valós miniatűr előnézete.
* **Közvetlen ugrás:** Az előnézeti képre kattintva az előadói konzol azonnal az adott diára ugrik.
* **Gyors dia-beszúrás:** A diák mellett található `+ Beszúrás (+1)` gomb közvetlenül beszúr egy új diát, és a teljes előadásban automatikusan eggyel eltolja az összes utána lévő dia sorszámát.
* **Sorszámok rendezése (1..N):** Egyetlen kattintással sorban újraszámozza az összes diát 1-től a legutolsóig, ha töröltél vagy átrendeztél oldalakat.
* **Fájlműveletek:**
  * `JSON letöltése` és `JSON betöltése` a forgatókönyv archiválásához és megosztásához.
  * `PDF csatolása` saját prezentáció azonnali helyi betallózásához.
  * `Nyers JSON` nézet a haladó szerkesztéshez vagy vágólapra másoláshoz.
  * Helyi automatikus mentés: minden módosítás automatikusan elmentődik a böngészőben (LocalStorage).

---

## Használat

### A) Használat GitHub Pages-en keresztül (Online)

1. Nyisd meg a böngésződben a közzétett oldalt:  
   `https://gnadori.github.io/zent/`
2. Az alkalmazás automatikusan betölti a repóban lévő prezentációs PDF-et (`AI.pdf` vagy `presentation.pdf`).
3. Kattints a **Kivetítő ablak** gombra, húzd át az új ablakot a kivetítőre vagy második monitorra, majd kattints a **Teljes képernyő** gombra.
4. Az előadói konzolon kattints az **Indítás** gombra vagy nyomd meg a **P** billentyűt, és a távirányítóval vagy a **PageDown** gombbal indíthatod a léptetést.

### B) Használat saját gépen (Offline / Lokális)

1. Töltsd le vagy klónozd a tárolót a számítógépedre.
2. Indítsd el a **`start.bat`** fájlt (dupla kattintással), amely azonnal elindít egy helyi webszervert és megnyitja az oldalt a böngészőben.
3. Másik lehetőségként közvetlenül is megnyitható az `index.html` fájl bármely modern böngészőben.

---

## Prezentációs PDF frissítése

Ha módosítottad vagy kibővítetted a prezentációt:

1. **GitHubon keresztül:**
   * Töltsd fel a frissített fájlt a repó gyökerébe `AI.pdf` néven (felülírva a régit).
   * A közzététel lefutása után a böngészőben nyomj egy gyorsítótár-törlő frissítést (**Ctrl + F5** vagy Mac-en `Cmd + Shift + R`).
2. **Közvetlenül a felületről:**
   * A *Forgatókönyv Szerkesztő* nézetben kattints a **PDF csatolása** gombra, és válaszd ki a gépeden lévő fájlt. A dia-előnézetek azonnal frissülnek.
3. **Új diák beszúrása a forgatókönyvbe:**
   * Ha a prezentáció közepébe új oldalakat illesztettél, a szerkesztőben a megfelelő diánál kattints a **`+ Beszúrás (+1)`** gombra.
   * Így a korábbi jegyzeteid és idézeteid sértetlenek maradnak, az új oldalak pedig azonnal a helyükre kerülnek.

---

## Billentyűparancsok

| Billentyű | Művelet |
|---|---|
| `PageDown` / `→` / `Szóköz` | Következő idézet vagy következő dia |
| `PageUp` / `←` | Előző idézet vagy előző dia |
| `↑` (Felfelé nyíl) | Idézet szövegméretének növelése |
| `↓` (Lefelé nyíl) | Idézet szövegméretének csökkentése |
| `P` | Időzítő indítása vagy szüneteltetése |
| `R` | Aktuális szekció időzítőjének újraindítása |
| `B` | Kivetítő elsötétítése (fekete kép ki/be) |
| `F11` | Teljes képernyő váltása a fókuszban lévő ablakban |

---

## Fájlstruktúra

* `index.html` – Előadói konzol, szekció időzítő, súgógép és Forgatókönyv Szerkesztő.
* `projector.html` – Tiszta kivetítő nézet a közönség számára, teljes képernyő gombbal.
* `AI.pdf` / `presentation.pdf` – Az előadás diaanyaga.
* `sample_presentation.json` – Alapértelmezett minta forgatókönyv-adatok.
* `start.bat` – Kényelmi indítószkript Windows környezethez.
* `assets/` – Helyi PDF.js megjelenítő könyvtár offline működéshez.
