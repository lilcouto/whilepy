'''Defina um número fixo no código. Peça ao usuário para adivinhar até acertar. Informe se o palpite é
maior ou menor que o número correto.'''
codigo = 23
while True:
    tentativa = int(input("Digite um número: "))
    if tentativa > codigo:
        print("O seu palpite é maior que o código")
    elif tentativa < codigo:
        print("O seu palpite é menor que o código")
    else: 
        print("O seu palpite está certo")
        break        