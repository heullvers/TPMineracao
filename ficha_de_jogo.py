import requests
from bs4 import BeautifulSoup

#page do campeonato brasileiro 2019 na 15ª rodada.
page = requests.get("https://www.academiadasapostasbrasil.com/stats/competition/inglaterra-stats/8/17429/53145/0/4")


soup = BeautifulSoup(page.content, 'html.parser')

##OBTER NOME CAMPEONATO
campeonato = soup.find("p", class_="competition-title")
campeonato = campeonato.find("span").get_text()
campeonato = campeonato.split(' ')

nome_campeonato = ''

for i in range(len(campeonato) - 1):
    nome_campeonato += campeonato[i] + ' '

nome_campeonato = nome_campeonato.rstrip()

##OBTER TEMPORADA
temporada = campeonato[len(campeonato)-1]

##OBTER PAÍS
pais = soup.find("p", class_="competition-subtitle").get_text()

##OBTER NUMERO DA RODADA
rodada = soup.find("td", id="week-gr")
rodada = rodada.find("span").get_text()

###############################################################
#CAPTURAR LINK FICHA DE JOGO DE CADA RODADA
partidas_da_rodada = soup.find("table", class_="competition-rounds competition-half-padding") #obtém a tabela de partidas
tabela = partidas_da_rodada.find_all("td") #obtém todo o conteúdo de cada coluna da tabela

link_ficha_de_jogo = [] #lista com os links da ficha de cada jogo
aux = 1 #auxilia a controlar a coluna que está sendo visualizada


for partida in tabela:
    if(aux == 8):
        aux = 1
    elif(aux == 7):
        link = partida.find("a").get("href")
        icone = partida.find("span", class_="aa-icon-player")
        if(icone): #verificando se existe a ficha de jogo
            link_ficha_de_jogo.append(link)
        aux += 1
    else:
        aux += 1

'''
print(nome_campeonato)
print(temporada)
print(pais)
print(rodada)
print(link_ficha_de_jogo)
'''
###############################################################