from random import choice
import json
import math

filename = 'rollen_simpel.json'
with open(filename) as f:
    rollen_simpel = json.load(f)

rollen_positief = []
rollen_negatief = []

for rol in rollen_simpel:
    if rol['score'] > 0:
        rollen_positief.append(rol)
    else:
        rollen_negatief.append(rol)

aantal_spelers = 18
gewenste_score = 0

def aantal_weerwolven(rollen_gekozen, treklijst_negatief):
    """Selecteert het aantal weerwolven in het spel
        en voegt ze toe aan rollen_gekozen"""
    if aantal_spelers <= 10:
        min_weerwolven = 2
        treklijst_negatief.remove({'rolnaam' : 'weerwolf', 'score' : -6, 'aantal' : 12, 'voorwaarde' : ''})
    elif aantal_spelers <= 18:
        min_weerwolven = math.ceil(aantal_spelers / 4) - 1
        for rol in treklijst_negatief:
            if rol['rolnaam'] == 'weerwolf':
                rol['aantal'] = min_weerwolven + 1
    else:
        min_weerwolven = math.ceil(aantal_spelers / 4) - 1
        for rol in treklijst_negatief:
            if rol['rolnaam'] == 'weerwolf':
                rol['aantal'] = min_weerwolven + 2
    active = True
    while active:
        rollen_gekozen.append('weerwolf')
        aantal_ww = rollen_gekozen.count('weerwolf')
        if aantal_ww == min_weerwolven:
            active = False

def aantal_burgers(rollen_gekozen):
    """Selecteert het aantal burgers in het spel
        en voegt ze toe aan rollen_gekozen"""
    geschat_burgers = math.ceil(aantal_spelers / 3) - 1
    active = True
    while active:
        rollen_gekozen.append('burger')
        aantal_gb = rollen_gekozen.count('burger')
        if aantal_gb == geschat_burgers:
            active = False

def score_berekenen(rollen_gekozen):
    """Berekent de score op basis van de gekozen rollen"""
    score = 0
    for rol in rollen_simpel:
        score += rollen_gekozen.count(rol['rolnaam'])*rol['score']
    return score

def formatteer(rollen_gekozen):
    """Formateert de gekozen rollen netjes"""
    print("\nDe volgende rollen doen mee:")
    for gekozen_rol in sorted(rollen_gekozen):
        print(f"- {gekozen_rol.title()}")

def voorwaarden(rollen_gekozen, nieuwe_rol):
    """Bekijkt of aan voorwaarden van nieuwe rol zijn voldaan"""
    if nieuwe_rol['voorwaarde'] == '':
        voorwaarde = True
    elif nieuwe_rol['voorwaarde'] in rollen_gekozen:
        voorwaarde = True
    else:
        voorwaarde = False
    return voorwaarde

def trek_rol(rollenlijst):
    """Trekt een rol uit de goede lijst."""
    try:
        nieuwe_rol = choice(rollenlijst)
    except IndexError:
        #als treklijst leeg is: gooi Burger erin
            nieuwe_rol = {'rolnaam' : 'burger', 'score' : 1, 'aantal' : 20, 'voorwaarde' : ''}
    return nieuwe_rol

def rollen_kiezen():
    """Kiest rollen en voegt deze toe aan de lijst rollen_gekozen"""
    rollen_gekozen = []
    treklijst_positief = rollen_positief[:]
    treklijst_negatief = rollen_negatief[:]
    aantal_weerwolven(rollen_gekozen, treklijst_negatief)
    aantal_burgers(rollen_gekozen)
    #while-loop trekt nieuwe kaarten
    while len(rollen_gekozen) < aantal_spelers:
        if score_berekenen(rollen_gekozen) < gewenste_score:
            nieuwe_rol = trek_rol(treklijst_positief)
        else:
            nieuwe_rol = trek_rol(treklijst_negatief)
        #bij de laatste kaart geen grote invloed op score meer
#        if nieuwe_rol['score'] < -3:
#            if aantal_spelers - len(rollen_gekozen) == 1:
#                continue
#            else:
#                 rollen_gekozen.append(nieuwe_rol['rolnaam'])
#        elif nieuwe_rol['score'] > 3:
#             if aantal_spelers - len(rollen_gekozen) == 1:
#                  continue
#             else:
#                  if voorwaarden(rollen_gekozen, nieuwe_rol):
#                      rollen_gekozen.append(nieuwe_rol['rolnaam'])
#              else:
#                  continue
        #voegt elke andere kaart toe aan rollen_gekozen
#       else:
        if voorwaarden(rollen_gekozen, nieuwe_rol):
            rollen_gekozen.append(nieuwe_rol['rolnaam'])
        else:
            continue
            #als max aantal bereikt, rol uit treklijst
        if rollen_gekozen.count(nieuwe_rol['rolnaam']) == nieuwe_rol['aantal']:
            if nieuwe_rol['score'] > 0:
                treklijst_positief.remove(nieuwe_rol)
            else:
                treklijst_negatief.remove(nieuwe_rol)
    return rollen_gekozen

def test(number_of_times):
    for number in range(number_of_times):
        rollen_gekozen = rollen_kiezen()
        print(rollen_gekozen)

test(99)

print('hello world')
