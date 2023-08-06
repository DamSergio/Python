import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            # if board[row][col] == None:
            #     board[row][col] = "*"
            #     bombs_planted += 1

            if board[row][col] == "*":
                continue

            board[row][col] = "*"
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue

                self.board[r][c] = self.get_num_neighboring_bomb(r, c)

    def get_num_neighboring_bomb(self, row, col):
        num_neighboring_bombs = 0

        for r in range(max(0, row - 1), min(self.dim_size, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dim_size, (col + 1) + 1)):
                if r == row and c == col:
                    continue

                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == "*":
            return False
        
        if self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row - 1), min(self.dim_size, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dim_size, (col + 1) + 1)):
                if (r, c) in self.dug:
                    continue

                self.dig(r, c)
        
        return True

    def __str__(self): #Es el toString de Java
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
                
        string_rep = ""
        widths = []

        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        indices = [i for i in range(self.dim_size)]
        indices_row = "   "
        cells = []

        for idx, col in enumerate(indices):
            form = "%-" + str(widths[idx]) + "s"
            cells.append(form % (col))
        
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []

            for idx, col in enumerate(row):
                form = "%-" + str(widths[idx]) + "s"
                cells.append(form % (col))
            
            string_rep += " |".join(cells)
            string_rep += " |\n"
        
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len

        return string_rep

def play(dim_size = 10, num_bombs = 10):
    #Paso 1: crear el tablero y poner las bombas
    board = Board(dim_size, num_bombs)
    #Paso 2: mostrar el tablero y preguntar donde quiere buscar
    #Paso 3a: si es una bomba se acaba el juego
    #Paso 3b: si no es una bomba, cavar todos los agujeros hasta que todos esten al lado de una bomba

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        #El re.split separa por el primer parametro (",(\\s)*") "," es por donde separa
        #"(\\s)*" elimina espacios en blanco " " despues de la coma
        user_input = re.split(",(\\s)*", input("Donde quieres cavar? Inserta fila, columna: "))
        row, col = int(user_input[0]), int(user_input[-1])

        if 0 > row >= board.dim_size or 0 > col >= board.dim_size:
            print("Coordenadas invalidas, prueba de nuevo")
            continue

        safe = board.dig(row, col)

        if not safe:
            break

    if safe:
        print("Felicidades, has ganado")

    else:
        print("Has perdido :(")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == "__main__":
    play()
