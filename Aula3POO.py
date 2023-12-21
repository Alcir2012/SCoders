class Frase():
    def __init__(self,frase:str):
        self.Frase = frase

    def Conta_Caracteres(self):
        caracteres = len(self.Frase)
        return caracteres
    
    def Conta_Palavras(self):
        palavras = len(self.Frase.split())
        return palavras
    def Inverte_Frase(self):
        inverter = self.Frase[::-1]
        return inverter
fras = Frase('Bom dia princesa!')

print(fras.Frase)
print(fras.Conta_Caracteres())
print(fras.Conta_Palavras())
print(fras.Inverte_Frase())