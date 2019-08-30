class Meses:
    janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro = range(1,13,1)


def qualMes(mes):
    if(mes == 'janeiro'):
        return Meses.janeiro
    elif(mes == 'fevereiro'):
        return Meses.fevereiro
    elif(mes == 'marco'):
        return Meses.marco
    elif(mes == 'abril'):
        return Meses.abril
    elif(mes == 'maio'):
        return Meses.maio
    elif(mes == 'junho'):
        return Meses.junho
    elif(mes == 'julho'):
        return Meses.julho
    elif(mes == 'agosto'):
        return Meses.agosto
    elif(mes == 'setembro'):
        return Meses.setembro
    elif(mes == 'outubro'):
        return Meses.outubro
    elif(mes == 'novembro'):
        return Meses.novembro
    elif(mes == 'dezembro'):
        return Meses.dezembro
    else:
        return None
    