import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana, identificar_minuto_expulsao_segundo_amarelo, identificar_minuto_expulsao_vermelho_direto, verificar_se_teve_expulsao, verifica_tempo_gols, verifica_placares_momentaneos
from classes.Partida import Partida
import datetime

def coleta_dados(link, nome_campeonato, temporada, pais, rodada):
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

    expulsoes_verificar_cartao = []
    ##adiciona atributo de segundo amarelo ou cartão vermelho time a
    if(minutos_expulsoes_time_a):
        for expulsao in minutos_seg_amarelo:
            expulsoes_verificar_cartao.append([expulsao, 'Segundo amarelo'])
        for expulsao in minutos_ver_direto:
            expulsoes_verificar_cartao.append([expulsao, 'Vermelho direto'])

    
    ##TIME B
    minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_b)
    minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_b)
    minutos_expulsoes_time_b = minutos_seg_amarelo + minutos_ver_direto

    ##adiciona atributo de segundo amarelo ou cartão vermelho time b
    if(minutos_expulsoes_time_b):
        for expulsao in minutos_ver_direto:
            expulsoes_verificar_cartao.append([expulsao, 'Vermelho direto'])
        for expulsao in minutos_seg_amarelo:
            expulsoes_verificar_cartao.append([expulsao, 'Segundo amarelo'])

    if(len(expulsoes_verificar_cartao) > 1):
        expulsoes_verificar_cartao = sorted(expulsoes_verificar_cartao, key=lambda x:x[0])

    if(verificar_se_teve_expulsao(minutos_expulsoes_time_a, minutos_expulsoes_time_b)):

        #minutos em que os gols da partida foram realizados
        minutos_gols_time_a = verifica_tempo_gols(time_a)
        minutos_gols_time_b = verifica_tempo_gols(time_b)

        ##qtd de expulsoes
        qtd_expulsoes_time_a = len(minutos_expulsoes_time_a)
        qtd_expulsoes_time_b = len(minutos_expulsoes_time_b)

        ##atributos minuto tempo cada expulsao
        minuto_primeira_expulsao_time_a = None
        minuto_segunda_expulsao_time_a = None
        minuto_terceira_expulsao_time_a = None
        minuto_quarta_expulsao_time_a = None

        minuto_primeira_expulsao_time_b = None
        minuto_segunda_expulsao_time_b = None
        minuto_terceira_expulsao_time_b = None
        minuto_quarta_expulsao_time_b = None

        i = 0
        while(i < qtd_expulsoes_time_a):
            if(i == 0):
                minuto_primeira_expulsao_time_a = minutos_expulsoes_time_a[0]
            elif(i == 1):
                minuto_segunda_expulsao_time_a = minutos_expulsoes_time_a[1]
            elif(i == 2):
                minuto_terceira_expulsao_time_a = minutos_expulsoes_time_a[2]
            else:
                minuto_quarta_expulsao_time_a = minutos_expulsoes_time_a[3]
            i += 1

        i = 0
        while(i < qtd_expulsoes_time_b):
            if(i == 0):
                minuto_primeira_expulsao_time_b = minutos_expulsoes_time_b[0]
            elif(i == 1):
                minuto_segunda_expulsao_time_b = minutos_expulsoes_time_b[1]
            elif(i == 2):
                minuto_terceira_expulsao_time_b = minutos_expulsoes_time_b[2]
            else:
                minuto_quarta_expulsao_time_b = minutos_expulsoes_time_b[3]

            i += 1

        ### Descobrir o placar final do jogo
        resultado_final = dados_gerais_da_partida[1].find(class_="f-score odd").get_text().strip() #resultado final no formato (0-0)
        gols_times = resultado_final.split()

        gols_mandante = int(gols_times[0]) #quantidade de gols do time mandante
        gols_visitante = int(gols_times[2]) #quantidade de gols do time visitante
        ###

        ##placar do jogo no momento da expulsao
        minutos_expulsoes = sorted(minutos_expulsoes_time_a + minutos_expulsoes_time_b)
        placares_no_momento_da_expulsao = verifica_placares_momentaneos(minutos_expulsoes, minutos_gols_time_a, minutos_gols_time_b)

        ##atributos placar do jogo cada expulsao
        placar_momento_expulsao_um = None
        placar_momento_expulsao_dois = None
        placar_momento_expulsao_tres = None
        placar_momento_expulsao_quatro = None
        placar_momento_expulsao_cinco = None
        placar_momento_expulsao_seis = None
        placar_momento_expulsao_sete = None
        placar_momento_expulsao_oito = None

        ##atributos vermelho direto ou segundo amarelo
        expulsao_um_cartao = None
        expulsao_dois_cartao = None
        expulsao_tres_cartao = None
        expulsao_quatro_cartao = None
        expulsao_cinco_cartao = None
        expulsao_seis_cartao = None
        expulsao_sete_cartao = None
        expulsao_oito_cartao = None

        ##quantidade de gols após expulsão
        quantidade_de_gols_apos_expulsao_um_time_a = 0
        quantidade_de_gols_apos_expulsao_um_time_b = 0

        quantidade_de_gols_apos_expulsao_dois_time_a = 0
        quantidade_de_gols_apos_expulsao_dois_time_b = 0

        quantidade_de_gols_apos_expulsao_tres_time_a = 0
        quantidade_de_gols_apos_expulsao_tres_time_b = 0

        quantidade_de_gols_apos_expulsao_quatro_time_a = 0
        quantidade_de_gols_apos_expulsao_quatro_time_b = 0

        quantidade_de_gols_apos_expulsao_cinco_time_a = 0
        quantidade_de_gols_apos_expulsao_cinco_time_b = 0

        quantidade_de_gols_apos_expulsao_seis_time_a = 0
        quantidade_de_gols_apos_expulsao_seis_time_b = 0

        quantidade_de_gols_apos_expulsao_sete_time_a = 0
        quantidade_de_gols_apos_expulsao_sete_time_b = 0

        quantidade_de_gols_apos_expulsao_oito_time_a = 0
        quantidade_de_gols_apos_expulsao_oito_time_b = 0

        i = 0
        while(i < len(placares_no_momento_da_expulsao)):
            if(i == 0):
                placar_momento_expulsao_um = placares_no_momento_da_expulsao[0]
                expulsao_um_cartao = expulsoes_verificar_cartao[0][1]

                gols = placar_momento_expulsao_um.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_um_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_um_time_b = gols_visitante - qtd_gols_time_b

            elif(i == 1):
                placar_momento_expulsao_dois = placares_no_momento_da_expulsao[1]
                expulsao_dois_cartao = expulsoes_verificar_cartao[1][1]

                gols = placar_momento_expulsao_dois.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_dois_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_dois_time_b = gols_visitante - qtd_gols_time_b

            elif(i == 2):
                placar_momento_expulsao_tres = placares_no_momento_da_expulsao[2]
                expulsao_tres_cartao = expulsoes_verificar_cartao[2][1]

                gols = placar_momento_expulsao_tres.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_tres_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_tres_time_b = gols_visitante - qtd_gols_time_b

            elif(i == 3):
                placar_momento_expulsao_quatro = placares_no_momento_da_expulsao[3]
                expulsao_quatro_cartao = expulsoes_verificar_cartao[3][1]

                gols = placar_momento_expulsao_quatro.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_quatro_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_quatro_time_b = gols_visitante - qtd_gols_time_b

            elif(i == 4):
                placar_momento_expulsao_cinco = placares_no_momento_da_expulsao[4]
                expulsao_cinco_cartao = expulsoes_verificar_cartao[4][1]

                gols = placar_momento_expulsao_cinco.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_cinco_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_cinco_time_b = gols_visitante - qtd_gols_time_b
            elif(i == 5):
                placar_momento_expulsao_seis = placares_no_momento_da_expulsao[5]
                expulsao_seis_cartao = expulsoes_verificar_cartao[5][1]

                gols = placar_momento_expulsao_seis.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_seis_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_seis_time_b = gols_visitante - qtd_gols_time_b
            elif(i == 6):
                placar_momento_expulsao_sete = placares_no_momento_da_expulsao[6]
                expulsao_sete_cartao = expulsoes_verificar_cartao[6][1]

                gols = placar_momento_expulsao_sete.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_sete_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_sete_time_b = gols_visitante - qtd_gols_time_b
            else:
                placar_momento_expulsao_oito = placares_no_momento_da_expulsao[7]
                expulsao_oito_cartao = expulsoes_verificar_cartao[7][1]

                gols = placar_momento_expulsao_oito.split('-')
                qtd_gols_time_a = int(gols[0])
                qtd_gols_time_b = int(gols[1])

                quantidade_de_gols_apos_expulsao_oito_time_a = gols_mandante - qtd_gols_time_a
                quantidade_de_gols_apos_expulsao_oito_time_b = gols_visitante - qtd_gols_time_b
            i += 1        

        ### Descobrir time mandante e visitante
        time_dentro = dados_gerais_da_partida[0].find_all("a")
        time_fora = dados_gerais_da_partida[2].find_all("a")

        time_dentro = time_dentro[1].get_text().strip() #TIME MANDANTE
        time_fora = time_fora[1].get_text().strip() #TIME VISITANTE

        ####

        ### Descobrir data do jogo
        data_do_jogo = dados_gerais_da_partida[1].find_all(class_="gamehead")
        data_do_jogo = data_do_jogo[1].get_text().strip() #data do jogo no formato (dia, mês, ano - horário)

        inf_data_do_jogo = data_do_jogo.split()
        dia = int(inf_data_do_jogo[0])
        mes = qualMes(inf_data_do_jogo[1])
        ano = int(inf_data_do_jogo[2])

        horario = inf_data_do_jogo[4]
        horario = horario.split(':')
        horas = int(horario[0])
        minutos = int(horario[1])

        horario = datetime.datetime(ano, mes, dia, horas, minutos) ##Horario

        ##Turno do jogo
        if((horas >= 6) and (horas <= 12)):
            turno = "Dia"
        elif((horas > 12) and (horas < 18)):
            turno = "Tarde"
        else:
            turno = "Noite"

        ##Dia da semana
        dia_semana= dia_da_semana(ano,mes,dia)

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

        vitorias = []
        empates = []
        derrotas = []
        ultimos_jogos_time_casa = trs[0]
        ultimos_jogos_time_visitante = trs[1]


        resultados_time_casa = []
        resultados_time_visitante = []


        for i in range(1,6):
            vitoria = ultimos_jogos_time_casa[i].find(class_="stat-win")
            empate = ultimos_jogos_time_casa[i].find(class_="stat-draw")
            derrota = ultimos_jogos_time_casa[i].find(class_="stat-lose")

            if(vitoria):
                resultados_time_casa.append('V')
            elif(empate):
                resultados_time_casa.append('E')
            else:
                resultados_time_casa.append('D')

        ultimo_jogo_casa = resultados_time_casa[0]
        segundo_ultimo_jogo_casa = resultados_time_casa[1]
        terceiro_ultimo_jogo_casa = resultados_time_casa[2]
        quarto_ultimo_jogo_casa = resultados_time_casa[3]
        quinto_ultimo_jogo_casa = resultados_time_casa[4]

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

        ultimo_jogo_visitante = resultados_time_visitante[0]
        segundo_ultimo_jogo_visitante = resultados_time_visitante[1]
        terceiro_ultimo_jogo_visitante = resultados_time_visitante[2]
        quarto_ultimo_jogo_visitante = resultados_time_visitante[3]
        quinto_ultimo_jogo_visitante = resultados_time_visitante[4]


        ##Identificar posição atual na tabela do time mandante e visitante
        classificacao = soup.find("table", class_="results competition-rounds competition-half-padding")
        posicao_atual_time_dentro = classificacao.find("tr", {"style":"background-color: #CDDFF0"})
        posicao_atual_time_dentro = int(posicao_atual_time_dentro.find("td").get_text().strip())

        posicao_atual_time_fora = classificacao.find("tr",{"style":"background-color: #FFE0A6"})
        posicao_atual_time_fora = int(posicao_atual_time_fora.find("td").get_text().strip())


        ##Identificar odds pré-jogo
        odds = soup.find("table", class_="stats-group odds full odds_MO")
        if(odds):
            odds = odds.find(class_="even")
            odds = odds.find_all(class_="odd-B")

            todas_odds = []
            for odd in odds:
                cotacao = odd.get_text().strip()
                if(cotacao):
                    cotacao = float(cotacao)
                else:
                    cotacao = None
                todas_odds.append(cotacao)

            odd_time_casa = todas_odds[0]
            odd_empate = todas_odds[1]
            odd_time_fora = todas_odds[2]
        else:
            odd_time_casa = None
            odd_empate = None
            odd_time_fora = None

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

        if(medias[0][2] != '-'):
            media_gols_marcados_por_jogo_time_casa_fora = float(medias[0][2])
        else:
            media_gols_marcados_por_jogo_time_casa_fora = float(0)  

        if(medias[0][3] != '-'):
            media_gols_marcados_por_jogo_time_casa_global = float(medias[0][3])
        else:
            media_gols_marcados_por_jogo_time_casa_global = float(0)

        if(medias[1][1] != '-'):
            media_gols_sofridos_por_jogo_time_casa_em_casa = float(medias[1][1])
        else:
            media_gols_sofridos_por_jogo_time_casa_em_casa = float(0)

        if(medias[1][2] != '-'):
            media_gols_sofridos_por_jogo_time_casa_fora = float(medias[1][2])
        else:
            media_gols_sofridos_por_jogo_time_casa_fora = float(0)

        if(medias[1][3] != '-'):
            media_gols_sofridos_por_jogo_time_casa_global = float(medias[1][3])
        else:
            media_gols_sofridos_por_jogo_time_casa_global = float(0)

        if(medias[2][1] != '-'):
            media_gols_marcados_sofridos_por_jogo_time_casa_em_casa = float(medias[2][1])
        else:
            media_gols_marcados_sofridos_por_jogo_time_casa_em_casa = float(0)

        if(medias[2][2] != '-'):
            media_gols_marcados_sofridos_por_jogo_time_casa_fora = float(medias[2][2])
        else:
            media_gols_marcados_sofridos_por_jogo_time_casa_fora = float(0)

        if(medias[2][3] != '-'):
            media_gols_marcados_sofridos_por_jogo_time_casa_global = float(medias[2][3])
        else:
            media_gols_marcados_sofridos_por_jogo_time_casa_global = float(0)

        if(medias[3][1] != '-'):
            jogos_sem_sofrer_gols_time_casa_em_casa = int(medias[3][1].replace("%",'')) / 100
        else:
            jogos_sem_sofrer_gols_time_casa_em_casa = float(0)

        if(medias[3][2] != '-'):
            jogos_sem_sofrer_gols_time_casa_fora = int(medias[3][2].replace("%",'')) / 100
        else:
            jogos_sem_sofrer_gols_time_casa_fora = float(0)

        if(medias[3][3] != '-'):
            jogos_sem_sofrer_gols_time_casa_global = int(medias[3][3].replace("%",'')) / 100
        else:
            jogos_sem_sofrer_gols_time_casa_global = float(0)


        if(medias[4][1] != '-'):
            jogos_sem_marcar_gols_time_casa_em_casa = int(medias[4][1].replace("%",'')) / 100
        else:
            jogos_sem_marcar_gols_time_casa_em_casa = float(0)

        if(medias[4][2] != '-'):
            jogos_sem_marcar_gols_time_casa_fora = int(medias[4][2].replace("%",'')) / 100
        else:
            jogos_sem_marcar_gols_time_casa_fora = float(0)

        if(medias[4][3] != '-'):
            jogos_sem_marcar_gols_time_casa_global = int(medias[4][3].replace("%",'')) / 100
        else:
            jogos_sem_marcar_gols_time_casa_global = float(0)


        if(medias[5][1] != '-'):
            jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa = int(medias[5][1].replace("%",'')) / 100
        else:
            jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa = float(0)

        if(medias[5][2] != '-'):
            jogos_com_mais_de_dois_gols_e_meio_time_casa_fora = int(medias[5][2].replace("%",'')) / 100
        else:
            jogos_com_mais_de_dois_gols_e_meio_time_casa_fora = float(0)

        if(medias[5][3] != '-'):
            jogos_com_mais_de_dois_gols_e_meio_time_casa_global = int(medias[5][3].replace("%",'')) / 100
        else:
            jogos_com_mais_de_dois_gols_e_meio_time_casa_global = float(0)

        if(medias[6][1] != '-'):
            jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa = int(medias[6][1].replace("%",'')) / 100
        else:
            jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa = float(0)

        if(medias[6][2] != '-'):
            jogos_com_menos_de_dois_gols_e_meio_time_casa_fora = int(medias[6][2].replace("%",'')) / 100
        else:
            jogos_com_menos_de_dois_gols_e_meio_time_casa_fora = float(0)

        if(medias[6][3] != '-'):
            jogos_com_menos_de_dois_gols_e_meio_time_casa_global = int(medias[6][3].replace("%",'')) / 100
        else:
            jogos_com_menos_de_dois_gols_e_meio_time_casa_global = float(0)


        #### TIME VISITANTE
        medias = []
        for linha in estatist_time_fora:
            tds = linha.find_all("td")
            valores = []
            for td in tds:
                valores.append(td.get_text().strip())
            medias.append(valores)


        if(medias[0][1] != '-'):
            media_gols_marcados_por_jogo_time_visitante_em_casa = float(medias[0][1])
        else:
            media_gols_marcados_por_jogo_time_visitante_em_casa = float(0)

        if(medias[0][2] != '-'):
            media_gols_marcados_por_jogo_time_visitante_fora = float(medias[0][2])
        else:
            media_gols_marcados_por_jogo_time_visitante_fora = float(0)

        if(medias[0][3] != '-'):
            media_gols_marcados_por_jogo_time_visitante_global = float(medias[0][3])
        else:
            media_gols_marcados_por_jogo_time_visitante_global = float(0)

        if(medias[1][1] != '-'):
            media_gols_sofridos_por_jogo_time_visitante_em_casa = float(medias[1][1])
        else:
            media_gols_sofridos_por_jogo_time_visitante_em_casa = float(0)

        if(medias[1][2] != '-'):
            media_gols_sofridos_por_jogo_time_visitante_fora = float(medias[1][2])
        else:
            media_gols_sofridos_por_jogo_time_visitante_fora = float(0)

        if(medias[1][3] != '-'):
            media_gols_sofridos_por_jogo_time_visitante_global = float(medias[1][3])
        else:
            media_gols_sofridos_por_jogo_time_visitante_global = float(0)

        if(medias[2][1] != '-'):
            media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa = float(medias[2][1])
        else:
            media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa = float(0)

        if(medias[2][2] != '-'):
            media_gols_marcados_sofridos_por_jogo_time_visitante_fora = float(medias[2][2])
        else:
            media_gols_marcados_sofridos_por_jogo_time_visitante_fora = float(0)

        if(medias[2][3] != '-'):
            media_gols_marcados_sofridos_por_jogo_time_visitante_global = float(medias[2][3])
        else:
            media_gols_marcados_sofridos_por_jogo_time_visitante_global = float(0)


        if(medias[3][1] != '-'):
            jogos_sem_sofrer_gols_time_visitante_em_casa = int(medias[3][1].replace("%",'')) / 100
        else:
            jogos_sem_sofrer_gols_time_visitante_em_casa = float(0)

        if(medias[3][2] != '-'):
            jogos_sem_sofrer_gols_time_visitante_fora = int(medias[3][2].replace("%",'')) / 100
        else:
            jogos_sem_sofrer_gols_time_visitante_fora = float(0)

        if(medias[3][3] != '-'):
            jogos_sem_sofrer_gols_time_visitante_global = int(medias[3][3].replace("%",'')) / 100
        else:
            jogos_sem_sofrer_gols_time_visitante_global = float(0)

        if(medias[4][1] != '-'):
            jogos_sem_marcar_gols_time_visitante_em_casa = int(medias[4][1].replace("%",'')) / 100
        else:
            jogos_sem_marcar_gols_time_visitante_em_casa = float(0)

        if(medias[4][2] != '-'):
            jogos_sem_marcar_gols_time_visitante_fora = int(medias[4][2].replace("%",'')) / 100
        else:
            jogos_sem_marcar_gols_time_visitante_fora = float(0)

        if(medias[4][3] != '-'):
            jogos_sem_marcar_gols_time_visitante_global = int(medias[4][3].replace("%",'')) / 100
        else:
            jogos_sem_marcar_gols_time_visitante_global = float(0)


        if(medias[5][1] != '-'):
            jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa = int(medias[5][1].replace("%",'')) / 100
        else:
            jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa = float(0)

        if(medias[5][2] != '-'):
            jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora = int(medias[5][2].replace("%",'')) / 100
        else:
            jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora = float(0)

        if(medias[5][3] != '-'):
            jogos_com_mais_de_dois_gols_e_meio_time_visitante_global = int(medias[5][3].replace("%",'')) / 100
        else:
            jogos_com_mais_de_dois_gols_e_meio_time_visitante_global = float(0)

        if(medias[6][1] != '-'):
            jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa = int(medias[6][1].replace("%",'')) / 100
        else:
            jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa = float(0)

        if(medias[6][2] != '-'):
            jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora = int(medias[6][2].replace("%",'')) / 100
        else:
            jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora = float(0)

        if(medias[6][3] != '-'):
            jogos_com_menos_de_dois_gols_e_meio_time_visitante_global = int(medias[6][3].replace("%",'')) / 100
        else:
            jogos_com_menos_de_dois_gols_e_meio_time_visitante_global = float(0)


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

        gols_marcados_time_casa_primeiro_sexto = lista_momento_gols[0][0]
        gols_marcados_time_casa_segundo_sexto = lista_momento_gols[1][0]
        gols_marcados_time_casa_terceiro_sexto = lista_momento_gols[2][0]
        gols_marcados_time_casa_quarto_sexto = lista_momento_gols[3][0]
        gols_marcados_time_casa_quinto_sexto = lista_momento_gols[4][0]
        gols_marcados_time_casa_ultimo_sexto = lista_momento_gols[5][0]


        gols_sofridos_time_casa_primeiro_sexto = lista_momento_gols[0][1]
        gols_sofridos_time_casa_segundo_sexto = lista_momento_gols[1][1]
        gols_sofridos_time_casa_terceiro_sexto = lista_momento_gols[2][1]
        gols_sofridos_time_casa_quarto_sexto = lista_momento_gols[3][1]
        gols_sofridos_time_casa_quinto_sexto = lista_momento_gols[4][1]
        gols_sofridos_time_casa_ultimo_sexto = lista_momento_gols[5][1]


        ################### Visitante

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


        gols_marcados_time_visitante_primeiro_sexto = lista_momento_gols[0][0]
        gols_marcados_time_visitante_segundo_sexto = lista_momento_gols[1][0]
        gols_marcados_time_visitante_terceiro_sexto = lista_momento_gols[2][0]
        gols_marcados_time_visitante_quarto_sexto = lista_momento_gols[3][0]
        gols_marcados_time_visitante_quinto_sexto = lista_momento_gols[4][0]
        gols_marcados_time_visitante_ultimo_sexto = lista_momento_gols[5][0]

        gols_sofridos_time_visitante_primeiro_sexto = lista_momento_gols[0][1]
        gols_sofridos_time_visitante_segundo_sexto = lista_momento_gols[1][1]
        gols_sofridos_time_visitante_terceiro_sexto = lista_momento_gols[2][1]
        gols_sofridos_time_visitante_quarto_sexto = lista_momento_gols[3][1]
        gols_sofridos_time_visitante_quinto_sexto = lista_momento_gols[4][1]
        gols_sofridos_time_visitante_ultimo_sexto = lista_momento_gols[5][1]

        '''
        estatisticas = soup.find("table", class_="match_stats_center")

        ##Posse de bola
        posse = estatisticas.find("tr", class_="possession")
        if(posse):
            posse_time_a = (int(posse.find("td", class_="stat_value_number_team_A").get_text().strip().replace("%",''))) / 100
            posse_time_b = (int(posse.find("td", class_="stat_value_number_team_B").get_text().strip().replace("%",''))) / 100
        else:
            posse_time_a = None
            posse_time_b = None

        ##Chutes a gol
        chutes_a_gol = estatisticas.find("tr", class_="shots_on_target")
        if(chutes_a_gol):
            chutes_a_gol_time_a = int(chutes_a_gol.find("td", class_="stat_value_number_team_A").get_text().strip())
            chutes_a_gol_time_b = int(chutes_a_gol.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            chutes_a_gol_time_a = None
            chutes_a_gol_time_b = None

        ##Chutes fora
        #shots_off_target
        chutes_fora = estatisticas.find("tr", class_="shots_off_target")
        if(chutes_fora):
            chutes_fora_time_a = int(chutes_fora.find("td", class_="stat_value_number_team_A").get_text().strip())
            chutes_fora_time_b = int(chutes_fora.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            chutes_fora_time_a = None
            chutes_fora_time_b = None

        ##Ataques
        #attacks
        ataques = estatisticas.find("tr", class_="attacks")
        if(ataques):
            ataques_time_a = int(ataques.find("td", class_="stat_value_number_team_A").get_text().strip())
            ataques_time_b = int(ataques.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            ataques_time_a = None
            ataques_time_b = None

        ##Ataques perigosos
        #dangerous_attacks
        ataques_perigosos = estatisticas.find("tr", class_="dangerous_attacks")
        if(ataques_perigosos):
            ataques_perigosos_time_a = int(ataques_perigosos.find("td", class_="stat_value_number_team_A").get_text().strip())
            ataques_perigosos_time_b = int(ataques_perigosos.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            ataques_perigosos_time_a = None
            ataques_perigosos_time_b = None

        ##Impedimentos
        #offsides
        impedimentos = estatisticas.find("tr", class_="offsides")
        if(impedimentos):
            impedimentos_time_a = int(impedimentos.find("td", class_="stat_value_number_team_A").get_text().strip())
            impedimentos_time_b = int(impedimentos.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            impedimentos_time_a = None
            impedimentos_time_b = None

        ##Faltas
        #fouls
        faltas = estatisticas.find("tr", class_="fouls")
        if(faltas):
            faltas_time_a = int(faltas.find("td", class_="stat_value_number_team_A").get_text().strip())
            faltas_time_b = int(faltas.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            faltas_time_a = None
            faltas_time_b = None

        ##Escanteios
        #corners
        escanteios = estatisticas.find("tr", class_="corners")
        if(escanteios):
            escanteios_time_a = int(escanteios.find("td", class_="stat_value_number_team_A").get_text().strip())
            escanteios_time_b = int(escanteios.find("td", class_="stat_value_number_team_B").get_text().strip())
        else:
            escanteios_time_a = None
            escanteios_time_b = None

        '''

        print('Ocorreu expulsão')
        partida = Partida(nome_campeonato, temporada, pais, rodada,
            time_dentro, time_fora, resultado_final, gols_mandante, gols_visitante, horario, turno, dia_semana,
            posicao_atual_time_dentro, posicao_atual_time_fora,
            ultimo_jogo_casa, segundo_ultimo_jogo_casa, terceiro_ultimo_jogo_casa, quarto_ultimo_jogo_casa, quinto_ultimo_jogo_casa, ultimo_jogo_visitante, segundo_ultimo_jogo_visitante, terceiro_ultimo_jogo_visitante, quarto_ultimo_jogo_visitante, quinto_ultimo_jogo_visitante,
            media_gols_marcados_por_jogo_time_casa_em_casa, media_gols_marcados_por_jogo_time_casa_fora, media_gols_marcados_por_jogo_time_casa_global, media_gols_sofridos_por_jogo_time_casa_em_casa, media_gols_sofridos_por_jogo_time_casa_fora, media_gols_sofridos_por_jogo_time_casa_global, media_gols_marcados_sofridos_por_jogo_time_casa_em_casa, media_gols_marcados_sofridos_por_jogo_time_casa_fora, media_gols_marcados_sofridos_por_jogo_time_casa_global, jogos_sem_sofrer_gols_time_casa_em_casa, jogos_sem_sofrer_gols_time_casa_fora, jogos_sem_sofrer_gols_time_casa_global, jogos_sem_marcar_gols_time_casa_em_casa, jogos_sem_marcar_gols_time_casa_fora, jogos_sem_marcar_gols_time_casa_global, jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa, jogos_com_mais_de_dois_gols_e_meio_time_casa_fora, jogos_com_mais_de_dois_gols_e_meio_time_casa_global, jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa, jogos_com_menos_de_dois_gols_e_meio_time_casa_fora, jogos_com_menos_de_dois_gols_e_meio_time_casa_global,
            media_gols_marcados_por_jogo_time_visitante_em_casa, media_gols_marcados_por_jogo_time_visitante_fora, media_gols_marcados_por_jogo_time_visitante_global, media_gols_sofridos_por_jogo_time_visitante_em_casa, media_gols_sofridos_por_jogo_time_visitante_fora, media_gols_sofridos_por_jogo_time_visitante_global, media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa, media_gols_marcados_sofridos_por_jogo_time_visitante_fora, media_gols_marcados_sofridos_por_jogo_time_visitante_global, jogos_sem_sofrer_gols_time_visitante_em_casa, jogos_sem_sofrer_gols_time_visitante_fora,jogos_sem_sofrer_gols_time_visitante_global, jogos_sem_marcar_gols_time_visitante_em_casa, jogos_sem_marcar_gols_time_visitante_fora, jogos_sem_marcar_gols_time_visitante_global,jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa, jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora, jogos_com_mais_de_dois_gols_e_meio_time_visitante_global, jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa, jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora, jogos_com_menos_de_dois_gols_e_meio_time_visitante_global,
            gols_marcados_time_casa_primeiro_sexto, gols_sofridos_time_casa_primeiro_sexto, gols_marcados_time_casa_segundo_sexto, gols_sofridos_time_casa_segundo_sexto, gols_marcados_time_casa_terceiro_sexto, gols_sofridos_time_casa_terceiro_sexto, gols_marcados_time_casa_quarto_sexto, gols_sofridos_time_casa_quarto_sexto, gols_marcados_time_casa_quinto_sexto, gols_sofridos_time_casa_quinto_sexto, gols_marcados_time_casa_ultimo_sexto, gols_sofridos_time_casa_ultimo_sexto,
            gols_marcados_time_visitante_primeiro_sexto, gols_sofridos_time_visitante_primeiro_sexto, gols_marcados_time_visitante_segundo_sexto, gols_sofridos_time_visitante_segundo_sexto, gols_marcados_time_visitante_terceiro_sexto, gols_sofridos_time_visitante_terceiro_sexto, gols_marcados_time_visitante_quarto_sexto, gols_sofridos_time_visitante_quarto_sexto, gols_marcados_time_visitante_quinto_sexto, gols_sofridos_time_visitante_quinto_sexto, gols_marcados_time_visitante_ultimo_sexto, gols_sofridos_time_visitante_ultimo_sexto,
            minuto_primeira_expulsao_time_a, minuto_segunda_expulsao_time_a, minuto_terceira_expulsao_time_a,minuto_quarta_expulsao_time_a, minuto_primeira_expulsao_time_b, minuto_segunda_expulsao_time_b, minuto_terceira_expulsao_time_b, minuto_quarta_expulsao_time_b,
            placar_momento_expulsao_um, placar_momento_expulsao_dois, placar_momento_expulsao_tres, placar_momento_expulsao_quatro, placar_momento_expulsao_cinco, placar_momento_expulsao_seis, placar_momento_expulsao_sete, placar_momento_expulsao_oito,
            expulsao_um_cartao, expulsao_dois_cartao, expulsao_tres_cartao, expulsao_quatro_cartao, expulsao_cinco_cartao, expulsao_seis_cartao, expulsao_sete_cartao, expulsao_oito_cartao,
            quantidade_de_gols_apos_expulsao_um_time_a, quantidade_de_gols_apos_expulsao_um_time_b, quantidade_de_gols_apos_expulsao_dois_time_a, quantidade_de_gols_apos_expulsao_dois_time_b, quantidade_de_gols_apos_expulsao_tres_time_a, quantidade_de_gols_apos_expulsao_tres_time_b, quantidade_de_gols_apos_expulsao_quatro_time_a, quantidade_de_gols_apos_expulsao_quatro_time_b, quantidade_de_gols_apos_expulsao_cinco_time_a, quantidade_de_gols_apos_expulsao_cinco_time_b, quantidade_de_gols_apos_expulsao_seis_time_a, quantidade_de_gols_apos_expulsao_seis_time_b, quantidade_de_gols_apos_expulsao_sete_time_a, quantidade_de_gols_apos_expulsao_sete_time_b, quantidade_de_gols_apos_expulsao_oito_time_a, quantidade_de_gols_apos_expulsao_oito_time_b,
            qtd_expulsoes_time_a, qtd_expulsoes_time_b)

        print(partida)
    else:
        print('Não ocorreu expulsao')

