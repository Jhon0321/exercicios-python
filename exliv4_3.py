n1 = float(input("Digite um numero: "))
n2 = float(input('Digite outro: ')) 
n3 = float(input('Digite mais um: '))

#n1 maior e n3 menor
if n1>n2 and n1>n3 and n2>n3:
    print('O numero {} é o maior e {} é o menor'.format(n1, n3))

#n1 maior e n2 menor
if n1>n3 and n1>n2 and n2<n3:
    print('O numero {} é o maior e {} é o menor'.format(n1, n3))

#n2 maior e n3 menor
if n2>n1 and n2>n3 and n1>n3:
    print('O maior é {} e o menor é {}'.format(n2,n3))

#n2 maior e n1 menor
if n2>n3 and n2>n1 and n1<n3:
    print('O maior é {} e o menor é {}'.format(n2,n1))

#n3 maior e n2 menor
if n3>n2 and n3>n1 and n1>n2:
    print('Esse é o menor {}, e esse o maior {}'.format(n2,n3))

#n3 maior e n1 menor
if n3>n1 and n3>n2 and n2>n1:
    print('Esse é o menor {}, e esse o maior {}'.format(n1,n3))
