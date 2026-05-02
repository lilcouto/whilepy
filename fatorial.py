'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120'''
n = int(input("Digite um número inteiro: "))
resultado = 1
while (n > 0):
    resultado = resultado * n
    n = n - 1
print(resultado)
