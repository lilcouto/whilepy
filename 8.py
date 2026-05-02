'''Peça um número e mostre a tabuada dele de 1 a 10.'''
n = int(input("Digite um número: "))
comeco = 1
while True:
    if comeco == 1 or comeco <= 10:
        tabuada = n * comeco
        print(tabuada)
        comeco = comeco + 1
    else: 
        break    