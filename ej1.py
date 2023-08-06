print("""
Bienvenidos a la calculadora
para salir escribe Salir
Las opereaciones son: suma, multi, div, resta
""")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingresa numero: ")

        if resultado.lower() == "salir":
            break
        
        resultado = int(resultado)

    operacion = input("Ingresa operacion: ")

    if operacion == "salir":
        break

    operando = input("Ingresa siguiente numero: ")

    if operando == "salir":
        break

    operando = int(operando)

    if operacion.lower() == "suma":
        resultado += operando

    elif operacion.lower() == "resta":
        resultado -= operando

    elif operacion.lower() == "multi":
        resultado *= operando

    elif operacion.lower() == "div":
        resultado /= operando

    print(f"El resultado es {resultado}.")
