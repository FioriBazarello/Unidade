from enum import Enum
from re import match
from selenium import webdriver
import utilities.definition as definition
import utilities.weather as weather
import controls.sounds as sd

def readFrase(message):
    message = message.lower()
    intention = searchIntention(message)
    subjects = searchSubject(message)
    intentionAction(intention, subjects)

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
        print("Não entendi sua intenção")
        sd.playSound('intention_not_recognized')

    if intention == intentions.openProgram:
        frase = "Eu devo abrir o programa {0}".format(subjects)
        fileName = 'open_program'
        print(frase)
        sd.generateSound(fileName, frase)
        sd.playSound(fileName)

    if intention == intentions.search:
            frase = "Buscando sobre {0}".format(subjects)
            fileName = 'search_for'
            print(frase)
            sd.generateSound(fileName, frase)
            sd.playSound(fileName)

            definition.searchDefinition(subjects)

    if intention == intentions.weather:
        weather.criarPrevisao()
        frase = "Eu devo buscar sobre {0}".format(subjects)
        fileName = 'search_for'

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
    'previsão' : 3
}

ignoreWords = [
    'sobre',
    'um'
]