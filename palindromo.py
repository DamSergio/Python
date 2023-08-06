numero = 129
aux = numero
palindromo = 0

while aux > 0:
    palindromo += aux % 10
    palindromo *= 10
    aux //= 10

palindromo //= 10

if numero == palindromo:
    print(f"El numero {numero} es un palindromo")
else:
    print(f"El numero {numero} no es un palindromo")