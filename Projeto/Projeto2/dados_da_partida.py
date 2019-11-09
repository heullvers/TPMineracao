# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana, identificar_minuto_expulsao_segundo_amarelo, identificar_minuto_expulsao_vermelho_direto, verificar_se_teve_expulsao, verifica_tempo_gols, verifica_placares_momentaneos
from classes.Partida import Partida
import datetime

def coleta_dados(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')


    dados_gerais_da_partida = soup.find("div", "stats-game-head")
    dados_gerais_da_partida = dados_gerais_da_partida.find_all("td")

    ##Identificar expulsoes
    time_a = soup.find(id="team_A_")
    time_b = soup.find(id="team_B_")

    ##TIME A
    minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_a)
    minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_a)
    minutos_expulsoes_time_a = minutos_seg_amarelo + minutos_ver_direto

    ###Auxilia a determinar futuramente atributo de v_d ou s_a
    expulsoes_verificar_cartao = []
    ##adiciona atributo de segundo amarelo ou cartão vermelho time a
    if(minutos_expulsoes_time_a):
        for expulsao in minutos_seg_amarelo:
            expulsoes_verificar_cartao.append([expulsao, 'Segundo amarelo', 'Mandante'])
        for expulsao in minutos_ver_direto:
            expulsoes_verificar_cartao.append([expulsao, 'Vermelho direto', 'Mandante'])
    
    ##TIME B
    minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_b)
    minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_b)
    minutos_expulsoes_time_b = minutos_seg_amarelo + minutos_ver_direto

    ##adiciona atributo de segundo amarelo ou cartão vermelho time b
    if(minutos_expulsoes_time_b):
        for expulsao in minutos_ver_direto:
            expulsoes_verificar_cartao.append([expulsao, 'Vermelho direto', 'Visitante'])
        for expulsao in minutos_seg_amarelo:
            expulsoes_verificar_cartao.append([expulsao, 'Segundo amarelo', 'Visitante'])

    if(len(expulsoes_verificar_cartao) > 1):
        expulsoes_verificar_cartao = sorted(expulsoes_verificar_cartao, key=lambda x:x[0])

    if(verificar_se_teve_expulsao(minutos_expulsoes_time_a, minutos_expulsoes_time_b)):

        minutos_gols_time_a = verifica_tempo_gols(time_a)
        minutos_gols_time_b = verifica_tempo_gols(time_b)

        minuto_expulsao_um = False
        minuto_expulsao_dois = False

        minutos_expulsoes = sorted(minutos_expulsoes_time_a + minutos_expulsoes_time_b)
        minuto_expulsao_um = minutos_expulsoes[0]

        if(len(minutos_expulsoes) > 1): #Houve mais de uma expulsão
            minuto_expulsao_dois = minutos_expulsoes[1]

        ### Descobrir o placar final do jogo
        resultado_final = dados_gerais_da_partida[1].find(class_="f-score odd").get_text().strip() #resultado final no formato (0-0)
        gols_times = resultado_final.split()

        gols_mandante = int(gols_times[0]) #quantidade de gols do time mandante
        gols_visitante = int(gols_times[2]) #quantidade de gols do time visitante

        ##placar do jogo no momento da expulsao
        minutos_expulsoes = sorted(minutos_expulsoes_time_a + minutos_expulsoes_time_b)
        placares_no_momento_da_expulsao = verifica_placares_momentaneos(minutos_expulsoes, minutos_gols_time_a, minutos_gols_time_b)

        ##atributos placar do jogo cada expulsao
        placar_momento_expulsao_um = None
        placar_momento_expulsao_dois = None

        ##atributos para verificar qual time levou cartao, mandante ou visitante
        expulsao_um_m_v = None
        expulsao_dois_m_v = None

        ##quantidade de gols no momento da expulsão
        quantidade_de_gols_no_momento_expulsao_um_time_a = None
        quantidade_de_gols_no_momento_expulsao_um_time_b = None

        quantidade_de_gols_no_momento_expulsao_dois_time_a = None
        quantidade_de_gols_no_momento_expulsao_dois_time_b = None

        ##vitória, derrota ou empate no momento da expulsão referente ao time da casa
        momento_expulsao_um_v_d_e = None
        momento_expulsao_dois_v_d_e = None

        diferenca_gols_expulsao_um = False
        diferenca_gols_expulsao_dois = False
        
        i = 0
        while(i < len(placares_no_momento_da_expulsao)):
            if(i == 0):
                placar_momento_expulsao_um = placares_no_momento_da_expulsao[0]
                expulsao_um_cartao = expulsoes_verificar_cartao[0][1]
                expulsao_um_m_v = expulsoes_verificar_cartao[0][2]

                gols = placar_momento_expulsao_um.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                if(qtd_gols_time_a > qtd_gols_time_b):
                    momento_expulsao_um_v_d_e = 'V'
                elif(qtd_gols_time_a < qtd_gols_time_b):
                    momento_expulsao_um_v_d_e = 'D'
                else:
                    momento_expulsao_um_v_d_e = 'E'

                quantidade_de_gols_no_momento_expulsao_um_time_a = qtd_gols_time_a
                quantidade_de_gols_no_momento_expulsao_um_time_b = qtd_gols_time_b

                diferenca_gols_expulsao_um = qtd_gols_time_a - qtd_gols_time_b

            else:
                placar_momento_expulsao_dois = placares_no_momento_da_expulsao[1]
                expulsao_dois_cartao = expulsoes_verificar_cartao[1][1]
                expulsao_dois_m_v = expulsoes_verificar_cartao[1][2]

                gols = placar_momento_expulsao_dois.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                if(qtd_gols_time_a > qtd_gols_time_b):
                    momento_expulsao_dois_v_d_e = 'V'
                elif(qtd_gols_time_a < qtd_gols_time_b):
                    momento_expulsao_dois_v_d_e = 'D'
                else:
                    momento_expulsao_dois_v_d_e = 'E'

                quantidade_de_gols_no_momento_expulsao_dois_time_a = qtd_gols_time_a
                quantidade_de_gols_no_momento_expulsao_dois_time_b = qtd_gols_time_b

                diferenca_gols_expulsao_dois = qtd_gols_time_a - qtd_gols_time_b
            i+= 1


        ###Modificações
        momento_expulsao_um_v_d_e_V = 0
        if(momento_expulsao_um_v_d_e == 'V'):
            momento_expulsao_um_v_d_e_V = 1

        momento_expulsao_dois_v_d_e_D = 0
        momento_expulsao_dois_v_d_e_E = 0
        momento_expulsao_dois_v_d_e_V = 0

        if(momento_expulsao_dois_v_d_e == 'D'):
            momento_expulsao_dois_v_d_e_D = 1
        elif(momento_expulsao_dois_v_d_e == 'E'):
            momento_expulsao_dois_v_d_e_E = 1
        elif(momento_expulsao_dois_v_d_e == 'V'):
            momento_expulsao_dois_v_d_e_V = 1

        expulsao_um_m_v_Mandante = 0
        if(expulsao_um_m_v == 'Mandante'):
            expulsao_um_m_v_Mandante = 1

        expulsao_dois_m_v_Visitante = 0
        if(expulsao_dois_m_v == 'Visitante'):
            expulsao_dois_m_v_Visitante = 1

        estatisticas = soup.find("table", class_="match_stats_center")

        ##Estatisticas outra aba
        link = link.replace("live", "prelive")
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        estatisticas_aprofundadas = soup.find(id="ultimos_resultados")

        ###Identificar histórico dos últimos 5 jogos do time mandante e visitante
        tabelas_jogos = estatisticas_aprofundadas.find_all("table", class_="stat-last10 stat-half-padding")
        trs = []
        for tabela in tabelas_jogos:
            trs.append(tabela.find_all("tr"))

        ultimos_jogos_time_visitante = trs[1]
        resultados_time_visitante = []

        for i in range(1,6):
            vitoria = ultimos_jogos_time_visitante[i].find(class_="stat-win")
            empate = ultimos_jogos_time_visitante[i].find(class_="stat-draw")
            derrota = ultimos_jogos_time_visitante[i].find(class_="stat-lose")

            if(vitoria):
                resultados_time_visitante.append('V')
            elif(empate):
                resultados_time_visitante.append('E')
            else:
                resultados_time_visitante.append('D')

        quarto_ultimo_jogo_visitante = resultados_time_visitante[3]

        quarto_ultimo_jogo_visitante_V = 0
        if(quarto_ultimo_jogo_visitante == 'V'):
            quarto_ultimo_jogo_visitante_V = 1


        ##Identificar posição atual na tabela do time mandante e visitante
        classificacao = soup.find("table", class_="results competition-rounds competition-half-padding")
        posicao_atual_time_dentro = classificacao.find("tr", {"style":"background-color: #CDDFF0"})
        if(posicao_atual_time_dentro):
            posicao_atual_time_dentro = int(posicao_atual_time_dentro.find("td").get_text().strip())
        else:
            posicao_atual_time_dentro = None

        posicao_atual_time_fora = classificacao.find("tr",{"style":"background-color: #FFE0A6"})
        if(posicao_atual_time_fora):
            posicao_atual_time_fora = int(posicao_atual_time_fora.find("td").get_text().strip())
        else:
            posicao_atual_time_fora = None

        ##Mais algumas estatisticas
        estatist = soup.find("tbody", class_="ajax-container")
        ##CAPTURAR MOMENTO DOS GOLS A PARTIR DAQUI
        estatist = estatist.find_all("table", class_="stat-seqs stat-half-padding")
        estatist_time_casa = estatist[0]
        estatist_time_fora = estatist[1]

        estatist_time_casa = estatist_time_casa.find("tbody")
        estatist_time_casa = estatist_time_casa.find_all("tr")

        estatist_time_fora = estatist_time_fora.find("tbody")
        estatist_time_fora = estatist_time_fora.find_all("tr")

        ### TIME CASA
        medias = []
        for linha in estatist_time_casa:
            tds = linha.find_all("td")
            valores = []
            for td in tds:
                valores.append(td.get_text().strip())
            medias.append(valores)

        if(medias[0][1] != '-'):
            media_gols_marcados_por_jogo_time_casa_em_casa = float(medias[0][1])
        else:
            media_gols_marcados_por_jogo_time_casa_em_casa = float(0)

        if(medias[1][1] != '-'):
            media_gols_sofridos_por_jogo_time_casa_em_casa = float(medias[1][1])
        else:
            media_gols_sofridos_por_jogo_time_casa_em_casa = float(0)

        #### TIME VISITANTE
        medias = []
        for linha in estatist_time_fora:
            tds = linha.find_all("td")
            valores = []
            for td in tds:
                valores.append(td.get_text().strip())
            medias.append(valores)

        if(medias[1][2] != '-'):
            media_gols_sofridos_por_jogo_time_visitante_fora = float(medias[1][2])
        else:
            media_gols_sofridos_por_jogo_time_visitante_fora = float(0)


        estatist = soup.find("tbody", class_="ajax-container")
        estatist_momento_gols = estatist.find_all("table", class_="stat-goals")

        estatist_momento_gols_time_casa = estatist_momento_gols[0]
        estatist_momento_gols_time_fora = estatist_momento_gols[1]

        estatist_momento_gols_time_casa = estatist_momento_gols_time_casa.find("tbody", class_="stat-quarts-padding")
        estatist_momento_gols_time_casa = estatist_momento_gols_time_casa.find_all("tr")

        lista = []
        par = True

        estatist_momento_gols_time_casa.pop()

        lista_momento_gols = []
        lista = []
        for tr in estatist_momento_gols_time_casa:
            if(par):
                gols_marcados = int(tr.find("td", class_="stats-wd-goalstime3").get_text().strip())
                lista.append(gols_marcados)
                par = False
                gols_sofridos = None
            else:
                gols_sofridos = tr.find_all("td")
                gols_sofridos = int(gols_sofridos[1].get_text().strip())
                lista.append(gols_sofridos)
                lista_momento_gols.append(lista)
                lista = []
                gols_marcados = None
                par = True

        gols_marcados_time_casa_segundo_sexto = lista_momento_gols[1][0]

        ########### Visitante

        estatist_momento_gols_time_fora = estatist_momento_gols_time_fora.find("tbody", class_="stat-quarts-padding")
        estatist_momento_gols_time_fora = estatist_momento_gols_time_fora.find_all("tr")

        lista = []
        par = True

        estatist_momento_gols_time_fora.pop()

        lista_momento_gols = []
        lista = []
        for tr in estatist_momento_gols_time_fora:
            if(par):
                gols_marcados = int(tr.find("td", class_="stats-wd-goalstime3").get_text().strip())
                lista.append(gols_marcados)
                par = False
                gols_sofridos = None
            else:
                gols_sofridos = tr.find_all("td")
                gols_sofridos = int(gols_sofridos[1].get_text().strip())
                lista.append(gols_sofridos)
                lista_momento_gols.append(lista)
                lista = []
                gols_marcados = None
                par = True

        gols_marcados_time_visitante_segundo_sexto = lista_momento_gols[1][0]
        gols_sofridos_time_visitante_quinto_sexto = lista_momento_gols[4][1]

        ###
        if(gols_mandante > gols_visitante):
            resultado_final_v_d_e = 'V'
        elif(gols_mandante < gols_visitante):
            resultado_final_v_d_e = 'D'
        else:
            resultado_final_v_d_e = 'E'

        partida = Partida(posicao_atual_time_dentro, posicao_atual_time_fora, media_gols_marcados_por_jogo_time_casa_em_casa, 
        media_gols_sofridos_por_jogo_time_casa_em_casa, media_gols_sofridos_por_jogo_time_visitante_fora, gols_marcados_time_casa_segundo_sexto, 
        gols_marcados_time_visitante_segundo_sexto, gols_sofridos_time_visitante_quinto_sexto, quantidade_de_gols_no_momento_expulsao_um_time_a, 
        minuto_expulsao_um, minuto_expulsao_dois, diferenca_gols_expulsao_um, diferenca_gols_expulsao_dois, expulsao_dois_m_v_Visitante, 
        quarto_ultimo_jogo_visitante_V,momento_expulsao_um_v_d_e_V, expulsao_um_m_v_Mandante, momento_expulsao_dois_v_d_e_D, momento_expulsao_dois_v_d_e_E, momento_expulsao_dois_v_d_e_V, resultado_final_v_d_e)

        print('Ocorreu expulsão')
        
        print('1 atributo')
        print(partida.posicao_time_dentro)
        print('2 atributo')
        print(partida.posicao_time_fora)
        print('3 atributo')
        print(partida.media_gols_marcados_por_jogo_time_casa_em_casa)
        print('4 atributo')
        print(partida.media_gols_sofridos_por_jogo_time_casa_em_casa)
        print('5 atributo')
        print(partida.gols_marcados_time_casa_segundo_sexto)
        print('6 atributo')
        print(partida.media_gols_sofridos_por_jogo_time_visitante_fora)
        print('7 atributo')
        print(partida.gols_marcados_time_visitante_segundo_sexto)
        print('8 atributo')
        print(partida.gols_sofridos_time_visitante_quinto_sexto)
        print('9 atributo')
        print(partida.quarto_ultimo_jogo_visitante_V)
        print('10 atributo')
        print(partida.minuto_expulsao_um)
        print('11 atributo')
        print(partida.minuto_expulsao_dois)
        print('12 atributo')
        print(partida.diferenca_gols_expulsao_um)
        print('13 atributo')
        print(partida.diferenca_gols_expulsao_dois)
        print('14 atributo')
        print(partida.momento_expulsao_um_v_d_e_V)
        print('15 atributo')
        print(partida.expulsao_um_m_v_Mandante)
        print('16 atributo')
        print(partida.momento_expulsao_dois_v_d_e_D)
        print('17 atributo')
        print(partida.momento_expulsao_dois_v_d_e_E)
        print('18 atributo')
        print(partida.momento_expulsao_dois_v_d_e_V)
        print('19 atributo')
        print(partida.quantidade_de_gols_no_momento_expulsao_um_time_a)
        print('20 atributo')
        print(partida.resultado_final_v_d_e)
        
        
        return partida


    else:
        print('Não ocorreu expulsao')
        return False

coleta_dados('https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/fortaleza/atletico-mg/2989208/1/live')