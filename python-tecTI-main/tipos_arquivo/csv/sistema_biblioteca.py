import pandas
import datetime as dt


class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Emprestimo:
    def __init__(self, livro, pessoa, data_emprestimo, data_devolucao):
        self.livro = livro
        self.pessoa = pessoa
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, livro, pessoa, data_emprestimo, data_devolucao):
        if livro in self.livros:
            emprestimo = Emprestimo(livro, pessoa, data_emprestimo, data_devolucao)
            self.emprestimos.append(emprestimo)
            self.livros.remove(livro)
            return True
        return False

    def devolver_livro(self, emprestimo):
        if emprestimo in self.emprestimos:
            self.emprestimos.remove(emprestimo)
            self.livros.append(emprestimo.livro)
            return True
        return False
    
    def listar_livros_disponiveis(self):
        return self.livros


biblioteca = Biblioteca()
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
data_emprestimo = dt.datetime.now()
data_devolucao = dt.datetime.now() + dt.timedelta(days=14)
biblioteca.emprestar_livro(livro2, pessoa1, data_emprestimo, data_devolucao)
emprestimo = biblioteca.emprestimos[0]

listar_livros = biblioteca.listar_livros_disponiveis()
print("Livros disponíveis:")
for livro in listar_livros:
    print(f"- {livro.titulo} by {livro.autor}") 
