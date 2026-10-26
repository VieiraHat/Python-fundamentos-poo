class cartao_estudantil:
    def __init__(self,nome_aluno):
     self.nome_aluno = nome_aluno
     self.saldo = 0
    def recarregar(self,valor):
      self.saldo += valor
    def usar_passagem(self,tarifa):
      if self.saldo >= tarifa:
        self.saldo -= tarifa
      else:
        print("Saldo insuficiente")
    def consultar_saldo(self):
      print(f"Seu saldo atual é: {self.saldo}")
      
              
      
