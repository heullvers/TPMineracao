import requests
from bs4 import BeautifulSoup

import csv

from dados_da_partida import coleta_dados
from classes.Partida import Partida


##escrita arquivo
f = open('Testes/verificacao_partidas_4.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('posicao_time_dentro', 'posicao_time_fora',  'media_gols_marcados_por_jogo_time_casa_em_casa', 'media_gols_sofridos_por_jogo_time_casa_em_casa', 'media_gols_sofridos_por_jogo_time_visitante_fora',
                        'gols_marcados_time_casa_segundo_sexto', 'gols_marcados_time_visitante_segundo_sexto', 'gols_sofridos_time_visitante_quinto_sexto', 'quantidade_de_gols_no_momento_expulsao_um_time_a',
                        'minuto_expulsao_um', 'minuto_expulsao_dois', 'diferenca_gols_expulsao_um', 'diferenca_gols_expulsao_dois', 'expulsao_dois_m_v_Visitante', 'quarto_ultimo_jogo_visitante_V',
                        'momento_expulsao_um_v_d_e_V', 'expulsao_um_m_v_Mandante', 'momento_expulsao_dois_v_d_e_D', 'momento_expulsao_dois_v_d_e_E', 'momento_expulsao_dois_v_d_e_V','resultado_final_v_d_e'
                    ))

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
    

    ##EM CASO DE ERROS DURANTE A COLETA AJUSTAR AQUI AS TEMPORADAS
    #del links_temporadas[0:12]

    for l in links_temporadas:
        link =  link_inicial + l

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
            ##EM CASO DE ERROS DURANTE A COLETA AJUSTAR AQUI AS RODADAS
            '''
            if(l == "/2272"):
                
                del rodadas_do_ano[0:28]
                print("deletei")
            else:
                print("nao deletei")
            '''
            
            for rodada in rodadas_do_ano:

                page = requests.get(rodada)
                soup = BeautifulSoup(page.content, 'html.parser')

                rodada_atual = soup.find("td", id="week-gr")
                if(rodada_atual):
                    rodada_atual = int(rodada_atual.find("span").get_text())
                else:
                    rodada_atual = None


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
                    partida = coleta_dados(link)
                    print('AQUII')
                    print(partida)
                    
                    if(partida):
                        print('entrei')
                        print(nome_campeonato)
                        print(temporada)
                        print(pais)
                        print(rodada_atual)
                        writer.writerow((partida.posicao_time_dentro, partida.posicao_time_fora,  partida.media_gols_marcados_por_jogo_time_casa_em_casa, partida.media_gols_sofridos_por_jogo_time_casa_em_casa, partida.media_gols_sofridos_por_jogo_time_visitante_fora,
                        partida.gols_marcados_time_casa_segundo_sexto, partida.gols_marcados_time_visitante_segundo_sexto, partida.gols_sofridos_time_visitante_quinto_sexto, partida.quantidade_de_gols_no_momento_expulsao_um_time_a,
                        partida.minuto_expulsao_um, partida.minuto_expulsao_dois, partida.diferenca_gols_expulsao_um, partida.diferenca_gols_expulsao_dois, partida.expulsao_dois_m_v_Visitante, partida.quarto_ultimo_jogo_visitante_V,
                        partida.momento_expulsao_um_v_d_e_V, partida.expulsao_um_m_v_Mandante, partida.momento_expulsao_dois_v_d_e_D, partida.momento_expulsao_dois_v_d_e_E, partida.momento_expulsao_dois_v_d_e_V, partida.resultado_final_v_d_e    
                            ))
finally:
    f.close()
        
        
'''
print(nome_campeonato)
print(temporada)
print(pais)
print(rodada_atual)
print(link_ficha_de_jogo)
'''
###############################################################




