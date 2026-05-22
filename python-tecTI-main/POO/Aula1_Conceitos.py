#atributos e  métodos que um objeto pode ter


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor} em {self.ano}."




meu_livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
print(meu_livro.titulo)  # Saída: O Senhor dos Anéis
print(meu_livro.descricao())  # Saída: O Senhor dos Anéis foi escrito por J.R.R. Tolkien em 1954.
