import random as r
# Numpy och matplot/lib används för att skriva ut ett fint diagram. Planen var att först
import matplotlib
# ha ett cirkeldiagram med de olika partierna, men jag såg att en kamrat  hade haft samma
import matplotlib.pyplot as plt
# idé så jag använder ett stolpdiagram istället.
import numpy as np

P = {'Partier': [                       # Dictionariet bygger på informationen från tabellen i instruktionerna.
    {'Partinamn': 'Gröngölingarna',     # Partinamn förklarar sig självt, det ä en string.
     'Vänster': True,                   # Inriktnigen är bool, de är enkla att arbeta med
     'Block': 'Småpartierna',           # Block, string
     # Partiledare har jag hittat på själv, också string. (Det var roligt att hitta på skämtnamm)
     'Partiledare': 'Steffe Stortå',
     # Min-/Maxröster används i randomiser-funktionen för att veta inom vilket område röstantalet ska finnas i.
     'Min_Röst': 3,
     'Max_Röst': 12,
     # Positionen säger vilken position informationen har i voteslist, för att jag ska kunna hålla koll på alla namn och partiledare.
     'Position': 0
     },                                 # Positionen tillåter också tillägg till listan med nya partier utan att behöva ändra för mycket i koden.
    {'Partinamn': 'Partikelpartiet',
     'Vänster': True,
     'Block': 'Småpartierna',
     'Partiledare': 'Herman Muskelberg',
     'Min_Röst': 2,
     'Max_Röst': 8,
     'Position': 1
     },
    {'Partinamn': 'Mälarpartiet',
     'Vänster': False,
     'Block': 'Småpartierna',
     'Partiledare': 'Gunnel Skyhög',
     'Min_Röst': 8,
     'Max_Röst': 18,
     'Position': 2
     },
    {'Partinamn': 'Sjörövarpartiet',
     'Vänster': False,
     'Block': 'Småpartierna',
     'Partiledare': 'Grigorij Svartskägg',
     'Min_Röst': 3,
     'Max_Röst': 12,
     'Position': 3
     },
    {'Partinamn': 'Extremisterna',
     'Vänster': False,
     'Block': 'Oljeblocket',
     'Partiledare': 'Lex Muthor',
     'Min_Röst': 3,
     'Max_Röst': 6,
     'Position': 4
     },
    {'Partinamn': 'Maskinpartiet',
     'Vänster': True,
     'Block': 'Oljeblocket',
     'Partiledare': 'Jo-hanna Nähä',
     'Min_Röst': 12,
     'Max_Röst': 22,
     'Position': 5
     },
    {'Partinamn': 'Framtidspartiet',
     'Vänster': False,
     'Block': 'Oljeblocket',
     'Partiledare': 'Doktor Bruun',
     'Min_Röst': 12,
     'Max_Röst': 18,
     'Position': 6
     },
    {'Partinamn': 'Allpartiet',
     'Vänster': True,
     'Block': 'Inget',
     'Partiledare': 'Steve Harwell',
     'Min_Röst': 20,
     'Max_Röst': 34,
     'Position': 7
     },

]}

voteslist = []
loserslist = []
winnerlist = []
oljelist = []       # För att försöka hålla koden så dynamisk som möjligt använder jag listor, vilket begränsar möjligheterna, men låter de
smålist = []        # redan implementerade funktionerna fungera mer dynamiskt
vänlist = []
höglist = []
Vänster = 0         # Värden för att sedan räkna de olika inriktningarnas röster
Höger = 0

# Jag tycker att det är skönast att jobba med bool-värden i while-loopar, för då kan man enkelt "stänga av" dem.
Kommentar = False
comma = True
omval = True


# Sorterar angiven lista genom att jämföra varje värde i listan med det tänkta största värdet för att sedan få ut ett ensamt värde.
def orderlist(lista):
    a = lista[0]
    for x in lista:
        if x > a:           # Om det jämförda värdet är större än det nuvarande största värdet, blir det jämförda värdet det nya största värdet.
            a = x
    return a


def reaction(name, party, votes, Positiv=True):
    PoRe = ['tar med glädje emot ' + str(votes)+'% röster', 'är tacksam för '+str(
        votes) + '%', 'är glad över '+str(votes)+'%']                                   # En funktion så jag slipper skriva ut reaktionen hella tiden.

    NeRe = ['är missnöjd över ', 'gillar inte ', 'vägrar acceptera ',
            'är förkrossad över ', 'låtsas vara oberörd av ', 'är rosenrasande över ']
    # Slumpar ett svar utifrån positiva och negativa omständigheter.
    if Positiv == True:
        print(name, 'från', party, str(r.choice(PoRe)))
    else:
        print(name, 'från', party, str(r.choice(NeRe)) + str(votes)+'%')


