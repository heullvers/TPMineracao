import requests
from bs4 import BeautifulSoup

url = 'http://servicos2.sjc.sp.gov.br/servicos/horario-e-itinerario.aspx?acao=p&opcao=1&txt='

req = requests.get(url)

soup = BeautifulSoup(req.text, 'lxml')

lista_itinerarios = soup.find_all('table', class_='textosm')

for lista_td in lista_itinerarios:
    lista = lista_td.find_all('td')
    #for lista_dados in lista:
        #print(lista_dados.next_element)



print(lista)