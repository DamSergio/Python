altura = int(input("Dime la altura de la piramide: "))

for capa in range(altura):
    linea = ""

    for espacio in range(capa, altura - 1):
        linea += "  "

    for bloque in range(1, (capa + 1) * 2):
        linea += "* "
    
    print(linea)