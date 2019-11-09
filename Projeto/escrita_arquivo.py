import csv
f = open('tabela2.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('Nome', 'Idade', 'Sexo'))
    writer.writerow(('Heuller', '21', 'M'))
    writer.writerow(('Alan', '22', 'F'))
    writer.writerow(('Kelvin', '21', 'M'))
finally:
    f.close()


