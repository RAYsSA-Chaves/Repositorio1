class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado.")
        else:
            print(f"Não é possível emprestar o livro {self.titulo}, pois ele já foi emprestado!")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido.")
        else:
            print((f"O livro {self.titulo} já está disponível!"))

    def obter_info(self):
        if self.disponivel:
            disponibilidade = "Sim"
        else:
            disponibilidade = "Não"
        print(f"Título: {self.titulo}\nAno de publicação: {self.ano_publicacao}.\nDisponível: {disponibilidade}")

#------------------------------------------------

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao):
        super().__init__(titulo, ano_publicacao)
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
        print(f"Coleção: {self.titulo}")
        for livro in self.lista_livros:
            if livro.disponivel:
                disponibilidade = "Sim"
            else:
                disponibilidade = "Não"
            print(f"{livro.titulo} | {livro.ano_publicacao} | Disponível: {disponibilidade}")
            print("--------")

#Testando:
colecao = ColecaoLivros("Coleção 1", 2016)

colecao.adicionar_livro(ItemBiblioteca("A Seleção", 2012))
colecao.adicionar_livro(ItemBiblioteca("A Elite", 2013))
colecao.adicionar_livro(ItemBiblioteca("A Escolha", 2014))

for livro in colecao.lista_livros:
    if livro.titulo == "A Elite":
        livro.emprestar()

colecao.verificar_disponibilidade_colecao()
print("--------")
colecao.obter_info()