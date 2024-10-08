import numpy as np

# Definimos los tableros iniciales
initial_boards = [
    np.array([[-1, 0,  1],
              [ 1, -1, 0],
              [ 0,  0,  0]])
]

class Gato:
    def __init__(self, board=None):
        # Inicializa el tablero, si no se proporciona uno, usa uno vacío
        self.board = np.zeros((3, 3), dtype=int) if board is None else board
        # Jugador inicial, 1 para MAX (x) y -1 para MIN (o)
        self.player = 1

    def __str__(self):
        # Representa el tablero para imprimirlo
        return '\n'.join([' '.join(['x' if cell == 1 else 'o' if cell == -1 else '.' for cell in row]) for row in self.board])

    def change_player(self):
        # Cambia al otro jugador multiplicando por -1
        self.player *= -1

    def actions(self, state):
        # Devuelve las coordenadas de las posiciones vacías
        return [(i, j) for i in range(3) for j in range(3) if state[i, j] == 0]

    def result(self, state, action):
        # Devuelve una copia del estado con la acción aplicada
        new_state = np.copy(state)
        new_state[action] = self.player
        return new_state

    def is_terminal(self, state):
        # Verifica si hay un ganador o empate
        for row in state:
            if abs(sum(row)) == 3:  # fila completa con el mismo jugador
                return True
        for col in state.T:
            if abs(sum(col)) == 3:  # columna completa con el mismo jugador
                return True
        if abs(state[0, 0] + state[1, 1] + state[2, 2]) == 3:  # diagonal principal
            return True
        if abs(state[0, 2] + state[1, 1] + state[2, 0]) == 3:  # diagonal secundaria
            return True
        return not any(0 in row for row in state)  # empate si no hay espacios vacíos

    def utility(self, state):
        # Retorna la utilidad del estado
        for row in state:
            if sum(row) == 3: return 1  # MAX gana
            if sum(row) == -3: return -1  # MIN gana
        for col in state.T:
            if sum(col) == 3: return 1
            if sum(col) == -3: return -1
        if state[0, 0] + state[1, 1] + state[2, 2] == 3: return 1
        if state[0, 0] + state[1, 1] + state[2, 2] == -3: return -1
        if state[0, 2] + state[1, 1] + state[2, 0] == 3: return 1
        if state[0, 2] + state[1, 1] + state[2, 0] == -3: return -1
        return 0  # empate o estado no terminal

def max_value(game, state, alpha, beta):
    if game.is_terminal(state):
        return game.utility(state), None
    v, move = -np.inf, None
    for action in game.actions(state):
        v2, _ = min_value(game, game.result(state, action), alpha, beta)
        if v2 > v:
            v, move = v2, action
        alpha = max(alpha, v)
        if v >= beta:
            break  # poda
    return v, move

def min_value(game, state, alpha, beta):
    if game.is_terminal(state):
        return game.utility(state), None
    v, move = np.inf, None
    for action in game.actions(state):
        v2, _ = max_value(game, game.result(state, action), alpha, beta)
        if v2 < v:
            v, move = v2, action
        beta = min(beta, v)
        if v <= alpha:
            break  # poda
    return v, move

def alphabeta(game):
    state = game.board
    alpha, beta = -np.inf, np.inf
    if game.player == 1:
        return max_value(game, state, alpha, beta)
    else:
        return min_value(game, state, alpha, beta)

# Función para jugar turnos alternos hasta que el juego termine
def play_game(board):
    game = Gato(board)
    while not game.is_terminal(game.board):
        print(f"Jugador {game.player} está jugando")
        print(game)
        value, move = alphabeta(game)
        if move is not None:
            game.board = game.result(game.board, move)
        game.change_player()
        print()

    # Mostrar resultado final
    print("Juego terminado")
    print(game)
    if game.utility(game.board) == 1:
        print("MAX (x) gana")
    elif game.utility(game.board) == -1:
        print("MIN (o) gana")
    else:
        print("Empate")

# Ejecuta el juego con el tablero inicial proporcionado
play_game(initial_boards[0])


