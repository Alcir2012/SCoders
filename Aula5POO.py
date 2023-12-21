class Turma():
    def __init__(self, turmaid:int):
        self.turmaid = turmaid
        self.alunos = []
    def __str__ (self):
        return f'id: {self.turmaid}'
    def adicionar_alunos(self,aluno):
        self.alunos.append(aluno)   
        return 'Aluno adicionado com sucesso!' 
       
class Aluno():
    def __init__(self, idAluno, nome):
        self.idAluno = idAluno
        self.nome = nome
    def __str__(self):
        return f'{self.nome} {self.idAluno}'
    
turm = Turma(1)
alun1 = Aluno(1,'Jose')
alun2 = Aluno(1,'Joao')
turm.adicionar_alunos(alun1)
turm.adicionar_alunos(alun2)
print(turm)
for i in turm.alunos:
    print(i)