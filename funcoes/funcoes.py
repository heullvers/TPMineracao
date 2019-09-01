from datetime import date

def dia_da_semana(ano,mes,dia):
    DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]

    data = date(year=ano, month=mes, day=dia)
    indice_da_semana = data.weekday()
    dia_da_semana = DIAS[indice_da_semana]
    
    return dia_da_semana


def identificar_minuto_expulsao_segundo_amarelo(icone_segundo_amarelo):
    minutos_expulsoes = []
    for seg_amarelo in icone_segundo_amarelo:
        seg_amarelo_results_string = str(seg_amarelo).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
        seg_amarelo_results_string_split = seg_amarelo_results_string.split()
        indice = seg_amarelo_results_string_split.index("aa-icon-Y2C'")
        minuto = seg_amarelo_results_string_split[indice+4]
        minuto = int(minuto.replace("'",''))
        minutos_expulsoes.append(minuto)

    return minutos_expulsoes

def identificar_minuto_expulsao_vermelho_direto(icone_vermelho_direto):
    minutos_expulsoes = []
    for ver_direto in icone_vermelho_direto:
        ver_direto_results_string = str(ver_direto).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
        ver_direto_results_string_split = ver_direto_results_string.split()
        indice = ver_direto_results_string_split.index("aa-icon-RC'")
        minuto = ver_direto_results_string_split[indice+4]
        minuto = int(minuto.replace("'",''))
        minutos_expulsoes.append(minuto)

    return minutos_expulsoes