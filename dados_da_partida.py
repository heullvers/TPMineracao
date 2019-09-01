import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana, identificar_minuto_expulsao_segundo_amarelo, identificar_minuto_expulsao_vermelho_direto
import datetime

page = requests.get("https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/avai/corinthians/2989073/1/live")
soup = BeautifulSoup(page.content, 'html.parser')

estatisticas = soup.find("table", class_="match_stats_center")

time_a = soup.find(id="team_A_")
time_b = soup.find(id="team_B_")

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_a)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_a)
minutos_expulsoes_time_a = minutos_seg_amarelo + minutos_ver_direto

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_b)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_b)
minutos_expulsoes_time_b = minutos_seg_amarelo + minutos_ver_direto

print(minutos_expulsoes_time_a)
print(minutos_expulsoes_time_b)
    #minutos_expulsoes = minutos_seg_amarelo + minutos_ver_direto


    # time_b = soup.find(id="team_B_")
    # icone_segundo_amarelo = time_b.find_all(class_="event aa-icon-Y2C")
    # icone_vermelho_direto = time_b.find_all(class_="event aa-icon-RC")
    # minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(icone_segundo_amarelo)
    # minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(icone_vermelho_direto)
    # minutos_expulsoes += minutos_seg_amarelo + minutos_ver_direto

#print(minutos_expulsoes)





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