import math

def logaritmo(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Os números devem ser positivos para calcular o logaritmo.")
    return math.log(a), math.log(b)
