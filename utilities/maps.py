
import webbrowser
import re
import modules.sounds as sounds

def findRouteLocation(terms):
  firstPattern = "de (.*?)\ para"
  first = re.search(firstPattern, terms).group(1)
  
  secondPattern = "para (.*?)$"
  second = re.search(secondPattern, terms).group(1)

  return [first, second]

def searchLocation(terms):
  sounds.playSound('searching_location')
  webbrowser.open_new_tab('https://www.google.com/maps/search/{0}'.format(terms))

def searchRoute(terms):
  places = findRouteLocation(terms)
  sounds.playSound('searching_route')
  webbrowser.open_new_tab('https://www.google.com/maps/dir/{0}/{1}'.format(places[0], places[1]))
  