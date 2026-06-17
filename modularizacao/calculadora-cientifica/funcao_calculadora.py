import divisao
import divisaointeira
import logaritmo
import potencia
import raiz
import soma
import subtrair
import multiplicar

def calculadora():
    print("\n--- CALCULADORA TERCEIRÃO: MODO MULTI-OPERACIONAL ---")
    
    try:
        a = float(input("Digite o primeiro número (a): "))
        b = float(input("Digite o segundo número (b): "))
        print("-" * 40)
        print(f"Soma: {soma.somar(a, b)}")
        print(f"Subtração: {subtrair.subtrair(a, b)}")
        print(f"Multiplicação: {multiplicar.multiplicar(a, b)}")
        
        try:
            print(f"Divisão: {divisao.divisao(a, b)}")
        except ValueError as e:
            print(f"Divisão: {e}")

        try:
            print(f"Divisão Inteira: {divisaointeira.divisaointeira(a, b)}")
        except ValueError as e:
            print(f"Divisão Inteira: {e}")

        print(f"Potência: {potencia.potencia(a, b)}")

        try:
            log_a, log_b = logaritmo.logaritmo(a, b)
            print(f"Logaritmo de a: {log_a}, Logaritmo de b: {log_b}")
        except ValueError as e:
            print(f"Logaritmo: {e}")
        raiz_a, raiz_b = raiz.raiz(a, b)
        print(f"Raiz de a: {raiz_a}, Raiz de b: {raiz_b}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos (use ponto para decimais).")
