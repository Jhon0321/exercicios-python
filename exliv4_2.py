v = int(input('Qual velocidade o carro esta: '))
if v>80:
    multa = (v-80)*5
    print('Voce foi multado em R$%.2f.' % (multa))
else:
    print('Voce nao foi multado, parabens!')