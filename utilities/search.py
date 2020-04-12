import wikipedia
import webbrowser

import modules.sounds as sd

wikipedia.set_lang("pt")

def searchDefinition(name):
    sd.playSound('searching')
    summary = wikipedia.summary(name, sentences=1)
    page = wikipedia.page(name)

    webbrowser.open_new_tab(page.url)
    sd.playTemporarySound(summary)