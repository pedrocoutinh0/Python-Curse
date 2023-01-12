"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    ehpar = numero_int % 2 == 0 
    if ehpar:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')
except:
    print("Não é um número inteiro.")