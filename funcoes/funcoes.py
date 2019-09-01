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


def identificar_minuto_expulsao_segundo_amarelo(time):
    minutos_expulsoes = []
    seg_amarelo_results_string = str(time).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('.','')
    seg_amarelo_results_string_split = seg_amarelo_results_string.split()
    if "aa-icon-Y2C'" in seg_amarelo_results_string_split:
        posicao = 0
        posicoes = []
        for pos in seg_amarelo_results_string_split:
            if(pos == "aa-icon-Y2C'"):
                posicoes.append(posicao + 4)
            posicao += 1

        for pos in posicoes:
            minuto = seg_amarelo_results_string_split[pos]
            minuto = minuto.replace("'",'')
            if '+' in minuto:
                minuto = minuto.split('+')
                minuto = int(minuto[0])+ int(minuto[1])
            else:
                minuto = int(minuto)
            minutos_expulsoes.append(minuto)

        
        # indice = seg_amarelo_results_string_split.index("aa-icon-Y2C'")
        # minuto = seg_amarelo_results_string_split[indice+4]
        # minuto = minuto.replace("'",'')
        # if '+' in minuto:
        #     minuto = minuto.split('+')
        #     minuto = int(minuto[0])+ int(minuto[1])
        # else:
        #     minuto = int(minuto)
        
        # minutos_expulsoes.append(minuto)

    return minutos_expulsoes

def identificar_minuto_expulsao_vermelho_direto(time):
    minutos_expulsoes = []
    ver_direto_results_string = str(time).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('.','')
    ver_direto_results_string_split = ver_direto_results_string.split()

    ###VERIFICAR MAIS DE UMA OCORRENCIAS
    
    if "aa-icon-RC'" in ver_direto_results_string_split:
        posicao = 0
        posicoes = []
        for pos in ver_direto_results_string_split:
            if(pos == "aa-icon-RC'"):
                posicoes.append(posicao + 4)
            posicao += 1

        for pos in posicoes:
            minuto = ver_direto_results_string_split[pos]
            minuto = minuto.replace("'",'')
            if '+' in minuto:
                minuto = minuto.split('+')
                minuto = int(minuto[0])+ int(minuto[1])
            else:
                minuto = int(minuto)
            minutos_expulsoes.append(minuto)

    return minutos_expulsoes
