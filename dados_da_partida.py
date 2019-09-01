import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana, identificar_minuto_expulsao_segundo_amarelo, identificar_minuto_expulsao_vermelho_direto
import datetime

page = requests.get("https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/sao-paulo/gremio/2989080/1/live")
soup = BeautifulSoup(page.content, 'html.parser')


estatisticas = soup.find("table", class_="match_stats_center")
cartao_vermelho = estatisticas.find(class_="red_cards")
segundo_amarelo = estatisticas.find(class_="yellow_red_cards")

###VERIFICACAO DE CARTÃO DO PRIMEIRO MODO POR MEIO DAS ESTATISTICAS
if((cartao_vermelho) and (segundo_amarelo)):
    teve_cartao_vermelho = True
    print('cartao vermelho e segundo amarelo no mesmo jogo')
    cartao_vermelho_casa = int(cartao_vermelho.find(class_="stat_value_number_team_A").get_text().strip())
    cartao_vermelho_visitante = int(cartao_vermelho.find(class_="stat_value_number_team_B").get_text().strip())

    segundo_amarelo_casa = int(segundo_amarelo.find(class_="stat_value_number_team_A").get_text().strip())
    segundo_amarelo_visitante = int(segundo_amarelo.find(class_="stat_value_number_team_B").get_text().strip())

elif((cartao_vermelho)):
    teve_cartao_vermelho = True
    print('cartao vermelho direto')
    cartao_vermelho_casa = int(cartao_vermelho.find(class_="stat_value_number_team_A").get_text().strip())
    cartao_vermelho_visitante = int(cartao_vermelho.find(class_="stat_value_number_team_B").get_text().strip())
elif((segundo_amarelo)):
    teve_cartao_vermelho = True
    print('segundo amarelo e expulsao')
    segundo_amarelo_casa = int(segundo_amarelo.find(class_="stat_value_number_team_A").get_text().strip())
    segundo_amarelo_visitante = int(segundo_amarelo.find(class_="stat_value_number_team_B").get_text().strip())
else:
    teve_cartao_vermelho = False
    print('nao houve expulsao nesse jogo')



time_a = soup.find(id="team_A_")
icone_segundo_amarelo = time_a.find_all(class_="event aa-icon-Y2C")
icone_vermelho_direto = time_a.find_all(class_="event aa-icon-RC")


minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(icone_segundo_amarelo)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(icone_vermelho_direto)
minutos_expulsoes = minutos_seg_amarelo + minutos_ver_direto

time_b = soup.find(id="team_B_")
icone_segundo_amarelo = time_b.find_all(class_="event aa-icon-Y2C")
icone_vermelho_direto = time_b.find_all(class_="event aa-icon-RC")

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(icone_segundo_amarelo)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(icone_vermelho_direto)
minutos_expulsoes += minutos_seg_amarelo + minutos_ver_direto


# for seg_amarelo in icone_segundo_amarelo:
#     seg_amarelo_results_string = str(seg_amarelo).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
#     seg_amarelo_results_string_split = seg_amarelo_results_string.split()
#     indice = seg_amarelo_results_string_split.index("aa-icon-Y2C'")
#     minuto = seg_amarelo_results_string_split[indice+4]
#     minuto = int(minuto.replace("'",''))
#     minutos_expulsoes.append(minuto)

# for ver_direto in icone_vermelho_direto:
#     ver_direto_results_string = str(ver_direto).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
#     ver_direto_results_string_split = ver_direto_results_string.split()
#     indice = ver_direto_results_string_split.index("aa-icon-RC'")
#     minuto = ver_direto_results_string_split[indice+4]
#     minuto = int(minuto.replace("'",''))
#     minutos_expulsoes.append(minuto)

print(minutos_expulsoes)





dados_gerais_da_partida = soup.find("div", "stats-game-head")
dados_gerais_da_partida = dados_gerais_da_partida.find_all("td")

### Descobrir time mandante e visitante
time_dentro = dados_gerais_da_partida[0].find_all("a")
time_fora = dados_gerais_da_partida[2].find_all("a")

time_dentro = time_dentro[1].get_text().strip() #TIME MANDANTE
time_fora = time_fora[1].get_text().strip() #TIME VISITANTE
####

### Descobrir o placar final do jogo
resultado_final = dados_gerais_da_partida[1].find(class_="f-score odd").get_text().strip() #resultado final no formato (0-0)
gols_times = resultado_final.split()

gols_mandante = gols_times[0] #quantidade de gols do time mandante
gols_visitante = gols_times[2] #quantidade de gols do time visitante
###

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