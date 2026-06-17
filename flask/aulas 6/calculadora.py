import math
from flask import render_template, request


def verificar_negativo(num):
    """Retorna True se o número for >= 0, False se negativo."""
    return num >= 0


def calcular():
    try:
        num1 = float(request.form["num1"])
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Erro: valor inválido para o primeiro número.",
            resultados="",
        )

    operacao = request.form["operacao"]

    # ── Operações que usam apenas num1 ──────────────────────────────────────
    match operacao:

        case "sqrt":
            if not verificar_negativo(num1):
                resultado = "Erro: número negativo"
                etapas = f"Não existe raiz real de {num1}."
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"
            return render_template(
                "calculadora.html", etapas=etapas, resultados=resultado
            )

        case "log":
            # log na base 10; exige num1 > 0
            if num1 <= 0:
                resultado = "Erro: logaritmo indefinido"
                etapas = f"log({num1}) não existe (número deve ser > 0)."
            else:
                resultado = math.log10(num1)
                etapas = f"log₁₀({num1}) = {resultado}"
            return render_template(
                "calculadora.html", etapas=etapas, resultados=resultado
            )

        case "ln":
            # logaritmo natural; exige num1 > 0
            if num1 <= 0:
                resultado = "Erro: logaritmo indefinido"
                etapas = f"ln({num1}) não existe (número deve ser > 0)."
            else:
                resultado = math.log(num1)
                etapas = f"ln({num1}) = {resultado}"
            return render_template(
                "calculadora.html", etapas=etapas, resultados=resultado
            )

    # ── Operações que usam num1 e num2 ──────────────────────────────────────
    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="",
        )

    try:
        num2 = float(num2_valor)
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Erro: valor inválido para o segundo número.",
            resultados="",
        )

    match operacao:

        case "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        case "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        case "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"

        case "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
                etapas = f"Não é possível dividir {num1} por zero."
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

        case "**":
            resultado = math.pow(num1, num2)
            etapas = f"{num1} ^ {num2} = {resultado}"

        case "bhaskara":
            # num1 = a, num2 = b; c vem de um campo extra
            c_valor = request.form.get("num3", "").strip()
            if not c_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe o coeficiente C para a fórmula de Bhaskara.",
                    resultados="",
                )
            try:
                c = float(c_valor)
            except ValueError:
                return render_template(
                    "calculadora.html",
                    etapas="Erro: valor inválido para o coeficiente C.",
                    resultados="",
                )

            a, b = num1, num2
            delta = b**2 - 4 * a * c
            etapas_lista = [
                f"Equação: {a}x² + {b}x + {c} = 0",
                f"Δ = b² − 4ac = {b}² − 4×{a}×{c} = {delta}",
            ]

            if a == 0:
                etapas = " | ".join(etapas_lista) + " | a ≠ 0 é obrigatório."
                resultado = "Erro: coeficiente 'a' não pode ser zero."
            elif delta < 0:
                etapas = " | ".join(etapas_lista) + " | Δ < 0: sem raízes reais."
                resultado = "Sem raízes reais (Δ < 0)"
            elif delta == 0:
                x = -b / (2 * a)
                etapas_lista.append(f"x = −b / 2a = {x}")
                etapas = " | ".join(etapas_lista)
                resultado = f"x = {x}"
            else:
                sqrt_delta = math.sqrt(delta)
                x1 = (-b + sqrt_delta) / (2 * a)
                x2 = (-b - sqrt_delta) / (2 * a)
                etapas_lista.append(f"√Δ = {sqrt_delta}")
                etapas_lista.append(f"x₁ = (−{b} + {sqrt_delta}) / (2×{a}) = {x1}")
                etapas_lista.append(f"x₂ = (−{b} − {sqrt_delta}) / (2×{a}) = {x2}")
                etapas = " | ".join(etapas_lista)
                resultado = f"x₁ = {x1}   |   x₂ = {x2}"

        case _:
            etapas = "Operação desconhecida."
            resultado = ""

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)