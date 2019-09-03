import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana, identificar_minuto_expulsao_segundo_amarelo, identificar_minuto_expulsao_vermelho_direto
import datetime

link = "https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/fortaleza/goias/2989078/1/live"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')


dados_gerais_da_partida = soup.find("div", "stats-game-head")
dados_gerais_da_partida = dados_gerais_da_partida.find_all("td")

##Identificar expulsoes
time_a = soup.find(id="team_A_")
time_b = soup.find(id="team_B_")

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_a)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_a)
minutos_expulsoes_time_a = minutos_seg_amarelo + minutos_ver_direto

minutos_seg_amarelo = identificar_minuto_expulsao_segundo_amarelo(time_b)
minutos_ver_direto = identificar_minuto_expulsao_vermelho_direto(time_b)
minutos_expulsoes_time_b = minutos_seg_amarelo + minutos_ver_direto

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

estatisticas = soup.find("table", class_="match_stats_center")
##Posse de bola
posse = estatisticas.find("tr", class_="possession")
if(posse):
    posse_time_a = int(posse.find("td", class_="stat_value_number_team_A").get_text().strip().replace("%",''))
    posse_time_b = int(posse.find("td", class_="stat_value_number_team_B").get_text().strip().replace("%",''))
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

##Estatisticas outra aba
link = link.replace("live", "prelive")
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

estatisticas_aprofundadas = soup.find(id="ultimos_resultados")

###Ajustar para receber essas variáveis da ficha de jogo
times = estatisticas_aprofundadas.find_all(class_="stats-subtitle")
time_casa = times[0].get_text()
time_visitante = times[1].get_text()

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
odds = odds.find(class_="even")
odds = odds.find_all(class_="odd-B")

todas_odds = []
for odd in odds:
    todas_odds.append(float(odd.get_text().strip()))

odd_time_casa = todas_odds[0]
odd_empate = todas_odds[1]
odd_time_fora = todas_odds[2]










'''
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

print(posicao_time_dentro)
print(posicao_time_fora)

print(odd_time_casa)
print(odd_empate)
print(odd_time_fora)
'''