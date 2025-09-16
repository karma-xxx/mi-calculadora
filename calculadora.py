# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División entre cero"
    return a / b

def elevar_al_cubo(numero):
    return numero ** 3

# Ejemplo de uso
if __name__ == "__main__":
    print("Calculadora en Python")
    print("Suma: 5 + 3 =", sumar(5, 3))
    print("Resta: 5 - 3 =", restar(5, 3))
    print("Multiplicación: 5 * 3 =", multiplicar(5, 3))
    print("División: 5 / 3 =", dividir(5, 3))
    print("Elevar al cubo: 3³ =", elevar_al_cubo(3))
    