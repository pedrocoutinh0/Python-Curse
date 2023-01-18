"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:
    opcao = input('Digite:\n\t1-Para Inserir\n\t2-Para Apagar\n\t3-Para Listar\n')

    if opcao == "1":
        compra = input('Digite o que você deseja adicionar: ')
        lista_compras.append(compra)
        os.system('cls')
    elif opcao == "2":
        os.system('cls')
        indice = input('Digite o indice do item que deseja apagar: ')
        try:
            indice = int(indice)
            del lista_compras[indice]
        except ValueError:
            print('Digite números inteiros !')
        except IndexError:
            print('Indice inexistente !')
    elif opcao == "3":
        if lista_compras:
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
        else:
            print('Lista vazia, adicione algo !')
            os.system('cls')
    else:
        print('Digite uma opção válida !')