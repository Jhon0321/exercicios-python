inicio = int(input('Digite o numero incial da tabuada: '))
final = int(input('Digite o ultimo multiplo: '))
x = 1
tab = 0

while final > tab:
    tab = inicio * x
    x += 1
    print (tab)
