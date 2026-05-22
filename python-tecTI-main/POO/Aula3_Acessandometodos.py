

class Personagem:
    def __init__(self, nome, poder, dano):
        self.nome = nome
        self.poder = poder
        self.dano = dano
    
    def usar_poder(self):
        self.poder += 10
        print(f"{self.nome} usou seu poder! Poder atual: {self.poder}")

    def atacar(self):
        print(f"{self.nome} atacou causando {self.dano} de dano!")
    
goku = Personagem("Goku", 100, 50)
# goku.usar_poder()
# goku.atacar()
monstro = Personagem("Monstro", 80, 40)
# monstro.atacar()

################################################################################################
while True:
    print("\nMenu \n escolha seu personagem:")
    print("1. Goku")
    print("2. Monstro") 
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        goku.usar_poder()
        goku.atacar()
    elif escolha == "2":
        monstro.atacar()
    else:
        print("Opção inválida. Tente novamente.")   
