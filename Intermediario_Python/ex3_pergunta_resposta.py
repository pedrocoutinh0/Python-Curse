# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

i = 0
for pergunta in perguntas:
    
    resposta = pergunta.get('Resposta')
    opcoes = pergunta.get('Opções')
    questao = pergunta.get('Pergunta')

    print(f'Pergunta: {questao}')
    print('Opções:')
    
    for j, opcao in zip(range(4), opcoes):
        print(f'{j}) {opcao}')
        if opcao == resposta:
            resposta = j
    
    escolha = input('Escolha uma opção: ')

    try:
        escolha = int(escolha)
    except:
        pass
    
    if escolha == resposta:
        print('Acertou 👍\n')
        i += 1
    else:
        print('Errou ❌\n')

print(f'Você acertou {i} de {len(perguntas)} perguntas')
    
