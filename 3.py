'''Peça um número inteiro positivo N e mostre todos os números de 1 até N usando repetição.'''
n = int(input("Digite um número inteiro e positivo: "))
contador = 1
while True:
    if contador <= n:
        print(contador)
        contador = contador + 1
    else:
        break
