n1 = float(input('Quantos km voce ira andar? '))

if n1<= 200.0:
    valor = n1*0.5
    
else:
    valor = n1*0.45
    
print('Ja que voce ira viajar {}km entao ira pagar R${}.'.format(n1,valor))