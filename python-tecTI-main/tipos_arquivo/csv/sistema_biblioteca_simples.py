import pandas as pd
import datetime as dt



while True:
    livros_disponiveis = ["O Senhor dos Anéis", "A Bela e a Fera", "Devoradores de Estrelas", "Orgulho e Preconceito",
                      "Apostila de Python do Cotemig"]
    print("Bem vindo ao cotemig biblioteca!")
    for i in range(len(livros_disponiveis)):
        print(f"- {i+1} {livros_disponiveis[i]}")
    escolha = input("Digite o número do livro que deseja emprestar ou '0' para encerrar: ")
    if escolha == '0':
        print("Obrigado por usar a biblioteca do Cotemig!")
        break
    elif 1 <= int(escolha) <= len(livros_disponiveis):
        nome = input("Digite seu nome: ")
        data_emprestimo = dt.datetime.now()
        data_devolucao = data_emprestimo + dt.timedelta(days=14)
        print(f"Livro '{livros_disponiveis[int(escolha)-1]}' emprestado para {nome}. Data de devolução: {data_devolucao.strftime('%Y-%m-%d')}")
        livros_disponiveis.remove(livros_disponiveis[int(escolha)-1])
    else:
        print("Livro não disponível. Por favor, escolha outro livro ou digite '0' para encerrar.")  
    livros = pd.DataFrame(livros_disponiveis, columns=["titulo"])
    livros.to_csv("livros_disponiveis_atualizado.csv", index=False, encoding="utf-8")
