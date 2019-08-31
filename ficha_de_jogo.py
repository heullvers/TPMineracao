import requests
from bs4 import BeautifulSoup

#page do campeonato brasileiro 2019 na 15ª rodada.
page = requests.get("https://www.academiadasapostasbrasil.com/stats/competition/brasil-stats/26/16888/51143/0/21")


soup = BeautifulSoup(page.content, 'html.parser')

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
        #print(partida)
        link = partida.find("a").get("href")
        icone = partida.find("span", class_="aa-icon-player")
        if(icone): #verificando se existe a ficha de jogo
            link_ficha_de_jogo.append(link)
        aux += 1
    else:
        aux += 1

print(link_ficha_de_jogo)
###############################################################