class aluno:
    def __init__(self,nome,matricula, nota_final):
        self.nome = nome
        self.matricula = matricula
        self.nota_final = nota_final
    def exibir_dados (self):
        print(f"Aluno :{self.nome}, matricula:{self.matricula}")    
    def verificar_aprovacao (self):
        if self.nota_final >= 6.0:
            print(f"Aluno {self.nome} foi aprovado")
        else:
            print(f"O aluno {self.nome} está de recuperação")
                