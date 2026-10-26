class Livro:
    def __init__(self, titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = True
    def emprestar(self):
     if self.disponibilidade == True:
      self.disponibilidade = False
     else:
        print("Livro não disponível")
    def devolver(self):
       self.disponibilidade = True 
       print ("Livro devolvido com sucesso")

