sal = float(input('Qual o seu salario atual? '))
casa = float(input('Qual o valor da casa? '))
par = int(input('Quantas parcelas? '))

mens = casa/par
por = sal*0.3
if mens <= por:
    print('APROVADO')
else:
    print('REPROVADO')