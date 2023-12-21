class Computador():
    def __init__(self,PlacaM:str,Processador:str,Memoria:int,SSD:int)-> None:
        self.Placa_Mae = PlacaM
        self.Processador = Processador
        self.Memoria = Memoria
        self.SSD = SSD
        
PC = Computador('Gigabyte', 'Intel Core i7', '16', '1000')
print(PC.Memoria)
