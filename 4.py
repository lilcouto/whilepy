'''Peça números ao usuário e some-os. O programa deve parar quando o usuário digitar um número
negativo. Ao final, mostre a soma total.'''
while True:
    n1 = int(input("Digite um número positivo: "))
    n2 = int(input("Digite um número positivo: "))
    if n1 > 0 and n2 > 0:
        soma = n1 + n2
    else: 
        print(soma)
        break