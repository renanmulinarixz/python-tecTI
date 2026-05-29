
# Crie uma classe de mercearia com atributos como nome do produto, preço e quantidade em estoque. 
# Implemente métodos para comprar um produto (diminuindo a quantidade em estoque) e para mostrar as informações do produto.



class Mercearia:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def comprar(self, quantidade_comprada):
        if quantidade_comprada <= self.quantidade:
            self.quantidade -= quantidade_comprada
            total = quantidade_comprada * self.preco
            print(f"Você comprou {quantidade_comprada} {self.nome}(s) por R${total:.2f}.")
        else:
            print(f"Desculpe, não temos {quantidade_comprada} {self.nome}(s) disponíveis. Temos apenas {self.quantidade}.")
    
    def mostrar_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade disponível: {self.quantidade}")  


banana = Mercearia("Coca-cola", 9.50, 100)
banana.mostrar_informacoes()  
banana.comprar(50)
banana.mostrar_informacoes()
