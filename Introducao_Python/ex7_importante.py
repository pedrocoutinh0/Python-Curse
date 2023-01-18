frase = 'oooooaaaaaeeeiilllllllllllllllllllllllllll'.lower().replace(" ", "")

tam = len(frase)
i = 0

letra_mvezes = frase[0]
maior = frase.count(frase[0])

while i < tam:
    letra_atual = frase[i]
    quant_vez = frase.count(letra_atual)

    if maior < quant_vez:
        maior = quant_vez
        letra_mvezes = letra_atual
    i += 1

print(f'A letra que aparece mais vezes é "{letra_mvezes}", ela aparece {maior} vezes')