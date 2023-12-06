while True:
    numero = int(input('Digite o primeiro número '))
    numero2= int(input('Digite um segundo número '))
    print('Escolha oque quer fazer com este número [1]somar, [2]multiplicar, [3]subtrair,[4]dividir,[5]Encerrar o programa')
    opção=int(input('sua escolha foi: '))
    if opção == 1:
        print('A soma dos números é {}'.format(numero+numero2))
    elif opção == 2:
        print('A multiplicação dos número é {}'.format(numero*numero2))
    elif opção == 3:
        print('A subtração dos números é {}'.format(numero-numero2))
    elif opção == 4:
        print('A divisão dos números é {}'.format (numero/numero2))
    elif opção == 5:
        print('Ok, bye')
        break
    else: 
        print('Opção não está nas litadas')    