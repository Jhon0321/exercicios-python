n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro: '))
ope = int(input('Qual operaçao deseja fazer? Digite 1 +, 2 -, 3 x, 4 para divisao: '))

if ope == 1:
    res = n1 + n2
    ope1 = 'soma'
if ope == 2:
    res = n1 - n2
    ope1 = 'subtração'
if ope == 3:
    res = n1 * n2
    ope1 =  'multiplicação'
if ope == 4:
    ope = n1 / n2
    ope1 = 'divisão'
print('O resultado da {} é {}'.format(ope1, res))