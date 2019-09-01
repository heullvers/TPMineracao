import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana, identificar_minuto_expulsao_segundo_amarelo, identificar_minuto_expulsao_vermelho_direto
import datetime

page = requests.get("https://www.academiadasapostasbrasil.com/stats/match/inglaterra-stats/barclays-premier-league/southampton/manchester-united/3029111/1/live")
soup = BeautifulSoup(page.content, 'html.parser')

estatisticas = soup.find("table", class_="match_stats_center")

##Posse de bola
posse = estatisticas.find("tr", class_="possession")
posse_time_a = int(posse.find("td", class_="stat_value_number_team_A").get_text().strip().replace("%",''))
posse_time_b = int(posse.find("td", class_="stat_value_number_team_B").get_text().strip().replace("%",''))

##Chutes a gol
chutes_a_gol = estatisticas.find("tr", class_="shots_on_target")
chutes_a_gol_time_a = int(chutes_a_gol.find("td", class_="stat_value_number_team_A").get_text().strip())
chutes_a_gol_time_b = int(chutes_a_gol.find("td", class_="stat_value_number_team_B").get_text().strip())

##Chutes fora
#shots_off_target
chutes_fora = estatisticas.find("tr", class_="shots_off_target")
chutes_fora_time_a = int(chutes_fora.find("td", class_="stat_value_number_team_A").get_text().strip())
chutes_fora_time_b = int(chutes_fora.find("td", class_="stat_value_number_team_B").get_text().strip())

##Ataques
#attacks
ataques = estatisticas.find("tr", class_="attacks")
ataques_time_a = int(ataques.find("td", class_="stat_value_number_team_A").get_text().strip())
ataques_time_b = int(ataques.find("td", class_="stat_value_number_team_B").get_text().strip())

##Ataques perigosos
#dangerous_attacks
ataques_perigosos = estatisticas.find("tr", class_="dangerous_attacks")
ataques_perigosos_time_a = int(ataques_perigosos.find("td", class_="stat_value_number_team_A").get_text().strip())
ataques_perigosos_time_b = int(ataques_perigosos.find("td", class_="stat_value_number_team_B").get_text().strip())

##Impedimentos
#offsides
impedimentos = estatisticas.find("tr", class_="offsides")
impedimentos_time_a = int(impedimentos.find("td", class_="stat_value_number_team_A").get_text().strip())
impedimentos_time_b = int(impedimentos.find("td", class_="stat_value_number_team_B").get_text().strip())

##Faltas
#fouls
faltas = estatisticas.find("tr", class_="fouls")
faltas_time_a = int(faltas.find("td", class_="stat_value_number_team_A").get_text().strip())
faltas_time_b = int(faltas.find("td", class_="stat_value_number_team_B").get_text().strip())

##Escanteios
#corners
escanteios = estatisticas.find("tr", class_="corners")
escanteios_time_a = int(escanteios.find("td", class_="stat_value_number_team_A").get_text().strip())
escanteios_time_b = int(escanteios.find("td", class_="stat_value_number_team_B").get_text().strip())

##Identificar expulsoes
time_a = soup.find(id="team_A_")
time_b = soup.find(id="team_B_")

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_a)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_a)
minutos_expulsoes_time_a = minutos_seg_amarelo + minutos_ver_direto

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_b)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_b)
minutos_expulsoes_time_b = minutos_seg_amarelo + minutos_ver_direto


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




print(minutos_expulsoes_time_a)
print(minutos_expulsoes_time_b)


print(time_dentro)
print(time_fora)
print(resultado_final)
print(gols_mandante)
print(gols_visitante)
print(data_do_jogo)
print(horario)
print(turno)
print(dia_semana)

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
