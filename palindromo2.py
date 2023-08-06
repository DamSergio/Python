def es_palindromo(texto):
    return quitar_espacios(texto).lower() == quitar_espacios(voltear_texto(texto)).lower()

def quitar_espacios(texto):
    return texto.replace(" ", "")

def voltear_texto(texto):
    pal = ""
    for char in reversed(texto):
        pal += char
    return pal

print("abba", es_palindromo("abba"))
print("amo la paloma", es_palindromo("amo la paloma"))