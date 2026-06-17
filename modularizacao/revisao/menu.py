# EXEMPLO DO QUE NÃO FAZER
def menu():
    print("Menu de Raças de Cachorros")
    print("1 - Vira-lata")
    print("2 - Poodle")
    print("3 - Labrador")
    print("4 - Bulldog")
    print("5 - Beagle")
    print("6 - Chihuahua")
    print("0 - Sair")
    opcao = input("Digite a opção: ")

    match opcao:
        case "1":
            return "Vira-lata"
        case "2":
            return "Poodle"
        case "3":
            return "Labrador"
        case "4":
            return "Bulldog"
        case "5":
            return "Beagle"
        case "6":
            return "Chihuahua"
        case "0":
            return None
        case _:
            print("Opção inválida")
            return None
