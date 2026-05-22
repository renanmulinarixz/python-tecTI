import ler_arquivo as la
import menu
import datetime as dt


dados = la.ler_arquivo()
raca = menu.menu()

if raca:
    peso = dados.get(raca)
    preco = peso * 2.5

    print(f"Raça: {raca}")
    print(f"Peso: {peso} kg")
    print(f"Preço: R$ {preco}")
