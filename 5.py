'''Peça números ao usuário continuamente e informe se cada número é par ou ímpar. O programa só
deve parar quando o usuário digitar 0.'''
while True:
    n1 = int(input("Digite um número diferente de 0: "))
    if n1 % 2 == 0 and n1 != 0:
        print(f'o número {n1} é par')
    elif n1 % 2 == 1 and n1 != 0:
        print(f'o número {n1} é ímpar')
    else:
        print(f'o número digitado foi {n1}')
        break
