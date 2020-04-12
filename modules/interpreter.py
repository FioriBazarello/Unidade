from enum import Enum

import modules.sounds as sd
import utilities.search as search
import utilities.weather as weather
import utilities.maps as maps

def readFrase(message):
    message = message.lower()
    print(message)
    if isCalling(message):
        intention = searchIntention(message)
        subjects = searchSubject(message)
        intentionAction(intention, subjects)

def isCalling(message):
    if message == 'unidade':
        sd.playSound('ask_yes')
        return False
    else:
        return 'unidade' in message

def searchIntention(message):
    intentionNum = 0
    words = message.split()

    for word in words:
        if word in verbs:
            intentionNum = verbs[word]

    return intentions(intentionNum)

def searchSubject(message):
    subjects = ""
    words = message.split()
    afterVerb = False

    for word in words:
        if word.lower() in verbs:
            afterVerb = True
        if afterVerb and word.lower() not in verbs:
            if ignoreWords.count(word) == 0 and len(word) > 1:
                subjects = subjects + " " + word

    return subjects.strip()

def intentionAction(intention, subjects):
    if intention == intentions.undefined:
        sd.playSound('intention_not_recognized')

    if intention == intentions.exit:
        sd.playSound('exiting')
        exit()

    if intention == intentions.search:
        search.searchDefinition(subjects)

    if intention == intentions.weather:
        weather.criarPrevisao()

    if intention == intentions.location:
        maps.searchLocation(subjects)

    if intention == intentions.route:
        maps.searchRoute(subjects)

class intentions(Enum):
    undefined = 0
    exit = 1
    search = 2
    weather = 3
    location = 4
    route = 5

verbs = {
    'saia' : 1,
    'feche' : 1,
    'pare' : 1,
    'pari' : 1,
    'buscar' : 2,
    'busque' : 2,
    'procurar' : 2,
    'procure' : 2,
    'achar' : 2,
    'ache' : 2,
    'pesquisar' : 2,
    'pesquise' : 2,
    'pesquisa' : 2,
    'previsão' : 3,
    'localize' : 4,
    'localiza' : 4,
    'rota': 5,
}

ignoreWords = [
    'sobre',
    'um',
    'por',
]