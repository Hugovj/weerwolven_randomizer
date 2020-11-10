import json

rollen_simpel = [
                {'rolnaam' : 'weerwolf', 'score' : -6, 'aantal' : 12, 'voorwaarde' : ''},
                {'rolnaam' : 'lieveling', 'score' : -6, 'aantal' : 1, 'voorwaarde' : ''},
                {'rolnaam' : 'tovenares', 'score' : -3, 'aantal' : 1, 'voorwaarde' : 'ziener'},
                {'rolnaam' : 'ziener', 'score' : 7, 'aantal' : 2, 'voorwaarde' : ''},
                {'rolnaam' : 'burger', 'score' : 1, 'aantal' : 20, 'voorwaarde' : ''},
                {'rolnaam' : 'heks', 'score' : 4, 'aantal' : 1, 'voorwaarde' : ''},
                {'rolnaam' : 'magiër', 'score' : 4, 'aantal' : 1, 'voorwaarde' : ''},
                {'rolnaam' : 'lijfwacht', 'score' : 3, 'aantal' : 1, 'voorwaarde' : ''},
                {'rolnaam' : 'jager', 'score' : 3, 'aantal' : 1, 'voorwaarde' : ''},
                {'rolnaam' : 'leerlingziener', 'score' : 4, 'aantal' : 1, 'voorwaarde' : 'ziener'},
                ]

filename = 'rollen_simpel.json'
with open(filename, 'w') as f:
    json.dump(rollen_simpel, f)
