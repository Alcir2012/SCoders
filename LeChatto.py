def Saudação(Nome = 'Alcir'):
    print(f'Bem vindo ao restaurante LeChatto {Nome}')
    
def Atendimento():
    atendimento = input('Deseja ver o cardapio? [1] Sim, [2] Não ')
    if atendimento.upper() == '1' or atendimento.upper() == 'SIM':
        pedido = input('Diga o que deseja do cardápio: [1] Combo Smash, [2] Combo Escolha do Chefe, [3] Hot Wings: ')
        if pedido == '1':
            print('Trazendo um Combo Smash em instantes')
        elif pedido == '2':
             print('Então você vai querer um Combo Escolha do Chefe')
        else:
            print('Trazendo uma hot Wings')
            return (f'Ok, vou trazer o seu {pedido}')
    else:
        return ('Nenhum pedido foi realizado, vou trazer apenas pães com molho da casa, é de graça :D ')
def Continua_Atendimento():
    for i in range(3):
        algo_mais = input('Deseja mais alguma coisa? [1] Sim, [2] Não ')
        if algo_mais == '1':
            continuação_pedido = input('O que deseja? [1] Bebidas, [2] Drinks, [3] entradas')
            if continuação_pedido == '1':
                lista_de_bebidas = input('Qual você quer? [1] Coca Zero [2] Fanta [3]Coca Normal')
                if lista_de_bebidas == '1' or 'Coca Zero':
                    print('Certo, vou trazer uma Coca Zero pra você')
                elif lista_de_bebidas == '2' or 'Fanta':
                    print('Certo, vou trazer uma Fanta para você')
                else:
                    print('Trazendo uma coca normal então')
            elif continuação_pedido == '2':
                lista_de_drinks = input('Qual drink você deseja? [1] Caipiroska [2] Caipirinha [3] NEGRONI [4] Dry Martini')
                if lista_de_drinks == '1':
                    print('Trazendo uma Caipiroska pra você')
                elif lista_de_drinks == '2':
                    print ('Trazendo uma Caipirinha pra você')
                elif lista_de_drinks == '3':
                    print('Trazendo um Negroni para você')
                elif lista_de_drinks == '4':
                    print('Trazendo um Dry Martini pra você')
            else:
                entradas = input('Segue a lista de entradas: [1]Onion Rings [2] Batata frita [3]Camarão empanado, [4] Batata com cheddar e bacon')
                if entradas  == '1':
                    print('Certo, trazendo uma Onion Rings pra você')
                elif entradas == '2':
                    print('Ok, trazendo uma batata frita pra você')
                elif entradas == '3':
                    print('Certo, vou trazer o carro chefe da casa, camarão empanado')
                else:
                    print('Show de bola, trazendo uma batata frita com cheddar e baconzada')
        else: 
            print('Certo, então qualquer coisa você me chama!')

Saudação()
resposta_atendimento = Atendimento()
#print(resposta_atendimento)
continua_atendimentos = Continua_Atendimento()