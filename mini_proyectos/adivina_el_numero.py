import random

def es_numero(n):
    try:
        int(n)
        return int(n)
    except ValueError:
        print("La cadena introducida no es valida")
        return 0
    
def comprobar(n_r, n_j):
    if n_r != n_j:
        print("El numero que has introducido es incorrecto, intentalo de nuevo")
    else:
        print(f"Felicidades, has acertado el numero, el numero correcto era: {n_r}")

numero_random = random.randint(1, 10)
numero_jugador = 0
print("En este juego tienes que adivinar un numero entre el 1 y el 10", numero_random)

while numero_random != numero_jugador:
    numero_jugador = input("Insereta el numero que creas que es: ")
    numero_jugador = es_numero(numero_jugador)
    comprobar(numero_random, numero_jugador)