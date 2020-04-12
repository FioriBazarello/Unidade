import modules.sounds as sd

basicSounds = {
  'ask_yes': 'Sim?',
  'intention_not_recognized': 'Sim?',
  'searching': 'Pesquisando...',
  'searching_location': 'Pesquisando localização...',
  'searching_route': 'Pesquisando rota...',
  'exiting': 'Parando execução'
}

print("Criando frases básicas...")

for sound in basicSounds:
  print('Gerando ' + sound)
  sd.generateSound(sound, basicSounds[sound])
