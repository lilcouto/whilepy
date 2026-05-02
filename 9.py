"""Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos e quantos
negativos foram digitados."""

contadorPositivo = 0
contadorNegativo = 0
while True:
    n = int(input("Digite um número: "))
    if n > 0:
        contadorPositivo = contadorPositivo + 1
    elif n < 0:
        contadorNegativo = contadorNegativo + 1
    else:
        print(
            f'A quantidade de números positivos foram de {contadorPositivo} números positivos, enquanto o de números negativos foram de {contadorNegativo} números negativos')
        break
