con = float(input('Quanto foi gasto em kWh? '))
tip = str(input('Qual o tipo de comercio? R para residencia, I para industria, e C para comercio: '))

if tip == 'R' or 'r' and con <= 500.0:
    valor = con * 0.4
if tip == 'R' or 'r' and con>500.0:
    valor = con * 0.65

if tip == 'C' or 'c' and con <= 1000.0:
    valor = con * 0.55
if tip == 'C' or 'c' and con > 1000.0:
    valor = con * 0.6

if tip == 'I' or 'i' and con <= 5000:
    valor = con * 0.55
if tip == 'I' or 'i' and con > 5000:
    valor = con * 0.6

print('O valor a ser pago é R$%.2f.' % (valor))
