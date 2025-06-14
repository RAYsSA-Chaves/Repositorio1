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

#------------------------------------------------

class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, edicao: int):
        super().__init__(titulo, ano_publicacao)
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao: int):
        if nova_edicao > 0 and nova_edicao > self.edicao:
            self.edicao = nova_edicao
            print(f"Edição da revista {self.titulo} atualizada.")
        else:
            print("A nova edição não pode ser um número menor que 0 ou menor que a edição anterior.")

    def restringir_emprestimo(self, dias_max: int):
        if self.ano_publicacao < 2000:
            if dias_max <= 7:
                return True
            else:
                return False
        return True
    
    def obter_info(self):
        if self.disponivel:
            disponibilidade = "Sim"
        else:
            disponibilidade = "Não"
        print(f"{self.titulo} | {self.ano_publicacao} | Edição: {self.edicao} | Disponível: {disponibilidade}")

#Testando:
revista = Revista("Vogue", 1996, 5)
revista.atualizar_edicao(6)
restricao = revista.restringir_emprestimo(5)
print(restricao)
revista.obter_info()