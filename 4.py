'''Peça números ao usuário e some-os. O programa deve parar quando o usuário digitar um número
negativo. Ao final, mostre a soma total.'''
resultado = 0

while True:
    n = int(input("Digite um número: "))
    
    if n < 0:
        break
    
    resultado = resultado + n

print(resultado)