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

#------------------------------------------------

class RelatorioBiblioteca:
    def __init__(self, objeto: Biblioteca):
        self.objeto = objeto

    def gerar_relatorio_completo(self):
        print("Relatório completo:")
        print("----------------------------------")
        for item in self.objeto.itens.values():
            item.obter_info()

    def gerar_relatorio_disponibilidade(self):
        contador = 0
        print("Relatório de disponibilidade:")
        print("----------------------------------")
        for item in self.objeto.itens.values():
            if isinstance(item, ColecaoLivros):  #considerar os itens dentro da colação
                for livro in item.lista_livros:
                    if livro.disponivel:
                        contador += 1
                        print(livro.titulo)
            elif item.disponivel:
                contador += 1
                print(item.titulo)
        print(f"Quantidade de itens disponíveis: {contador}")

    def gerar_relatorio_emprestimos(self):
        contador = 0
        total = 0
        print("Relatório de empréstimos:")
        print("----------------------------------")
        for item in self.objeto.itens.values():
            total += 1
            if isinstance(item, ColecaoLivros):  #considerar os itens dentro da colação
                total -= 1  #desconsiderar a o objeto coleção
                for livro in item.lista_livros:
                    total += 1
                    if not livro.disponivel:
                        contador += 1
            elif not item.disponivel:
                contador += 1
        print(f"{contador} itens emprestados.")
        proporcao = (contador/total)
        print(f"Proporção de itens emprestados em relação ao total: {contador}/{total} = {proporcao:.2f}")

#Testando:
#Criando os objetos
bibli = Biblioteca()
livro = ItemBiblioteca("A Seleção", 2012)
revista = Revista("Vogue", 1996, 5)
colecao = ColecaoLivros("Coleção 1", 2014)

#Adicionando livros na coleção
colecao.adicionar_livro(ItemBiblioteca("Boa Noite Punpun 1", 2007))
colecao.adicionar_livro(ItemBiblioteca("Boa Noite Punpun 2", 2014))

#Usando os métodos da biblioteca
bibli.adicionar_item(livro)
bibli.adicionar_item(revista)
bibli.adicionar_item(colecao)
livro.emprestar()

#Usando os métodos do relatório
relatorio = RelatorioBiblioteca(bibli)
relatorio.gerar_relatorio_completo()
relatorio.gerar_relatorio_disponibilidade()
relatorio.gerar_relatorio_emprestimos()