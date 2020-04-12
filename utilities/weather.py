from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import modules.sounds as sounds

# Esse codigo é de Osasco. Para conseguir outros, faça a busca com o
# nome da sua cidade: http://servicos.cptec.inpe.br/XML/listaCidades?city=NomeDaCidade
cityCode = '3656'

def criarPrevisao():
    hora = datetime.now()

    target = urlopen('http://servicos.cptec.inpe.br/XML/cidade/{0}/previsao.xml'.format(cityCode))
    content = BeautifulSoup(target.read(), 'lxml')
    previsao = content.find('previsao')
    
    maxima = previsao.find('maxima').get_text()
    minima = previsao.find('minima').get_text()
    clima = previsao.find('tempo').get_text()

    frase = "Hoje, {0} de {1}, terá mínima de {2} e máxima de {3} Graus Celsius, {4}".format(hora.day, mes[str(hora.month)], minima, maxima, climas[clima])
    sounds.playTemporarySound(frase)

climas = {
    'ec':'Encoberto com Chuvas Isoladas',
    'ci':'Chuvas Isoladas',
    'c':'Chuva',
    'in':'Instável',
    'pp':'Possibilidade de Pancadas de Chuva',
    'cm':'Chuva pela Manhã',
    'cn':'Chuva à Noite',
    'pt':'Pancadas de Chuva à Tarde',
    'pm':'Pancadas de Chuva pela Manhã',
    'np':'Nublado e Pancadas de Chuva',
    'pc':'Pancadas de Chuva',
    'pn':'Parcialmente Nublado',
    'cv':'Chuvisco',
    'ch':'Chuvoso',
    't':'Tempestade',
    'ps':'Predomínio de Sol',
    'e':'Encoberto',
    'n':'Nublado',
    'cl':'Céu Claro',
    'nv':'Nevoeiro',
    'g':'Geada',
    'ne':'Neve',
    'nd':'Não Definido',
    'pnt':'Pancadas de Chuva à Noite',
    'psc':'Possibilidade de Chuva',
    'pcm':'Possibilidade de Chuva pela Manhã',
    'pct':'Possibilidade de Chuva à Tarde',
    'pcn':'Possibilidade de Chuva à Noite',
    'npt':'Nublado com Pancadas à Tarde',
    'npn':'Nublado com Pancadas à Noite',
    'ncn':'Nublado com Possibilidade de Chuva à Noite',
    'nct':'Nublado com Possibilidade de Chuva à Tarde',
    'ncm':'Nublado com Possibilidade de Chuva pela Manhã',
    'npm':'Nublado com Pancadas de Chuva pela Manhã',
    'npp':'Nublado com Possibilidade de Chuva',
    'vn':'Variação de Nebulosidade',
    'ct':'Chuva à Tarde',
    'ppn':'Possibilidade de Pancadas de Chuva à Noite',
    'ppt':'Possibilidade de Pancadas de Chuva à Tarde',
    'ppm':'Possibilidade de Pancadas de Chuva pela Manhã'
}

mes = {
    '1' : 'janeiro',
    '2' : 'fevereiro',
    '3' : 'março',
    '4' : 'abril',
    '5' : 'maio',
    '6' : 'junho',
    '7' : 'julho',
    '8' : 'agosto',
    '9' : 'setembro',
    '10' : 'outubro',
    '11' : 'novembro',
    '12' : 'dezembro'
}