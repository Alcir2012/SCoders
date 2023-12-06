def calculadora(num1,num2, operação = '+'):
    if operação == '+':
        return num1+num2 #ao usar return, encerra a função, então, oque eu colocar após o return, não será executado
    else:
        return('Operação invalida')
resultado = calculadora(5,7)
print(resultado)