# En egen funktion för att kunna få partiledaren från det största partiet i en falang reagera på resultatet.
def hvreaction(leader, party, vänster=False):
    reactions = ['uppskattar att', 'är nöjd över att', 'är tacksam för att']
    if vänster == True:
        print(leader+' från det största vänster-partiet,', party +
              ', '+str(r.choice(reactions)), 'vänstern är störst.')
    if vänster == False:
        print(leader+' från det största höger-partiet,', party +
              ', ' + str(r.choice(reactions)), 'högern är störst.')


# Partiledarna ska kunna göra handlingar som påverkar hur folk röstar på dem.
def kommentar(leader, party, bad=True):
    badK = ['förolämpade en folkgrupp!', 'har begått ett brott!', 'provocerar ryssarna!',
            'kastade pajer på motståndet!', 'har kommit ut som usel sångare!', 'snubblade över sin egen hand!']
    # För tillfället används inte denna rad, men jag lämnar den här för framtida ändringar
    goodK = ['sade att de gillade att människor mår bra!']
    if bad == True:
        print(leader, 'från', party, r.choice(badK))
    elif bad == True:
        print(leader, 'från', party, r.choice(goodK))


# Det finns 1/5 chans att någon gör en dum handling
kchans = r.randint(0, 4)
if kchans == 0:
    dummis = r.choice(P['Partier'])
    Kommentar = True

print('Partier:')
# Varje parti i dicten ska skrivas ut med ett kommatecken, förutom det allra sista.
for parti in P['Partier']:
    while comma == True:                    # Jag tycker att det ser snyggt ut :)
        print(parti['Partinamn']+',')
        if P['Partier'].index(parti) == len(P['Partier'])-2:
            comma = False
        break
    else:
        print(parti['Partinamn'])

if Kommentar == True:
    # Om vi har en dummis som gör bort sig ska den förlora 20% av sina röstchanser
    kommentar(dummis['Partiledare'], dummis['Partinamn'], True)
    # Detta innebär att alla andra partier kan få lite fler röster automatiskt
    dummis['Min_Röst'] = round(dummis['Min_Röst']*0.8)
    dummis['Max_Röst'] = round(dummis['Max_Röst']*0.8)
    print('Det var super-effektivt!',
          dummis['Partinamn'], 'förlorade 20% av väljarbasen!')

for parti in P['Partier']:
    # Delar ut röster utifrån min-/ och maxröster
    votes = r.randint(parti['Min_Röst'], parti['Max_Röst'])
    voteslist.append(votes)
    if sum(voteslist) > 100:
        while omval == True:
            # Om röstantalet är mer än 100, kastas rösterna om tills de inte är mer än 100 längre.
            voteslist.clear()
            for parti in P['Partier']:
                votes = r.randint(parti['Min_Röst'], parti['Max_Röst'])
                # I det här programmet är voteslist min bästa vän, och därför förblir den oförändrad.
                voteslist.append(votes)
            # Skulle något värde tas bort från listan skulle positionerna i dicten bli värdeösa,
            if sum(voteslist) <= 100:
                omval = False                       # och jag skulle inte kunna leka mer med partierna :(
                break
nonvotes = 100-sum(voteslist)
# print(voteslist)
print('\n'+str(sum(voteslist))+'% voter turnout')
if nonvotes > 0:
    # Röstare och icke-röstare
    print(str(nonvotes)+'% avstod från att rösta.')
print()

for parti in P['Partier']:
    if parti['Block'] == 'Småpartierna':
        # Partierna sorteras in i blocken som står i dicten
        smålist.append(voteslist[parti['Position']])
    elif parti['Block'] == 'Oljeblocket':
        oljelist.append(voteslist[parti['Position']])

    if int(voteslist[parti['Position']]) >= 4:
        print(parti['Partinamn']+': ' +
              str(voteslist[parti['Position']]) + '%')      # Alla partier som kvalificerar till riksdagen skrivs ut här
    else:
        loserslist.append(parti['Partinamn'])
        if parti['Block'] == 'Småpartierna':
            # Om partierna inte kvalificerar tas de bort från alla sorteringar, förutom voteslist förstås
            smålist.remove(voteslist[parti['Position']])
        if parti['Block'] == 'Oljeblocket':
            oljelist.remove(voteslist[parti['Position']])
    if parti['Vänster'] == True:
        # Sorterar till antalet röster i varje inriktining
        Vänster += voteslist[parti['Position']]
        vänlist.append(voteslist[parti['Position']])
    else:
        Höger += voteslist[parti['Position']]
        höglist.append(voteslist[parti['Position']])


