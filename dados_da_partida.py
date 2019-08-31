import requests
from bs4 import BeautifulSoup

from Enum.Meses import qualMes
from funcoes.funcoes import dia_da_semana
import datetime

page = requests.get("https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/cruzeiro/santos/2989057/1/live")
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

if(teve_cartao_vermelho):
    sumario = soup.find_all(class_="stat-quarts-padding")
    trs = []
    for evento in sumario:
        tr = evento.find_all("tr")
        trs.append(tr)

    
    lista_teste = []
    indice1 = 0
    indice2 = 0
    for tr in trs:
        for td in tr:
            tds = td.find_all("td", class_="match-sum-wd-symbol")
            for dado in tds:
                cartao_v = dado.find("span", class_="aa-icon-RC")
                if(cartao_v):
                    qual_quarts = indice1
                    qual_tr = indice2
                    #print(cartao_v)
                    #print('INDICE', indice)
                    #print('-----------------')
            #dicionario[indice] = tds
            #print(tds)
            #print('QUAL TR', indice)
            #print('-----------------')
            indice2 += 1
        indice1 += 1

    cod = trs[qual_quarts][qual_tr]
    minuto_duplicado = cod.find_all(class_="match-sum-wd-minute")
    for minuto in minuto_duplicado:
        minuto = minuto.get_text().strip()
        if(minuto != ''):
            minuto = minuto.replace("'",'')
            print(minuto)
    #print(minuto)

    #print(dicionario)
    #     print(tr)
    #     print('---------------')
        #tds = tr.find_all("td")
        #print(tds)
        #print('------------------')
        #print(trs)
        #print('--------')
        #lista = sumario.find("span")
    #icon_cv = sumario.find_all(class_="ico aa-icon-RC")
    #print(lista)
    #print(sumario)
    #print('-------')
    #print(trs)


#print(cartao_vermelho_casa)
#print(cartao_vermelho_visitante)

#print(segundo_amarelo)
#print(segundo_amarelo_casa)
#print(segundo_amarelo_visitante)
#print(cartao_vermelho)




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