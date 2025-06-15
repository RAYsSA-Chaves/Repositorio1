from typing import Union

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

#------------------------------------------------

class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item: Union[ItemBiblioteca, Revista, ColecaoLivros]):
        if item.titulo in self.itens:
            print("O item já existe na biblioteca")
        else:
            self.itens[item.titulo] = item  #fica assim: "titulo" : "item"
            print(f"{item.titulo} foi adicionado à biblioteca.")

    def remover_titulo(self, titulo: str):
        if titulo in self.itens:
            del self.itens[titulo]
            print(f"{titulo} removido da biblioteca.")
        else:
            print("O item não existe na biblioteca.")

    def listar_itens_disponiveis(self):
        print("Itens disponíveis:")
        for item in self.itens.values():
            if item.disponivel:
                print(item.titulo)
                print("--------")

    def contar_itens_emprestados(self):
        num = 0
        print("Itens emprestados:")
        for item in self.itens.values():
            if not item.disponivel:
                num += 1
        print(num)

#Testando:
#Criando os objetos
bibli = Biblioteca()
livro = ItemBiblioteca("A Seleção", 2012)
revista = Revista("Vogue", 1996, 5)
colecao = ColecaoLivros("Coleção 1", 2016)

#Adicionando livros na coleção
colecao.adicionar_livro(ItemBiblioteca("A Seleção", 2012))
colecao.adicionar_livro(ItemBiblioteca("A Elite", 2013))

#Usando os métodos da biblioteca
bibli.adicionar_item(livro)
bibli.adicionar_item(revista)
bibli.adicionar_item(colecao)
bibli.remover_titulo("Coleção 1")
livro.emprestar()
bibli.listar_itens_disponiveis()
bibli.contar_itens_emprestados()