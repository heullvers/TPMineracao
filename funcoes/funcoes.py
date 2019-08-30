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