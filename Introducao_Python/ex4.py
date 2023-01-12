"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
nome = nome.replace(" ", "")

ncurto = len(nome) < 5
nnormal = len(nome) > 4 and len(nome) < 7
ngrande = len(nome) > 6
if len(nome) >= 1:
    if ncurto:
        print(f'Seu nome é curto')
    elif nnormal:
        print(f'Seu nome é normal')
    elif ngrande:
        print(f'Seu nome é muito grande')
else:
    print('Digite um nome !')
    