"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
#!/usr/bin/env python
# Desenvolvimento Aberto
# shell.py
import os

palavra_secreta = "perfume"
tam = len(palavra_secreta)
tentativas = 0
letra_acertadas = ''

while True:
    letra = input("Digite uma letra: ")
    if len(letra) != 1:
        print('Digite uma letra !')
        continue
    
    if letra in palavra_secreta:
        letra_acertadas += letra

    palavra_anonima =""
    for letras in palavra_secreta:
        if letras in letra_acertadas:
            palavra_anonima += letras
        else:
            palavra_anonima += "*"
                

    if palavra_anonima == palavra_secreta:
        os.system("cls")
        print(f'VOCÊ GANHOU PARABÉNS !!! \nA palavra era: {palavra_secreta} \nTentativas {tentativas}')
        tentativas = 0 
    else:
        print(f'A palavra formatada é: {palavra_anonima}')
        tentativas += 1