for loser in loserslist:
    # Kom ett parti inte in i riksdagen måste vi ju få veta...
    print(loser+' kom inte in i Riksdagen')

# orkar inte skriva sum(oljelist), visar hur många röster vardera block fick
Oljeblock = sum(oljelist)
Småblock = sum(smålist)

print()
for v in voteslist:
    winnerlist.append(v)

win = orderlist(winnerlist)     # Sorterarfunktionen används här för att hitta största partier: I valet, vänstern och högern.
vän = orderlist(vänlist)
hög = orderlist(höglist)

if Vänster > Höger:
    for parti in P['Partier']:
        if voteslist[parti['Position']] == vän:
            hvreaction(parti['Partiledare'],            # Höger-/Vänster-reaktionsfunktionen används här så partiledaren kan reagera till resultatet
                       parti['Partinamn'], parti['Vänster'])
elif Vänster < Höger:
    for parti in P['Partier']:
        if voteslist[parti['Position']] == hög:
            hvreaction(parti['Partiledare'],
                       parti['Partinamn'], parti['Vänster'])
else:
    # Jag är ingen politiker, så jag vet inte vad som händer om inriktiningarna är lika stora.
    print('Inriktningarna är lika stora!')


# Eftersom jag bryr mig om miljön återanvänder jag listor, dessutom slipper jag skriva en extra rad där jag definierar listan
winnerlist.clear()
for parti in P['Partier']:
    if int(voteslist[parti['Position']]) == int(win):   # Här används voteslist för att identifiera vem rösterna tillhör
        winner = parti
        winnerlist.append(parti)                        # Återanvändning av vinnarlistan för att lagra alla vinnare, ifall det skulle finnas flera
        if len(winnerlist) == 1:
            print(winner['Partinamn'] + ' är störst parti med ' +
                  str(voteslist[winner['Position']]) + '%')
        elif len(winnerlist) == 2:                          # Finns alltid möjlighet att två partier delar på vinsten
            print(winnerlist[0]+' och '+winnerlist[1] +                 
                  ' fick båda högst antal röster med ' + str(voteslist[winner['Position']])+'%')

if Oljeblock > Småblock:                # Jämför de två blocken för att se vilket som är störst, eller om de är lika stora.
    print('Oljeblocket är största blocket med ' + str(Oljeblock) + '%')
    print('Småpartierna fick', str(Småblock)+'%')
elif Oljeblock == Småblock:
    print('Blocken är lika stora med '+str(Oljeblock)+'% var')
else:
    print('Småpartierna är största blocket med ' + str(Småblock)+'%')
    print('Oljeblocket fick', str(Oljeblock)+'%')

print('Högerröster: ' + str(Höger)+'%\nVänsterröster: ' + str(Vänster)+'%')     # Skriver ut antalet röster för varje inriktning
print()

for parti in P['Partier']:
    if voteslist[parti['Position']] < 4:
        reaction(parti['Partiledare'], parti['Partinamn'],  # För "förlorarna" använder vi de negativa reaktionerna.
                 voteslist[parti['Position']], False)
    if winner == parti:
        reaction(parti['Partiledare'], parti['Partinamn'],  # Vinnaren måste såklart reagera till vinsten
                 voteslist[parti['Position']], True)
if Kommentar== True:
    print(dummis['Partiledare'],'från'+dummis['Partinamn'],'ber om ursäkt för den tidigare incidenten') # Har någon gjort fel, ber de om ursäkt.

namnlist = []
for parti in P['Partier']:
    namnlist.append(parti['Partinamn'])     # Vi vill göra en lista med alla partinamn som labels på stolpdiagrammet
# För charten:
x = np.arange(len(namnlist))  # För att namnen ska skrivas ut med rätt längd och antal
width = 0.35  # Bredden på stolparna

fig, ax = plt.subplots()            # Skapar diagrammet
rects = ax.bar(x, voteslist, width) # Skapar stolparna, med namn osv

# Här skrivs allt ut:
ax.set_ylabel('Röster (%)')
ax.set_title('Val 2022')        # Massa etiketter ger ett alldeles pimpat diagram.
ax.set_xticks(x)
ax.set_xticklabels(namnlist)


def autolabel(rects):
    # Denna funktion skriver ut antal röster ovanför vardera stolpe.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Avstånd från stapeln
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects)
fig.canvas.set_window_title('Valresultat')  # Titeln på själva pop-up fönstret.
fig.tight_layout()

visa = input(
    '\nVill du se ett diagram av resultatet?\nJa eller Nej?\n>').title()
if 'Ja' in visa:
    plt.show()                          # Vill man inte se diagrammet ska man inte behöva se den.
else:
    pass