#coleta_dados('https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/csa/chapecoense/2989095/1/live')

'''

    #dados basicos
    print(time_dentro)
    print(time_fora)
    print(resultado_final)
    print(gols_mandante)
    print(gols_visitante)
    print(data_do_jogo)
    print(horario)
    print(turno)
    print(dia_semana)

    #histórico últimos 5 jogos
    print(ultimo_jogo_casa)
    print(segundo_ultimo_jogo_casa)
    print(terceiro_ultimo_jogo_casa)
    print(quarto_ultimo_jogo_casa)
    print(quinto_ultimo_jogo_casa)

    print(ultimo_jogo_visitante)
    print(segundo_ultimo_jogo_visitante)
    print(terceiro_ultimo_jogo_visitante)
    print(quarto_ultimo_jogo_visitante)
    print(quinto_ultimo_jogo_visitante)

    #posição atual na tabela
    print(posicao_atual_time_dentro)
    print(posicao_atual_time_fora)

    #cotação média em casa de apostas pré-jogo
    print(odd_time_casa)
    print(odd_empate)
    print(odd_time_fora)

    #estatísticas aprofundadas
    print(media_gols_marcados_por_jogo_time_casa_em_casa)
    print(media_gols_marcados_por_jogo_time_casa_fora)
    print(media_gols_marcados_por_jogo_time_casa_global)
    print(media_gols_sofridos_por_jogo_time_casa_em_casa)
    print(media_gols_sofridos_por_jogo_time_casa_fora )
    print(media_gols_sofridos_por_jogo_time_casa_global)
    print(media_gols_marcados_sofridos_por_jogo_time_casa_em_casa)
    print(media_gols_marcados_sofridos_por_jogo_time_casa_fora)
    print(media_gols_marcados_sofridos_por_jogo_time_casa_global)

    print(jogos_sem_sofrer_gols_time_casa_em_casa)
    print(jogos_sem_sofrer_gols_time_casa_fora)
    print(jogos_sem_sofrer_gols_time_casa_global)
    print(jogos_sem_marcar_gols_time_casa_em_casa)
    print(jogos_sem_marcar_gols_time_casa_fora)
    print(jogos_sem_marcar_gols_time_casa_global)
    print(jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa)
    print(jogos_com_mais_de_dois_gols_e_meio_time_casa_fora)
    print(jogos_com_mais_de_dois_gols_e_meio_time_casa_global)
    print(jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa)
    print(jogos_com_menos_de_dois_gols_e_meio_time_casa_fora)
    print(jogos_com_menos_de_dois_gols_e_meio_time_casa_global)

    print(media_gols_marcados_por_jogo_time_visitante_em_casa)
    print(media_gols_marcados_por_jogo_time_visitante_fora)
    print(media_gols_marcados_por_jogo_time_visitante_global)
    print(media_gols_sofridos_por_jogo_time_visitante_em_casa)
    print(media_gols_sofridos_por_jogo_time_visitante_fora )
    print(media_gols_sofridos_por_jogo_time_visitante_global)
    print(media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa)
    print(media_gols_marcados_sofridos_por_jogo_time_visitante_fora)
    print(media_gols_marcados_sofridos_por_jogo_time_visitante_global)
    print(jogos_sem_sofrer_gols_time_visitante_em_casa)
    print(jogos_sem_sofrer_gols_time_visitante_fora)
    print(jogos_sem_sofrer_gols_time_visitante_global)
    print(jogos_sem_marcar_gols_time_visitante_em_casa)
    print(jogos_sem_marcar_gols_time_visitante_fora)
    print(jogos_sem_marcar_gols_time_visitante_global)
    print(jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa)
    print(jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora)
    print(jogos_com_mais_de_dois_gols_e_meio_time_visitante_global)
    print(jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa)
    print(jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora)
    print(jogos_com_menos_de_dois_gols_e_meio_time_visitante_global)

    print(gols_marcados_time_casa_primeiro_sexto)
    print(gols_sofridos_time_casa_primeiro_sexto) 
    print(gols_marcados_time_casa_segundo_sexto)
    print(gols_sofridos_time_casa_segundo_sexto)
    print(gols_marcados_time_casa_terceiro_sexto)
    print(gols_sofridos_time_casa_terceiro_sexto)
    print(gols_marcados_time_casa_quarto_sexto)
    print(gols_sofridos_time_casa_quarto_sexto)
    print(gols_marcados_time_casa_quinto_sexto)
    print(gols_sofridos_time_casa_quinto_sexto)
    print(gols_marcados_time_casa_ultimo_sexto)
    print(gols_sofridos_time_casa_ultimo_sexto)

    print(gols_marcados_time_visitante_primeiro_sexto)
    print(gols_sofridos_time_visitante_primeiro_sexto) 
    print(gols_marcados_time_visitante_segundo_sexto)
    print(gols_sofridos_time_visitante_segundo_sexto)
    print(gols_marcados_time_visitante_terceiro_sexto)
    print(gols_sofridos_time_visitante_terceiro_sexto)
    print(gols_marcados_time_visitante_quarto_sexto)
    print(gols_sofridos_time_visitante_quarto_sexto)
    print(gols_marcados_time_visitante_quinto_sexto)
    print(gols_sofridos_time_visitante_quinto_sexto)
    print(gols_marcados_time_visitante_ultimo_sexto)
    print(gols_sofridos_time_visitante_ultimo_sexto)

    ##dados relacionados a expulsao
    print(minuto_primeira_expulsao_time_a)
    print(minuto_segunda_expulsao_time_a)
    print(minuto_terceira_expulsao_time_a)
    print(minuto_quarta_expulsao_time_a)
    print(minuto_primeira_expulsao_time_b)
    print(minuto_segunda_expulsao_time_b)
    print(minuto_terceira_expulsao_time_b)
    print(minuto_quarta_expulsao_time_b)

    print(placar_momento_expulsao_um)
    print(placar_momento_expulsao_dois)
    print(placar_momento_expulsao_tres)
    print(placar_momento_expulsao_quatro)
    print(placar_momento_expulsao_cinco)
    print(placar_momento_expulsao_seis)
    print(placar_momento_expulsao_sete)
    print(placar_momento_expulsao_oito)

    print(expulsao_um_cartao)
    print(expulsao_dois_cartao)
    print(expulsao_tres_cartao)
    print(expulsao_quatro_cartao)
    print(expulsao_cinco_cartao)
    print(expulsao_seis_cartao)
    print(expulsao_sete_cartao)
    print(expulsao_oito_cartao)

    print(quantidade_de_gols_apos_expulsao_um_time_a)
    print(quantidade_de_gols_apos_expulsao_um_time_b)
    print(quantidade_de_gols_apos_expulsao_dois_time_a)
    print(quantidade_de_gols_apos_expulsao_dois_time_b)
    print(quantidade_de_gols_apos_expulsao_tres_time_a)
    print(quantidade_de_gols_apos_expulsao_tres_time_b)
    print(quantidade_de_gols_apos_expulsao_quatro_time_a)
    print(quantidade_de_gols_apos_expulsao_quatro_time_b)
    print(quantidade_de_gols_apos_expulsao_cinco_time_a)
    print(quantidade_de_gols_apos_expulsao_cinco_time_b)
    print(quantidade_de_gols_apos_expulsao_seis_time_a)
    print(quantidade_de_gols_apos_expulsao_seis_time_b)
    print(quantidade_de_gols_apos_expulsao_sete_time_a)
    print(quantidade_de_gols_apos_expulsao_sete_time_b)
    print(quantidade_de_gols_apos_expulsao_oito_time_a)
    print(quantidade_de_gols_apos_expulsao_oito_time_b)

    print(qtd_expulsoes_time_a)
    print(qtd_expulsoes_time_b)

    #estatisticas que não estão sendo utilizadas momentaneamente
    print(posse_time_a)
    print(posse_time_b)
    print(chutes_a_gol_time_a)
    print(chutes_a_gol_time_b)
    print(chutes_fora_time_a)
    print(chutes_fora_time_b)
    print(ataques_time_a)
    print(ataques_time_b)
    print(ataques_perigosos_time_a)
    print(ataques_perigosos_time_b)
    print(impedimentos_time_a)
    print(impedimentos_time_b)
    print(faltas_time_a)
    print(faltas_time_b)
    print(escanteios_time_a)
    print(escanteios_time_b)
    '''