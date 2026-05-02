'''Peça vários números ao usuário (encerra com 0) e informe qual foi o maior número digitado.'''
maior = 0
while True:
    n = int(input("Digite um número diferente de 0: "))
    if n == 0:
        print(f'o maior número digitado foi: {maior}')
        break

    if maior == 0:
        maior = n
    elif n > maior:
        maior = n
    print(f'o maior número digitado até então foi: {maior}')

