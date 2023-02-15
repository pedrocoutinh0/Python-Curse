# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def aumentar(vezes: int):
    def multiplicar(num: float):
        return num*vezes
    return multiplicar

duplicar = aumentar(2)
triplicar = aumentar(3)
quadruplicar = aumentar(4)

print(duplicar(7))
print(triplicar(9))
print(quadruplicar(16))