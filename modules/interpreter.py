from enum import Enum

import modules.sounds as sd
import utilities.search as search
import utilities.weather as weather

def readFrase(message):
    message = message.lower()
    print(message)
    if isCalling(message):
        intention = searchIntention(message)
        subjects = searchSubject(message)
        intentionAction(intention, subjects)

def isCalling(message):
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

    if intention == intentions.search:
        search.searchDefinition(subjects)

    if intention == intentions.weather:
        weather.criarPrevisao()

class intentions(Enum):
    undefined = 0
    openProgram = 1
    search = 2
    weather = 3

verbs = {
    'abra' : 1,
    'abre' : 1,
    'abrir' : 1,
    'rode' : 1,
    'rodar' : 1,
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
}

ignoreWords = [
    'sobre',
    'um',
    'por',
]