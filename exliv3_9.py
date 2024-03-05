dias = 0 
horas = 0 
minutos = 0 
segundos = 0


dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

soma = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos 

print('O total de segundos é {}'.format(soma))