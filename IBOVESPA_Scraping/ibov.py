import pandas as pd
import requests
from bs4 import BeautifulSoup

pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 200)

def busca_carteira_teorica(indice):
    url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice={}&idioma=pt-br'.format(indice.upper())
    return pd.read_html(url, decimal=',', thousands='.', index_col='Código')[0][:-1]

def busca_pagina_teorica(indice):
    url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice={}&idioma=pt-br'.format(indice.upper())
    page = requests.get(url)
    return page

ibov = busca_carteira_teorica('ibov')
ibov.sort_values('Part. (%)', ascending=False)

ibovpagina = busca_pagina_teorica('ibov')

soup = BeautifulSoup(ibovpagina.content,'html.parser')
results = soup.find(id='ctl00_contentPlaceHolderConteudo_grdResumoCarteiraTeorica_ctl00_ctl03_ctl00_lblRedutorResultado')

#redutor = results.find_all('span', class_='label')

txt = results.text 
x = txt.replace(".", "")
y = x.replace(",", ".")
z = float(y)
print (ibov)

