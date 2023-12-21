class Arquivo():
    __path: str
    def __init__(self, path):
        self.__path = path
    def ler_txt(self, encoding='utf-8'):
        with open(self.__path,'r',encoding=encoding) as arq:
            for item in arq:
                print(item)
        arq.close
arquivo = Arquivo(r'C:\Users\Alcir.Sousa\Documents\GitHub\SCoders\testePOO.txt')
arquivo.ler_txt()