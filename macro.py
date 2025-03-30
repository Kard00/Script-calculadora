
print('** CALCULADORA 2 **')

operacao = input('Escolha uma operação: (+, -, *, /,) ou digite (sair) para finalizar o programa : ')
while operacao != 'sair':
    num1 = input('Digite um número inteiro: ')
    num2 = input('Digite outro número inteiro: ')
    if operacao == '+' :
     Resultado = int(num1) + int(num2)
    elif operacao == '-' :
     Resultado = int(num1) - int(num2)
    elif operacao == '*' :
     Resultado = int(num1) * int(num2)
    elif operacao == '/' :
     Resultado = int(num1) / int(num2)
    else:
        print('Operação inválida')
    print('O resultado da operação é:', Resultado)
    operacao = input('Escolha uma operação: (+, -, *, /,) ou digite (sair) para finalizar o programa : ')
