"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Digite o horário: ")

try:
    horario_int = int(horario)
    bdia = horario_int > -1 and horario_int < 12
    btarde = horario_int > 11 and horario_int < 18
    bnoite = horario_int > 17 and horario_int < 24

    if bdia:
        print(f'Bom dia ! São {horario_int} horas.')
    elif btarde:
        print(f'Boa tarde ! São {horario_int} horas')
    elif bnoite:
        print(f'Boa noite ! São {horario_int} horas')
    else:
        print('O horário precisa estar entre 0 e 23')
except:
    print('O horário não é inteiro.')