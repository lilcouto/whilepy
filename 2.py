'''Peça ao usuário para digitar uma senha. Continue solicitando até que ele acerte a senha correta
(defina uma senha fixa no código).'''
senha = "coutinho"
dica = "Dica = Sobrenome"
tentativa = input("Digite a senha: ")
while True:
    if tentativa != senha:
        print("Senha errada")
        print(dica)
        tentativa = input("Digite a senha: ")
    else:
        print("senha correta")
        break    
