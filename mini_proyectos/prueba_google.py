num_inicial = int(input("Dime un numero del cual empezar a contar: "))
found = False

for n in range(num_inicial, 10000000):
    aux = n
    palindromo = 0

    while aux > 0:
        palindromo += aux % 10
        palindromo *= 10
        aux //= 10

    palindromo //= 10

    if n == palindromo:
        for i in range(2, n // 2):
            if (n % i == 0):
                break
        else:
            print(f"El numero {n} es primo")
            found = True
            break
    if found:
        break
