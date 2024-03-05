dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km foram rodados? '))

d = dias * 60
dis = km * 0.15
soma = d + dis
print('Por km foram R${} e dos dias R${} a soma é R${}.'.format(dis, d, soma))