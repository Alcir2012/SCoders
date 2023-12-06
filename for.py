soma = 0
for i in range(3):
    nota= float(input('Informe sua nota '))
    soma = soma+nota
média = soma/3
print(média)
nota_minima = 7
if média < nota_minima:
    print('Você não passou, tente novamente ano que vem')
else:
    print('Você passou, te vejo ano que vem')
    