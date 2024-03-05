#Variaveis

cigarros = int(input('Quantos cigarros voce fuma por dia? '))
anos = int(input('A quantos anos voce fuma? '))
temp = (anos * 365)* cigarros / 1440

print('Voce perdeu {} dias de vida'.format(round(temp)))
