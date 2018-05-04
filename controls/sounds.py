from gtts import gTTS
from pygame import mixer

userLang = 'pt'
mixer.init()

def generateSound(audioName, frase):
    voz = gTTS(frase, lang = userLang)
    voz.save('resources/sounds/' + audioName + '.mp3')

def playSound(audioName):
    mixer.music.load('resources/sounds/' + audioName + '.mp3')
    mixer.music.play()
    esperarSom()

def esperarSom():
    while mixer.music.get_busy() == True:
        continue