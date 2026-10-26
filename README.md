# Zent Presenter & Pacer ⏱️

Prezentációkat segítő, kétképernyős intelligens időmérő és súgógép (teleprompter).

## Főbb funkciók

1. **Intelligens léptetés (Clicker / PageDown támogatás):**
   - Egy diához több idézet vagy vázlatpont rendelhető.
   - A `PageDown` / `→` / `Szóköz` gomb az aktuális dián belüli **következő idézetre lép**.
   - Ha az adott dia utolsó idézeténél jársz, a következő gombnyomásra **a következő diára ugrik a kivetítőn**, és elindítja az új szakasz időzítőjét.

2. **Dinamikus tempó és színvisszajelzés:**
   - **Zöld szín:** Amíg a tervezett időn belül vagy, mutatja a hátralévő időt visszaszámlálva.
   - **Piros szín & finom pulzálás:** Ha túllépted a szakaszt, azonnal átvált pirosra és mutatja a túllépés mértékét (`+00:35 túllépés`).
   - **Globális előadás-tempó:** Valós időben jelzi, hogy a teljes tervezett időhöz képest hány perc/másodperc késésben vagy előnyben vagy.

3. **Kétképernyős PDF kivetítő:**
   - A `🖥️ Kivetítő ablak` gomb megnyit egy önálló ablakot, amit áthúzhatsz a projektorra/külső képernyőre és F11-gyel teljes képernyőre tehetsz.
   - Csak a tiszta diák jelennek meg rajta; a jegyzeteid és az időzítő csak a saját monitorodon láthatóak.

4. **Beépített vizuális Forgatókönyv Szerkesztő:**
   - Diák és szakaszok hozzáadása, törlése, mozgatása.
   - Tervezett percek és másodpercek beállítása.
   - Idézetek / mondanivalók hozzáadása, sorrendezése.
   - JSON letöltése / betöltése és nyers JSON szerkesztő.
   - Saját prezentációs PDF csatolása.

---

## Indítás

Egyszerűen kattints duplán a **`start.bat`** fájlra, amely elindítja a helyi szervert és azonnal megnyitja a böngészőt.
*(Vagy közvetlenül nyisd meg az `index.html` fájlt a böngésződben).*

---

## Billentyűparancsok

| Billentyű | Művelet |
|---|---|
| `PageDown` / `→` / `Szóköz` | Következő idézet vagy következő dia |
| `PageUp` / `←` | Előző idézet vagy előző dia |
| `P` | Időmérés szüneteltetése / folytatása |
| `R` | Aktuális szakasz időzítőjének újraindítása |
| `B` | Kivetítő elsötétítése (Blackout) |
| `F11` (vagy dupla kattintás a kivetítőn) | Teljes képernyő a projektoron |
