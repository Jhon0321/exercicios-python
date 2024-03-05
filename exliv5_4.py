n1 = int(input('Digite o ultimo numero: '))
x = 1

while x < n1 :
    res = n1 % 2
    if res != 0:
        x = x + 2
    else:
        n1 = n1 + 1
    
    if x != 0 and x < n1:
        print(x)