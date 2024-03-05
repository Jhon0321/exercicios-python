prod = float(input('Digite o preço do produto: '))
desc = float(input('Digite o desconto; '))

desc1 = desc/100
prod1 = desc1 * prod
desconto = prod - prod1
print('O produto custa {} e com desconto fica {}'.format(prod, desconto))
