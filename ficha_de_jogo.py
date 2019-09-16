import requests
from bs4 import BeautifulSoup

from dados_da_partida import coleta_dados

#page do campeonato brasileiro 2019 na 15ª rodada.

##MONTAR ARRAY COM LINK DOS CAMPEONATOS QUE SERÃO EXTRAÍDOS OS DADOS

link_inicial = "https://www.academiadasapostasbrasil.com/stats/competition/alemanha-stats/9"

page = requests.get(link_inicial)
soup = BeautifulSoup(page.content, 'html.parser')

##IDENTIFICAR CÓDIGOS DE CADA TEMPORADA PARA ACHAR LINK TEMPORADAS
links_ano = soup.find(class_="chzn-select select-season")
links_ano = links_ano.find_all("option")

links_temporadas = []
for option in links_ano:
    link = '/' + option.get("value")
    links_temporadas.append(link)

for l in links_temporadas:
    link =  link_inicial + l

    print('-------------------------------------------------------------------')

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    navegacao_rodada = soup.find(class_="competition-tr-title")

    if(navegacao_rodada):
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
        ultima_rodada = soup.find("td", id="week-gr")
        ultima_rodada = int(ultima_rodada.find("span").get_text())


        ##IDENTIFICAR LINKS RODADA DO ANO
        alternar_rodada = soup.find("td", id="week-gr")
        alternar_rodada = alternar_rodada.find(class_="group-url").get("value")

        rodadas_do_ano = []

        for i in range(ultima_rodada, 0, -1):
            link_rodada = alternar_rodada + str(i)
            rodadas_do_ano.append(link_rodada)

        ###############################################################

        for rodada in rodadas_do_ano:

            page = requests.get(rodada)
            soup = BeautifulSoup(page.content, 'html.parser')

            rodada_atual = soup.find("td", id="week-gr")
            rodada_atual = int(rodada_atual.find("span").get_text())


            print("CAMPEONATO", nome_campeonato)
            print("TEMPORADA", temporada)
            print("RODADA", rodada_atual)


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

            for link in link_ficha_de_jogo:
                coleta_dados(link)
    
    
    '''
    print(nome_campeonato)
    print(temporada)
    print(pais)
    print(rodada)
    print(link_ficha_de_jogo)
    '''
    ###############################################################