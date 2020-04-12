from gtts import gTTS
import playsound
import random
import os

userLang = 'pt'

def generateSound(audioName, frase):
    voz = gTTS(frase, lang = userLang)
    voz.save('resources/sounds/' + audioName + '.mp3')

def playSound(audioName):
    playsound.playsound('resources/sounds/' + audioName + '.mp3')

def deleteSound(audioName):
    os.remove('resources/sounds/' + audioName + '.mp3')

def playTemporarySound(frase):
    audioName = 'audio_' + str(random.randint(1, 20000000))
    generateSound(audioName, frase)
    playSound(audioName)
    deleteSound(audioName)