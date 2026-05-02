'''Desenvolva um programa que solicite ao usuário a digitação de uma nota entre 0
e 10. Caso o valor informado esteja fora desse intervalo, o programa deve exibir
uma mensagem de erro e solicitar novamente a entrada, repetindo o processo até
que um valor válido seja informado.'''
intervalo = int(input("Digite um número entre 0 e 10: "))
while True:
    if intervalo < 0 or intervalo > 10:
        print("Erro! Fora do intervalo")
        intervalo = int(input("Digite um número entre 0 e 10 "))
    else: 
        print("Valor está dentro do intervalo")
        break    

