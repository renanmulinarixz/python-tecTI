from models.usuario import Usuario
from servicos.controle_gastos import ControleGastos
from utils.arquivo import salvar_dados


def menu():

    print("\nSISTEMA DE MESADA")
    print("1 - Registrar entrada (mesada)")
    print("2 - Registrar gasto")
    print("3 - Ver resumo")
    print("4 - Ver gastos por categoria")
    print("5 - Salvar e sair")
    print("===")


def main():

    nome = input("Digite o nome do usuário: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))

    usuario = Usuario(nome, saldo_inicial)
    controle = ControleGastos(usuario)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            valor = float(input("Valor da entrada: "))
            descricao = input("Descrição (ex: mesada, bônus): ")

            controle.registrar_entrada(valor, descricao)
            print("Entrada registrada com sucesso!")


        elif opcao == "2":
            valor = float(input("Valor do gasto: "))
            categoria = input("Categoria (lanchonete, cinema, academia, etc): ")
            descricao = input("Descrição do gasto: ")

            controle.registrar_gasto(valor, categoria, descricao)
            print("Gasto registrado com sucesso!")

        elif opcao == "3":
            resumo = usuario.resumo()
            print("\n RESUMO")
            print(f"Nome: {resumo['nome']}")
            print(f"Saldo atual: {resumo['saldo']:.2f}")
            print(f"Total de transações: {resumo['total_transacoes']}")

 
        elif opcao == "4":
            print("\nGASTOS POR CATEGORIA")
            dados = controle.listar_gastos_por_categoria()

            if not dados:
                print("Nenhum gasto registrado ainda.")
            else:
                for categoria, valor in dados.items():
                    print(f"{categoria}: {valor:.2f}")

        
        elif opcao == "5":
            salvar_dados(usuario)
            print("Dados salvos. Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
