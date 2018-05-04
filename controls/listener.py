import speech_recognition as sr
import controls.interpreter as bot
from time import sleep

def callback(recog, frase):
    try:
        transc = recog.recognize_google(frase, language='pt')
        # TODO: Verify for command and run it
        print(transc)
        bot.readFrase(transc)
    except sr.UnknownValueError:
        print('=> Som não reconhecido como fala humana <=')
    except sr.RequestError as err:
        print('=> Erro: {0}'.format(err))

def start():
    """
    Starts to listen the ambient sounds.
    """
    recog = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as fala:
        recog.adjust_for_ambient_noise(fala)

    print('Iniciando escuta')
    stopListening = recog.listen_in_background(fala, callback)

    while True: sleep(0.1)
        
    stopListening(wait_for_stop=False)