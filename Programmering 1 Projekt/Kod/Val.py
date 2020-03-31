# 3. Reagera!
import random as r
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

P = {'Partier': [
    {'Partinamn': 'Gröngölingarna',
     'Vänster': True,
     'Block': 'Småpartierna',
     'Partiledare': 'Steffe Stortå',
     'Min_Röst': 3,
     'Max_Röst': 12,
     'Position': 0
     },
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
     'Partiledare': 'Doc Bruun',
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
oljelist = []
smålist = []
vänlist = []
höglist = []
Vänster = 0
Höger = 0

comma = True
omval = True


def reaction(name, party, votes, Positiv=True):
    PoRe = ['tar med glädje emot ' + str(votes)+'% röster', 'är tacksam för '+str(
        votes) + '%', 'är glad över '+str(votes)+'%']

    NeRe = ['är missnöjd över ', 'gillar inte ', 'vägrar acceptera ',
            'är förkrossad över ', 'låtsas vara oberörd av ', 'är rosenrasande över ']
    if Positiv == True:
        print(name, 'från', party, str(r.choice(PoRe)))
    else:
        print(name, 'från', party, str(r.choice(NeRe)) + str(votes)+'%')
def hvreaction(leader, party, vänster= False):
    reactions= ['uppskattar att', 'är nöjd över att', 'är tacksam för att']
    if vänster== True:
        print(leader+' från det största vänster-partiet,', party+', '+str(r.choice(reactions)), 'vänstern är störst.')
    if vänster == False:
        print(leader+' från det största höger-partiet,', party+', '+ str(r.choice(reactions)),'högern är störst.')

# WIPPPPPPPPPPPP
print('Partier:')
for parti in P['Partier']:
    while comma == True:
        print(parti['Partinamn']+',')
        if P['Partier'].index(parti) == len(P['Partier'])-2:
            comma = False
        break
    else:
        print(parti['Partinamn'])
# För att alla partier, förutom det sista, ska skrivas ut med ett kommatecken. Det fyller ingen funktion men det ser snyggt ut :)
    votes = r.randint(parti['Min_Röst'], parti['Max_Röst'])
    voteslist.append(votes)
    if sum(voteslist) > 100:
        while omval == True:
            voteslist.clear()
            for parti in P['Partier']:
                votes = r.randint(parti['Min_Röst'], parti['Max_Röst'])
                voteslist.append(votes)
            if sum(voteslist) <= 100:
                omval = False
                break
nonvotes = 100-sum(voteslist)
# print(voteslist)
print('\n'+str(sum(voteslist))+'% voter turnout\n')
for parti in P['Partier']:
    if parti['Block'] == 'Småpartierna':
        smålist.append(voteslist[parti['Position']])
    elif parti['Block'] == 'Oljeblocket':
        oljelist.append(voteslist[parti['Position']])

    if int(voteslist[parti['Position']]) >= 4:
        print(parti['Partinamn']+': ' +
              str(voteslist[parti['Position']]) + '%')
    else:
        loserslist.append(parti['Partinamn'])
        if parti['Block'] == 'Småpartierna':
            smålist.remove(voteslist[parti['Position']])
        if parti['Block'] == 'Oljeblocket':
            oljelist.remove(voteslist[parti['Position']])
    if parti['Vänster'] == True:
        Vänster += voteslist[parti['Position']]
        vänlist.append(voteslist[parti['Position']])
    else:
        Höger += voteslist[parti['Position']]
        höglist.append(voteslist[parti['Position']])


for loser in loserslist:
    print(loser+' kom inte in i Riksdagen')

Oljeblock = sum(oljelist)
Småblock = sum(smålist)

print()
for v in voteslist:
    winnerlist.append(v)

# Vilket objekt i listan är störst?
win = winnerlist[0]
for x in winnerlist:
    if x > win:
        win = x
vän = vänlist[0]
for y in vänlist:
    if y > vän:
        vän = y
hög = höglist[0]
for z in höglist:
    if z > hög:
        hög = z

if Vänster > Höger:
    for parti in P['Partier']:
        if voteslist[parti['Position']]== vän:
            hvreaction(parti['Partiledare'], parti['Partinamn'],parti['Vänster'])
elif Vänster < Höger:
    for parti in P['Partier']:
        if voteslist[parti['Position']] == hög:
            hvreaction(parti['Partiledare'], parti['Partinamn'], parti['Vänster'])
else:
    print('Inriktningarna är lika stora!')

    # Partiledare för vän talar ut osv.

winnerlist.clear()
for parti in P['Partier']:
    if int(voteslist[parti['Position']]) == int(win):
        winner = parti
        winnerlist.append(parti)
        if len(winnerlist) == 1:
            print(winner['Partinamn'] + ' är störst parti med ' +
                  str(voteslist[winner['Position']]) + '%')
    #     print(winner['Partiledare'] + ' från', winner['Partinamn'] +
    #         ' reagerar till vinsten:\n' + r.choice(reaktioner))
        elif len(winnerlist) == 2:
            print(winnerlist[0]+' och '+winnerlist[1] +
                  ' fick båda högst antal röster med ' + str(voteslist[winner['Partinamn']])+'%')

if Oljeblock > Småblock:
    print('Oljeblocket är största blocket med ' + str(Oljeblock) + '%')
    print('Småpartierna fick', str(Småblock)+'%')
elif Oljeblock == Småblock:
    print('Blocken är lika stora med '+str(Oljeblock)+'% var')
else:
    print('Småpartierna är största blocket med ' + str(Småblock)+'%')
    print('Oljeblocket fick', str(Oljeblock)+'%')
print()

for parti in P['Partier']:
    if voteslist[parti['Position']] < 4:
        reaction(parti['Partiledare'], parti['Partinamn'],
                 voteslist[parti['Position']], False)
    if winner == parti:
        reaction(parti['Partiledare'], parti['Partinamn'],
                 voteslist[parti['Position']], True)

# print('Högerröster: ' + str(Höger)+'%\nVänsterröster: ' +
#       str(Vänster)+'%\nTotal: '+str(Höger+Vänster)+'%')

namnlist = []
for parti in P['Partier']:
    namnlist.append(parti['Partinamn'])

# För charten:
x = np.arange(len(namnlist))  # För att namnen ska skrivas ut rätt
width = 0.35  # Bredden på staplarna

fig, ax = plt.subplots()
rects = ax.bar(x, voteslist, width)

# Här skrivs allt ut:
ax.set_ylabel('Röster (%)')
ax.set_title('Val 2022')
ax.set_xticks(x)
ax.set_xticklabels(namnlist)


def autolabel(rects):
    # Denna funktion skriver ut antal röster ovanför vardera stapel.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Avstånd från stapeln
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects)
fig.canvas.set_window_title('Valresultat')
fig.tight_layout()

visa = input(
    '\nVill du se ett diagram av resultatet?\nJa eller Nej?\n>').title()
if 'Ja' in visa:
    plt.show()
else:
    pass

# Partiledare i största falang-partiet ska reagera till H-V-resultatet