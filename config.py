import modules.sounds as sd

basicSounds = {
  'ask_yes': 'Sim?',
  'intention_not_recognized': 'Sim?',
  'searching': 'Pesquisando...',
}

print("Criando frases básicas...")

for sound in basicSounds:
  print('Gerando ' + sound)
  sd.generateSound(sound, basicSounds[sound])
