

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca # define a marca
        self.modelo = modelo # define modelo
        self.ano = ano #ano do carro
        self.velocidade = 0 #velocidade

    def acelerar(self):
        self.velocidade += 30 #aumenta a velocidade em 30 km/h
        print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 30 #diminui a velocidade em 30 km/h
        if self.velocidade < 0:
            self.velocidade = 0 #garante que a velocidade não seja negativa
        print(f"O carro freou. Velocidade atual: {self.velocidade} km/h")
    
    def imprimir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


meu_carro = Carro("Toyota", "Corolla", 2020)
# meu_carro.imprimir_informacoes() 


# meu_carro.acelerar()
# meu_carro.acelerar()
# meu_carro.frear()
# meu_carro.frear()
# meu_carro.acelerar()
# meu_carro.frear()  # Testa frear mais vezes para garantir que a velocidade não fique negativa

# carro_novo = Carro("Honda", "Civic", 2022)
# carro_novo.imprimir_informacoes()
# carro_novo.acelerar()
# carro_novo.frear()

##############################################################################################
'''
Agora fazendo um menu para interagir com o usuário

'''

# while True:
#     print("\nMenu:")
#     print("1. Acelerar")
#     print("2. Frear")
#     print("3. Imprimir informações do carro")
#     print("4. Sair")

#     escolha = input("Escolha uma opção: ")

#     if escolha == "1":
#         meu_carro.acelerar()
#     elif escolha == "2":
#         meu_carro.frear()
#     elif escolha == "3":
#         meu_carro.imprimir_informacoes()
#     elif escolha == "4":
#         print("Saindo do programa.")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")

###########################################################################################
''' 
Cadastro o carro no menu, para criar um novo carro e interagir com ele'''

while True:
    print("\nMenu:")
    print("1. Cadastrar novo carro")
    print("2. Acelerar")
    print("3. Frear")
    print("4. Imprimir informações do carro")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = int(input("Digite o ano do carro: "))
        meu_carro = Carro(marca, modelo, ano)
        print("Carro cadastrado com sucesso!")
    elif escolha == "2":
        if 'meu_carro' in locals():
            meu_carro.acelerar()
        else:
            print("Nenhum carro cadastrado. Por favor, cadastre um carro primeiro.")
    elif escolha == "3":
        if 'meu_carro' in locals():
            meu_carro.frear()
        else:
            print("Nenhum carro cadastrado. Por favor, cadastre um carro primeiro.")
    elif escolha == "4":
        if 'meu_carro' in locals():
            meu_carro.imprimir_informacoes()
        else:
            print("Nenhum carro cadastrado. Por favor, cadastre um carro primeiro.")
    elif escolha == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")


        
