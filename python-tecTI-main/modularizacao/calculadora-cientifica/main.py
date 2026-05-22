import funcao_calculadora

if __name__ == "__main__":
    print("Bem-vindo ao Sistema Calculadora Terceirão.")
    input("Pressione Enter para iniciar a calculadora...")

    while True:
        # chama sua função principal
        funcao_calculadora.calculadora()

        # pergunta se quer continuar
        opcao = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()

        if opcao == "n":
            print("Encerrando a calculadora... Até mais!")
            break
        elif opcao != "s":
            print("Opção inválida. Continuando...")

# pip install pyinstaller
#   pip install pyinstaller  
##pyinstaller --onefile main.py  
