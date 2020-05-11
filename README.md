# [Läs loggboken](https://github.com/abbindustrigymnasium/driverbot-abbwiljoh/blob/master/loggbok.md "Loggbok Bil/Programmering")
---
## Python-Projekt, William Johansson 2020

### Installering
``` python
pip install matplotlib
```
### Program: Valsimulator
Mitt projekt är en valsimulator som använder slumpade värden för att simulera en valsituation och skriva ut resultat. Varje parti har en förutspådd vidd där antalet röster varierar, vilket innebär att de slumpade värdena inte är helt random, utan har en viss struktur. Politikerna från de olika partierna gör uttalanden beroende på resultat, och det finns en chans att någon av partiledarna gör eller säger något knasigt som skulle påverka resultatet. När alla resultat räknats finns ett alternativ att få en visuell representation i form av ett stapeldiagram där de accepterade partierna (>4%) och deras resutat visas.

![alt_text](https://raw.githubusercontent.com/abbindustrigymnasium/programmering-1-miniprojekt-abbwiljoh/master/bilder/Val_TerminalBild.jpg "Terminalen från Val.py")

### Grundläggande om kod
Programmet bygger på en dictionary där alla partier och relevant information finns och ett värde, position, som säger i vilken ordning partierna och deras resultat ska behandlas. Denna position anknyter till den lista som skapas när alla röster räknats, så att man kan kolla på listan "voteslist" och se att ```voteslist.index(RÖSTANTAL)``` korresponderar med positionsvärdeet i dicten.
```python
    {'Partinamn': 'Partikelpartiet',
     'Vänster': True,
     'Block': 'Småpartierna',
     'Partiledare': 'Herman Muskelberg',
     'Min_Röst': 2,
     'Max_Röst': 8,
     'Position': 1
     },
```

### Diagram
Diagrammet bygger på matplotlib och är relativt grundläggande. Jag kunde ganska enkelt hitta dokumentation om hur det fungerar, och det var väldigt enkelt att modifiera koden för att få det man ville. Jag gillar den minimalistiska men praktiska designen i hur staplarna och axlarna ser ut. Ett cirkeldiagram hade sett riktigt coolt ut, men efter att ha sett att en klasskamrat redan hade ett cirkeldiagram bestämde jag mig för att testa något annat.

![alt_text](https://raw.githubusercontent.com/abbindustrigymnasium/programmering-1-miniprojekt-abbwiljoh/master/bilder/Valresultat_bild.jpg "Diagram från Val.py")

### Frågor
Om du har några frågor eller om det finns några okklarheter, kontakta mig.
