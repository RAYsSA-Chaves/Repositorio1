class ItemBiblioteca:
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

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                print(f"O livro {livro.titulo} não está disponível")
                return False
        return True

    def obter_info(self):
        for livro in self.lista_livros:
            print(livro.titulo)

#Testando:
colecao = ColecaoLivros("Coleção 1", 2016, True)

colecao.adicionar_livro(ItemBiblioteca("A Seleção", 2012, True))
colecao.adicionar_livro(ItemBiblioteca("A Elite", 2013, True))
colecao.adicionar_livro(ItemBiblioteca("A Escolha", 2014, False))
colecao.verificar_disponibilidade_colecao()
print("--------")
colecao.obter_info()