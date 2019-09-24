import csv
f = open('tabela3.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow(('Nome', 'Idade', 'Sexo'))
    writer.writerow(('Leo', '21', 'M'))
    writer.writerow(('Luiz Carlos', '50', 'M'))
    writer.writerow(('Juninho', '51', 'M'))
finally:
    f.close()


