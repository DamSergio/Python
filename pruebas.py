board = [" " for _ in range(9)]
print(list(range(1, 10)))
print(board[0:3])

for row in [board[i*3:(i+1)*3] for i in range(3)]:
    print("| " + " | ".join(row) + " |")

number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
for row in number_board:
    print("| " + " | ".join(row) + " |")

moves = []

for (i, spot) in enumerate(board):
    if spot == " ":
        moves.append(i)
print(moves)
print(list(enumerate(board)))

print(11 % 10)

print(9**2)

puzzle = [[i + 1 for i in range(j*10, j*10+10)] for j in range(9)]
print(puzzle)

row_start = (2 // 3)
col_start = (1 // 3)
matrix = puzzle[row_start * 3 : (row_start * 3) + 3][col_start * 3 : (col_start * 3) + 3]

print(matrix)

cadena = "".join(["i","n","p","u","t","\ "]).strip()
cadena2 = "hola"
print(cadena+cadena2)

array1 = ["caca", "morsa", "arroz", "si", "cacahuete"]
tupla = {i : len(i) for i in array1}
print(tupla)

caca = {"1,1":"sdf"}
print(caca)

