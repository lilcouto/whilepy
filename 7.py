'''Peça várias notas ao usuário (encerra quando digitar -1) e calcule a média das notas válidas.'''
contador = 0
soma = 0
while True:
    n1 = float(input("Digite uma nota: "))
    if n1 == -1:
        break
    soma = soma + n1
    contador = contador + 1
media = soma / contador
print(f'a média das notas é {media}')    
   