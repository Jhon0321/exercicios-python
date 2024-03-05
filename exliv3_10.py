sal = float(input('Qual o seu salario atual? '))
por = float(input('Qual a porcentagem de aumento? '))

aum1 = por / 100 
aum2 = sal * aum1
atual = aum2 + sal

print('O salario era {} com o aumento ficou {}'.format(sal, atual))
