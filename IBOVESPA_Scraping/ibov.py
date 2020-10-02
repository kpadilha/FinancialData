import requests
from bs4 import BeautifulSoup

URL = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&idioma=pt-br'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ctl00_contentPlaceHolderConteudo_Pnltabela')

print(results.prettify())
