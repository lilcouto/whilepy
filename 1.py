'''Solicite uma nota entre 0 e 10. Continue pedindo até que o usuário informe um valor válido.'''
nota = int(input("Digite um número entre 0 e 10: "))
while True:
    if nota < 0 or nota > 10:
        print("Erro! Fora do intervalo")
        nota = int(input("Digite um número entre 0 e 10: "))
    else: 
        print("Valor está dentro do intervalo")
        break    

