'''
Calculadora
'''

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    op = input('Digite o operador(+,-,/,*): ').replace(" ", "")

    result = None

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('Números inválidos !')
        continue

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        if num2 == 0:
            print("Números não podem ser divididos por 0 !")
            continue
        result = num1 / num2
    elif op == "*":
        result = num1*num2
    else:
        print('Operador Inválido')
        continue
    
    print(f'{num1} {op} {num2} = {result} ')

    sair = input('Se deseja sair digite 0: ').replace(" ", "")
    if sair == "0":
        break