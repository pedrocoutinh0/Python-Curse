"""
Iterando strings com while
"""
#       012345678910
nome = 'Pedro Lucas'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)

index = 0
nova_string = ""

while index < tamanho_nome:

    if index == (tamanho_nome-1):
        nova_string += "*" + nome[index] + "*"
        index += 1
        continue

    nova_string += "*" + nome[index] 
    index += 1

print(nova_string)