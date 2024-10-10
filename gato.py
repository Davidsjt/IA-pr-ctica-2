import numpy as np

initial_boards = [ 
    np.array([[ 0, 0, 0],
              [ 0, 1, 0],
              [ 0, 0, -1]])
]

class Gato:
    def __init__(self, board=None):
        self.board = np.zeros((3, 3), dtype=int) if board is None else board
        self.player = 1  # MAX (1) empieza siempre

    def __str__(self):
        return '\n'.join(['|'.join(['x' if cell == 1 else 'o' if cell == -1 else ' ' for cell in row]) for row in self.board])

    def change_player(self):
        self.player *= -1

    def actions(self, state):
        """Devuelve una lista de todas las posiciones vacías (acciones posibles)."""
        return [(i, j) for i in range(3) for j in range(3) if state[i, j] == 0]

    def result(self, state, action, player):
        """Devuelve un nuevo estado después de aplicar la acción del jugador especificado."""
        new_state = state.copy()
        new_state[action[0], action[1]] = player  
        return new_state

    def is_terminal(self, state):
        """Verifica si el juego ha terminado y devuelve True si es así."""
        return self.utility(state) is not None

    def utility(self, state):
        """Devuelve 1 si gana MAX, -1 si gana MIN, 0 si es empate, y None si el juego sigue."""
        for row in state:
            if abs(sum(row)) == 3:
                return 1 if row[0] == 1 else -1
        for col in state.T:
            if abs(sum(col)) == 3:
                return 1 if col[0] == 1 else -1
        if abs(state[0, 0] + state[1, 1] + state[2, 2]) == 3:
            return 1 if state[0, 0] == 1 else -1
        if abs(state[0, 2] + state[1, 1] + state[2, 0]) == 3:
            return 1 if state[0, 2] == 1 else -1
        if all(state[row][col] != 0 for row in range(3) for col in range(3)):
            return 0
        return None

def max_value(game, state, alpha, beta):
    utility = game.utility(state)
    if utility is not None:
        return utility, None
    v, move = -np.inf, None
    for action in game.actions(state):
        new_state = game.result(state, action, 1)  # Aplicar acción como MAX (jugador 1)
        v2, _ = min_value(game, new_state, alpha, beta)
        if v2 > v:
            v, move = v2, action
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v, move

def min_value(game, state, alpha, beta):
    utility = game.utility(state)
    if utility is not None:
        return utility, None
    v, move = np.inf, None
    for action in game.actions(state):
        new_state = game.result(state, action, -1)  # Aplicar acción como MIN (jugador -1)
        v2, _ = max_value(game, new_state, alpha, beta)
        if v2 < v:
            v, move = v2, action
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v, move

def alphabeta(game):
    """Inicia el algoritmo de alpha-beta en función de quién es el jugador actual."""
    state = game.board
    if game.player == 1:
        return max_value(game, state, -np.inf, np.inf)
    else:
        return min_value(game, state, -np.inf, np.inf)

def play_game(board):
    """Jugar el juego del gato con alpha-beta desde un estado inicial dado."""
    game = Gato(board)
    print(f"Jugador {game.player} está jugando")
    print(game)
    print()  # Línea en blanco para separar las jugadas

    while not game.is_terminal(game.board):
        value, move = alphabeta(game)
        if move is not None:
            game.board = game.result(game.board, move, game.player)
            game.change_player()
            
            # Mostrar el tablero después de cada movimiento con el jugador actual
            print(f"Jugador {game.player} está jugando")
            print(game)
            print()  # Línea en blanco para separar las jugadas
        else:
            break

    print("Juego terminado")
    print(game)

print("Caso 1")

for board in initial_boards:
    for row in board:
        print(' '.join(str(element) for element in row))
    print()
play_game(initial_boards[0])


