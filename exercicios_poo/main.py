class itemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado.")
        else:
            print(f"Não é possível emprestar o livro {self.titulo}, pois ele já foi emprestado!")

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido.")
        else:
            print((f"O livro {self.titulo} já está disponível!"))

    def obter_info(self):
        if self.disponivel == True:
            disponibilidade = "Sim"
        else:
            disponibilidade = "Não"
        print(f"Título: {self.titulo}\nAno de publicação: {self.ano_publicacao}.\nDisponível: {disponibilidade}")

#Testando:
livro = itemBiblioteca("A Seleção", 2012, True)

livro.obter_info()
print("--------")
livro.emprestar()
print("--------")
livro.devolver()
print("--------")
livro.obter_info()