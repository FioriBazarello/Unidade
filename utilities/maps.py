
import webbrowser
import modules.sounds as sounds

def searchLocation(terms):
  sounds.playSound('searching_location')
  webbrowser.open_new_tab('https://www.google.com/maps/search/{0}'.format(terms))

def searchRoute(terms):
  print(terms)
  sounds.playSound('searching_route')
  webbrowser.open_new_tab('https://www.google.com/maps/dir/{0}/{1}'.format('Osasco', 'Cuzco'))
  