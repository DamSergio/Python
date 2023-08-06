import random
import math

class Player:
    def __init__(self, letter):
        #letter es "x" o "o"
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8): ")
            try:
                val = int(square)

                if val not in game.available_moves():
                    raise ValueError
                
                valid_square = True
            
            except ValueError:
                print("Invalid square. Try again.")
        
        return val

#algoritmo minimax
class GeniusComputerPlayer(Player):
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        
        else:
            square = self.minimax(game, self.letter)["position"]
        
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        opponent = "O" if player == "X" else "X"

        if state.current_winner == opponent:
            return {"position": None,
                    "score": 1 * (state.nums_empty_squares() + 1) if opponent == max_player else -1 * (state.nums_empty_squares() + 1)}
        
        elif not state.empty_squares():
            return {"position": None,
                    "score": 0}
        
        if player == max_player:
            best = {"position": None,
                    "score": -math.inf}
        else:
            best = {"position": None,
                    "score": math.inf}
        
        for possible_move in state.available_moves():
            #paso 1: hacer un movimiento
            state.make_move(possible_move, player)
            #paso 2: recursividad usando minimax para simular una partida con ese movimiento
            sim_score = self.minimax(state, opponent) #alterno el jugador
            #paso 3: desago el movimiento
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move
            #paso 4: actualizar disccionario si es necesario
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        
        return best