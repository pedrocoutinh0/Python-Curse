import random
from time import sleep

print('Gerando CPF...')
for i in range(0,3):
    sleep(1)
    print("...")


cpf = random.randint(100000000,999999999)
cpf = str(cpf)

i = 10
soma = 0

for digito in cpf:
    digito = int(digito)
    soma += digito*i
    i -= 1

soma *= 10
resto = soma % 11
primeiro_digito_cpf = resto if resto <= 9 else 0


i = 11
soma = 0

for digito in cpf:
    digito = int(digito)
    soma += digito*i
    i -= 1
soma += primeiro_digito_cpf * i 
soma *= 10
resto = soma % 11
segundo_digito_cpf = resto if resto <= 9 else 0

cpf = cpf + str(primeiro_digito_cpf) + str(segundo_digito_cpf)

print(f"O CPF gerado é {cpf} .")


