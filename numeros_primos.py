numero = 33

for i in range(2, numero // 2):
    if (numero % i == 0):
        print(f"El numero {numero} no es primo")
        break
else:
    print(f"El numero {numero} es primo")