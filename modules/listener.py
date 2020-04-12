import speech_recognition as sr
import modules.interpreter as bot
from time import sleep

def callback(recog, frase):
    try:
        transc = recog.recognize_google(frase, language='pt')
        bot.readFrase(transc)
    except sr.UnknownValueError:
        print('=> Som não reconhecido')
    except sr.RequestError as err:
        print('=> Erro: {0}'.format(err))

def start():
    recog = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as fala:
        recog.adjust_for_ambient_noise(fala)

    print('Escutando')
    stopListening = recog.listen_in_background(fala, callback)

    while True: sleep(0.1)
        
    stopListening(wait_for_stop=False)