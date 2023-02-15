# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args: int):
    num = 1
    for numero in args:
        num *= numero
    return num

print(multiplicar(1,2,3,4,5))


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero: int):
    if numero % 2 == 0:
        return "Par"
    return "Impar"

print(par_impar(34))