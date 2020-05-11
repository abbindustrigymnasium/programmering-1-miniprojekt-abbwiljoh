import random as r

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
    if Positiv:
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
    # goodK = ['sade att de gillade när människor mår bra!']
    if bad == True:
        print(leader, 'från', party, r.choice(badK))
    # elif bad == False:
    #     print(leader, 'från', party, r.choice(goodK))
