from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml
from unicodedata import normalize

def searchDefinition(name):
    name = normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    name = name.strip().replace(' ', '%20')

    target = urlopen('https://pt.wikipedia.org/w/api.php?format=xml&action=opensearch&search={0}&limit=1&namespace=0'.format(name))
    content = BeautifulSoup(target.read(), 'xml')

    
    description = content.find("Description").get_text()

    print(description)