import requests
from bs4 import BeautifulSoup

import csv

from dados_da_partida import coleta_dados
from classes.Partida import Partida


##escrita arquivo
f = open('Jupyter/campeonato_italiano_5.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(( 'nome_campeonato', 'temporada', 'pais', 'rodada',
    'time_dentro', 'time_fora', 'resultado_final', 'resultado_final_v_d_e','gols_mandante', 'gols_visitante', 'horario', 'turno', 'dia_semana',
    'posicao_time_dentro', 'posicao_time_fora',
    'ultimo_jogo_casa', 'segundo_ultimo_jogo_casa', 'terceiro_ultimo_jogo_casa', 'quarto_ultimo_jogo_casa', 'quinto_ultimo_jogo_casa', 'ultimo_jogo_visitante', 'segundo_ultimo_jogo_visitante', 'terceiro_ultimo_jogo_visitante', 'quarto_ultimo_jogo_visitante', 'quinto_ultimo_jogo_visitante',
    'media_gols_marcados_por_jogo_time_casa_em_casa', 'media_gols_marcados_por_jogo_time_casa_fora', 'media_gols_marcados_por_jogo_time_casa_global', 'media_gols_sofridos_por_jogo_time_casa_em_casa', 'media_gols_sofridos_por_jogo_time_casa_fora', 'media_gols_sofridos_por_jogo_time_casa_global', 'media_gols_marcados_sofridos_por_jogo_time_casa_em_casa', 'media_gols_marcados_sofridos_por_jogo_time_casa_fora', 'media_gols_marcados_sofridos_por_jogo_time_casa_global', 'jogos_sem_sofrer_gols_time_casa_em_casa', 'jogos_sem_sofrer_gols_time_casa_fora', 'jogos_sem_sofrer_gols_time_casa_global', 'jogos_sem_marcar_gols_time_casa_em_casa', 'jogos_sem_marcar_gols_time_casa_fora', 'jogos_sem_marcar_gols_time_casa_global', 'jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa', 'jogos_com_mais_de_dois_gols_e_meio_time_casa_fora', 'jogos_com_mais_de_dois_gols_e_meio_time_casa_global', 'jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa', 'jogos_com_menos_de_dois_gols_e_meio_time_casa_fora', 'jogos_com_menos_de_dois_gols_e_meio_time_casa_global',
    'media_gols_marcados_por_jogo_time_visitante_em_casa', 'media_gols_marcados_por_jogo_time_visitante_fora', 'media_gols_marcados_por_jogo_time_visitante_global', 'media_gols_sofridos_por_jogo_time_visitante_em_casa', 'media_gols_sofridos_por_jogo_time_visitante_fora', 'media_gols_sofridos_por_jogo_time_visitante_global', 'media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa', 'media_gols_marcados_sofridos_por_jogo_time_visitante_fora', 'media_gols_marcados_sofridos_por_jogo_time_visitante_global', 'jogos_sem_sofrer_gols_time_visitante_em_casa', 'jogos_sem_sofrer_gols_time_visitante_fora','jogos_sem_sofrer_gols_time_visitante_global', 'jogos_sem_marcar_gols_time_visitante_em_casa', 'jogos_sem_marcar_gols_time_visitante_fora', 'jogos_sem_marcar_gols_time_visitante_global','jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa', 'jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora', 'jogos_com_mais_de_dois_gols_e_meio_time_visitante_global', 'jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa', 'jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora', 'jogos_com_menos_de_dois_gols_e_meio_time_visitante_global',
    'gols_marcados_time_casa_primeiro_sexto', 'gols_sofridos_time_casa_primeiro_sexto', 'gols_marcados_time_casa_segundo_sexto', 'gols_sofridos_time_casa_segundo_sexto', 'gols_marcados_time_casa_terceiro_sexto', 'gols_sofridos_time_casa_terceiro_sexto', 'gols_marcados_time_casa_quarto_sexto', 'gols_sofridos_time_casa_quarto_sexto', 'gols_marcados_time_casa_quinto_sexto', 'gols_sofridos_time_casa_quinto_sexto', 'gols_marcados_time_casa_ultimo_sexto', 'gols_sofridos_time_casa_ultimo_sexto',
    'gols_marcados_time_visitante_primeiro_sexto', 'gols_sofridos_time_visitante_primeiro_sexto', 'gols_marcados_time_visitante_segundo_sexto', 'gols_sofridos_time_visitante_segundo_sexto', 'gols_marcados_time_visitante_terceiro_sexto', 'gols_sofridos_time_visitante_terceiro_sexto', 'gols_marcados_time_visitante_quarto_sexto', 'gols_sofridos_time_visitante_quarto_sexto', 'gols_marcados_time_visitante_quinto_sexto', 'gols_sofridos_time_visitante_quinto_sexto', 'gols_marcados_time_visitante_ultimo_sexto', 'gols_sofridos_time_visitante_ultimo_sexto',
    'minuto_primeira_expulsao_time_a', 'minuto_segunda_expulsao_time_a', 'minuto_terceira_expulsao_time_a','minuto_quarta_expulsao_time_a', 'minuto_primeira_expulsao_time_b', 'minuto_segunda_expulsao_time_b', 'minuto_terceira_expulsao_time_b', 'minuto_quarta_expulsao_time_b',
    'placar_momento_expulsao_um', 'placar_momento_expulsao_dois', 'placar_momento_expulsao_tres', 'placar_momento_expulsao_quatro', 'placar_momento_expulsao_cinco', 'placar_momento_expulsao_seis', 'placar_momento_expulsao_sete', 'placar_momento_expulsao_oito',
    'expulsao_um_cartao', 'expulsao_dois_cartao', 'expulsao_tres_cartao', 'expulsao_quatro_cartao', 'expulsao_cinco_cartao', 'expulsao_seis_cartao', 'expulsao_sete_cartao', 'expulsao_oito_cartao',
    'quantidade_de_gols_apos_expulsao_um_time_a', 'quantidade_de_gols_apos_expulsao_um_time_b', 'quantidade_de_gols_apos_expulsao_dois_time_a', 'quantidade_de_gols_apos_expulsao_dois_time_b', 'quantidade_de_gols_apos_expulsao_tres_time_a', 'quantidade_de_gols_apos_expulsao_tres_time_b', 'quantidade_de_gols_apos_expulsao_quatro_time_a', 'quantidade_de_gols_apos_expulsao_quatro_time_b', 'quantidade_de_gols_apos_expulsao_cinco_time_a', 'quantidade_de_gols_apos_expulsao_cinco_time_b', 'quantidade_de_gols_apos_expulsao_seis_time_a', 'quantidade_de_gols_apos_expulsao_seis_time_b', 'quantidade_de_gols_apos_expulsao_sete_time_a', 'quantidade_de_gols_apos_expulsao_sete_time_b', 'quantidade_de_gols_apos_expulsao_oito_time_a', 'quantidade_de_gols_apos_expulsao_oito_time_b',
    'quantidade_de_gols_no_momento_expulsao_um_time_a', 'quantidade_de_gols_no_momento_expulsao_um_time_b', 'quantidade_de_gols_no_momento_expulsao_dois_time_a', 'quantidade_de_gols_no_momento_expulsao_dois_time_b', 'quantidade_de_gols_no_momento_expulsao_tres_time_a', 'quantidade_de_gols_no_momento_expulsao_tres_time_b', 'quantidade_de_gols_no_momento_expulsao_quatro_time_a', 'quantidade_de_gols_no_momento_expulsao_quatro_time_b', 'quantidade_de_gols_no_momento_expulsao_cinco_time_a', 'quantidade_de_gols_no_momento_expulsao_cinco_time_b', 'quantidade_de_gols_no_momento_expulsao_seis_time_a', 'quantidade_de_gols_no_momento_expulsao_seis_time_b', 'quantidade_de_gols_no_momento_expulsao_sete_time_a', 'quantidade_de_gols_no_momento_expulsao_sete_time_b', 'quantidade_de_gols_no_momento_expulsao_oito_time_a', 'quantidade_de_gols_no_momento_expulsao_oito_time_b',
    'intervalo_expulsao_um_v_d_e', 'intervalo_expulsao_dois_v_d_e', 'intervalo_expulsao_tres_v_d_e', 'intervalo_expulsao_quatro_v_d_e', 'intervalo_expulsao_cinco_v_d_e', 'intervalo_expulsao_seis_v_d_e', 'intervalo_expulsao_sete_v_d_e', 'intervalo_expulsao_oito_v_d_e',
    'momento_expulsao_um_v_d_e', 'momento_expulsao_dois_v_d_e', 'momento_expulsao_tres_v_d_e', 'momento_expulsao_quatro_v_d_e', 'momento_expulsao_cinco_v_d_e', 'momento_expulsao_seis_v_d_e', 'momento_expulsao_sete_v_d_e', 'momento_expulsao_oito_v_d_e',
    'expulsao_um_m_v', 'expulsao_dois_m_v', 'expulsao_tres_m_v', 'expulsao_quatro_m_v', 'expulsao_cinco_m_v', 'expulsao_seis_m_v', 'expulsao_sete_m_v', 'expulsao_oito_m_v',
    'qtd_expulsoes_time_a', 'qtd_expulsoes_time_b',
    'posse_time_a', 'posse_time_b', 'chutes_a_gol_time_a', 'chutes_a_gol_time_b', 'chutes_fora_time_a', 'chutes_fora_time_b', 'ataques_time_a', 'ataques_time_b', 'ataques_perigosos_time_a', 'ataques_perigosos_time_b', 'impedimentos_time_a', 'impedimentos_time_b', 'faltas_time_a', 'faltas_time_b', 'escanteios_time_a', 'escanteios_time_b'))

    link_inicial = "https://www.academiadasapostasbrasil.com/stats/competition/italia-stats/13"

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
    del links_temporadas[0:12]

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
            
            if(l == "/2272"):
                
                del rodadas_do_ano[0:28]
                print("deletei")
            else:
                print("nao deletei")
            
            
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
                    partida = coleta_dados(link, nome_campeonato, temporada, pais, rodada_atual)
                    
                    
                    if(partida):
                        writer.writerow((partida.nome_campeonato, partida.temporada, partida.pais, partida.rodada,
                            partida.time_mandante, partida.time_visitante, partida.resultado_final, partida.resultado_final_v_d_e, partida.gols_mandante, partida.gols_visitante, partida.horario, partida.turno, partida.dia_da_semana,
                            partida.posicao_atual_na_tabela_time_mandante, partida.posicao_atual_na_tabela_time_visitante,
                            partida.ultimo_jogo_time_mandante, partida.segundo_ultimo_jogo_time_mandante, partida.terceiro_ultimo_jogo_time_mandante, partida.quarto_ultimo_jogo_time_mandante, partida.quinto_ultimo_jogo_time_mandante, partida.ultimo_jogo_time_visitante, partida.segundo_ultimo_jogo_time_visitante, partida.terceiro_ultimo_jogo_time_visitante, partida.quarto_ultimo_jogo_time_visitante, partida.quinto_ultimo_jogo_time_visitante,
                            partida.media_gols_marcados_por_jogo_time_mandante_em_casa, partida.media_gols_marcados_por_jogo_time_mandante_fora, partida.media_gols_marcados_por_jogo_time_mandante_global, partida.media_gols_sofridos_por_jogo_time_mandante_em_casa, partida.media_gols_sofridos_por_jogo_time_mandante_fora, partida.media_gols_sofridos_por_jogo_time_mandante_global, partida.media_gols_marcados_e_sofridos_por_jogo_time_mandante_em_casa, partida.media_gols_marcados_e_sofridos_por_jogo_time_mandante_fora, partida.media_gols_marcados_e_sofridos_por_jogo_time_mandante_global, partida.jogos_sem_sofrer_gols_time_mandante_em_casa, partida.jogos_sem_sofrer_gols_time_mandante_fora, partida.jogos_sem_sofrer_gols_time_mandante_global, partida.jogos_sem_marcar_gols_time_mandante_em_casa, partida.jogos_sem_marcar_gols_time_mandante_fora, partida.jogos_sem_marcar_gols_time_mandante_global, partida.jogos_com_mais_de_dois_gols_e_meio_time_mandante_em_casa, partida.jogos_com_mais_de_dois_gols_e_meio_time_mandante_fora, partida.jogos_com_mais_de_dois_gols_e_meio_time_mandante_global, partida.jogos_com_menos_de_dois_gols_e_meio_time_mandante_em_casa, partida.jogos_com_menos_de_dois_gols_e_meio_time_mandante_fora, partida.jogos_com_menos_de_dois_gols_e_meio_time_mandante_global,
                            partida.media_gols_marcados_por_jogo_time_visitante_em_casa, partida.media_gols_marcados_por_jogo_time_visitante_fora, partida.media_gols_marcados_por_jogo_time_visitante_global, partida.media_gols_sofridos_por_jogo_time_visitante_em_casa, partida.media_gols_sofridos_por_jogo_time_visitante_fora, partida.media_gols_sofridos_por_jogo_time_visitante_global, partida.media_gols_marcados_e_sofridos_por_jogo_time_visitante_em_casa, partida.media_gols_marcados_e_sofridos_por_jogo_time_visitante_fora, partida.media_gols_marcados_e_sofridos_por_jogo_time_visitante_global, partida.jogos_sem_sofrer_gols_time_visitante_em_casa, partida.jogos_sem_sofrer_gols_time_visitante_fora, partida.jogos_sem_sofrer_gols_time_visitante_global, partida.jogos_sem_marcar_gols_time_visitante_em_casa, partida.jogos_sem_marcar_gols_time_visitante_fora, partida.jogos_sem_marcar_gols_time_visitante_global, partida.jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa, partida.jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora, partida.jogos_com_mais_de_dois_gols_e_meio_time_visitante_global, partida.jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa, partida.jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora, partida.jogos_com_menos_de_dois_gols_e_meio_time_visitante_global,
                            partida.gols_marcados_time_mandante_primeiro_sexto, partida.gols_sofridos_time_mandante_primeiro_sexto, partida.gols_marcados_time_mandante_segundo_sexto, partida.gols_sofridos_time_mandante_segundo_sexto, partida.gols_marcados_time_mandante_terceiro_sexto, partida.gols_sofridos_time_mandante_terceiro_sexto, partida.gols_marcados_time_mandante_quarto_sexto, partida.gols_sofridos_time_mandante_quarto_sexto, partida.gols_marcados_time_mandante_quinto_sexto, partida.gols_sofridos_time_mandante_quinto_sexto, partida.gols_marcados_time_mandante_ultimo_sexto, partida.gols_sofridos_time_mandante_ultimo_sexto,
                            partida.gols_marcados_time_visitante_primeiro_sexto, partida.gols_sofridos_time_visitante_primeiro_sexto, partida.gols_marcados_time_visitante_segundo_sexto, partida.gols_sofridos_time_visitante_segundo_sexto, partida.gols_marcados_time_visitante_terceiro_sexto, partida.gols_sofridos_time_visitante_terceiro_sexto, partida.gols_marcados_time_visitante_quarto_sexto, partida.gols_sofridos_time_visitante_quarto_sexto, partida.gols_marcados_time_visitante_quinto_sexto, partida.gols_sofridos_time_visitante_quinto_sexto, partida.gols_marcados_time_visitante_ultimo_sexto, partida.gols_sofridos_time_visitante_ultimo_sexto,
                            partida.minuto_primeira_expulsao_time_mandante, partida.minuto_segunda_expulsao_time_mandante, partida.minuto_terceira_expulsao_time_mandante, partida.minuto_quarta_expulsao_time_mandante, partida.minuto_primeira_expulsao_time_visitante, partida.minuto_segunda_expulsao_time_visitante, partida.minuto_terceira_expulsao_time_visitante, partida.minuto_quarta_expulsao_time_visitante,
                            partida.placar_momento_expulsao_um, partida.placar_momento_expulsao_dois, partida.placar_momento_expulsao_tres, partida.placar_momento_expulsao_quatro, partida.placar_momento_expulsao_cinco, partida.placar_momento_expulsao_seis, partida.placar_momento_expulsao_sete, partida.placar_momento_expulsao_oito,
                            partida.expulsao_um_cartao_vd_ou_sa, partida.expulsao_dois_cartao_vd_ou_sa, partida.expulsao_tres_cartao_vd_ou_sa, partida.expulsao_quatro_cartao_vd_ou_sa, partida.expulsao_cinco_cartao_vd_ou_sa, partida.expulsao_seis_cartao_vd_ou_sa, partida.expulsao_sete_cartao_vd_ou_sa, partida.expulsao_oito_cartao_vd_ou_sa,
                            partida.quantidade_de_gols_apos_expulsao_um_time_mandante, partida.quantidade_de_gols_apos_expulsao_um_time_visitante, partida.quantidade_de_gols_apos_expulsao_dois_time_mandante, partida.quantidade_de_gols_apos_expulsao_dois_time_visitante, partida.quantidade_de_gols_apos_expulsao_tres_time_mandante, partida.quantidade_de_gols_apos_expulsao_tres_time_visitante, partida.quantidade_de_gols_apos_expulsao_quatro_time_mandante, partida.quantidade_de_gols_apos_expulsao_quatro_time_visitante, partida.quantidade_de_gols_apos_expulsao_cinco_time_mandante, partida.quantidade_de_gols_apos_expulsao_cinco_time_visitante, partida.quantidade_de_gols_apos_expulsao_seis_time_mandante, partida.quantidade_de_gols_apos_expulsao_seis_time_visitante, partida.quantidade_de_gols_apos_expulsao_sete_time_mandante, partida.quantidade_de_gols_apos_expulsao_sete_time_visitante, partida.quantidade_de_gols_apos_expulsao_oito_time_mandante, partida.quantidade_de_gols_apos_expulsao_oito_time_visitante,
                            partida.quantidade_de_gols_no_momento_expulsao_um_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_um_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_dois_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_dois_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_tres_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_tres_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_quatro_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_quatro_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_cinco_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_cinco_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_seis_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_seis_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_sete_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_sete_time_visitante, partida.quantidade_de_gols_no_momento_expulsao_oito_time_mandante, partida.quantidade_de_gols_no_momento_expulsao_oito_time_visitante,
                            partida.intervalo_expulsao_um_v_d_e, partida.intervalo_expulsao_dois_v_d_e, partida.intervalo_expulsao_tres_v_d_e, partida.intervalo_expulsao_quatro_v_d_e, partida.intervalo_expulsao_cinco_v_d_e, partida.intervalo_expulsao_seis_v_d_e, partida.intervalo_expulsao_sete_v_d_e, partida.intervalo_expulsao_oito_v_d_e,
                            partida.momento_expulsao_um_v_d_e, partida.momento_expulsao_dois_v_d_e, partida.momento_expulsao_tres_v_d_e, partida.momento_expulsao_quatro_v_d_e, partida.momento_expulsao_cinco_v_d_e, partida.momento_expulsao_seis_v_d_e, partida.momento_expulsao_sete_v_d_e, partida.momento_expulsao_oito_v_d_e,
                            partida.expulsao_um_m_v, partida.expulsao_dois_m_v, partida.expulsao_tres_m_v, partida.expulsao_quatro_m_v, partida.expulsao_cinco_m_v, partida.expulsao_seis_m_v, partida.expulsao_sete_m_v, partida.expulsao_oito_m_v,
                            partida.qtd_expulsoes_time_mandante, partida.qtd_expulsoes_time_visitante,
                            partida.posse_time_mandante, partida.posse_time_visitante, partida.chutes_a_gol_time_mandante, partida.chutes_a_gol_time_visitante, partida.chutes_fora_time_mandante, partida.chutes_fora_time_visitante, partida.ataques_time_mandante, partida.ataques_time_visitante, partida.ataques_perigosos_time_mandante, partida.ataques_perigosos_time_visitante, partida.impedimentos_time_mandante, partida.impedimentos_time_visitante, partida.faltas_time_mandante, partida.faltas_time_visitante, partida.escanteios_time_mandante, partida.escanteios_time_visitante))
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