import numpy as np
import matplotlib.pyplot as plt


NUM_REINAS = 8

np.random.seed(12345)

# a) Construye el problema de las n reinas donde se colocan n piezas reinas en un tablero de ajedrez de tamaño n×n. La posición inicial de las reinas es aleatoria.
class Board():
    """Problemas de las k reinas"""
    def __init__(self, size=NUM_REINAS):
        #Tamaño del tablero
        self.size = size
        #Piezas en el tablero
        get_row = lambda size, shift: [{"type": (cell_index + shift) % 2, "piece": None} 
                                       for cell_index in range(size)]
        self.board = [get_row(self.size, _ % 2) for _ in range(self.size)]
        self.queen_board = np.zeros((size, size))
        
    def __str__(self):
        return str([[cell["type"] if cell["piece"]==None else cell["piece"] for cell in row] for row in self.board])

    def put(self, piece: str, cell: tuple) -> bool:
        """Coloca una pieza en una configuración del tablero"""
        row, column = cell
        self.board[row][column]['piece'] = piece
        
    def create_array(self):
        """Crea una matriz con la información del tablero"""
        self.queen_board = np.zeros((self.size, self.size))
        for i,row in enumerate(self.board):
            for j in range(self.size):
                if row[j]['piece'] == 'Q':
                    self.queen_board[i][j] = 1
                    
    def put_pieces(self, num=NUM_REINAS, init='init', piece='Q'):
        """Coloca un número num de piezas en el tablero ya sea en configuración
        aleatoria o en alguna otra."""
        if init == 'random':
            elements = range(num)
            for i in elements:
                row, column = np.random.choice(elements), np.random.choice(elements)
                self.put(piece=piece, cell=(row,column))
        elif init == 'init':
            for pos in [(0,6),(1,4),(2,1),(3,3),(4,5),(5,7),(6,2),(7,0)][:num]:
                self.put(piece=piece, cell=pos)
        self.create_array()
                    
    def move(self, i,j):
        """Acción de mover una pieza"""
        s_p = self.board[i][j]
        if s_p['piece'] != 'Q':
            pass
        else:
            m,n = np.random.choice(range(self.size)), np.random.choice(range(self.size))
            s_q = self.board[m][n]
            if s_q['piece'] != 'Q':
                self.board[i][j]['piece'] = None
                self.queen_board[i][j] = 0
                self.board[m][n]['piece'] = 'Q'
                self.queen_board[m][n] = 1
                #self.create_array()
            else:
                self.move(i,j)
    
    def draw(self):
        """Dibuja el tablero"""
        img_board = np.array([[cell["type"] if cell["piece"]==None else 0.5 for cell in row] for row in self.board])
        plt.imshow(img_board, cmap='Greys')
        plt.axis('off')
        plt.show()
        


#Crea el problema
board = Board(size=NUM_REINAS)
board.put_pieces(num=NUM_REINAS, init='line')

#Visualiza el problema
board.draw()

def get_population(s=7):
    """Genera una población de genes de tamaño s"""
    population = []
    for i in range(s):
        population.append(np.random.choice(NUM_REINAS, size=NUM_REINAS, replace=False)+1)
    return population

def get_scores(population, fitness_function):
    """Obtiene probabilidades a partir de la función fitness"""
    partition = 0
    probs = np.zeros(len(population))
    for i, subject in enumerate(population):
        score = fitness_function(subject)
        exp = np.exp(score)
        probs[i] = exp
        partition += exp
    
    return probs/partition

def get_board(array):
    """Dibuja la solución a partir de los genes"""
    new_board = Board(size=NUM_REINAS)
    for x,y in enumerate(array):
        new_board.put(piece='Q', cell=(x,y-1))
        
    return new_board

# b) Define la función fitness como el negativo del total de reinas que se están amenazando entre sí. El valor máximo debe ser 0.́

def fitness(array, s = NUM_REINAS):
    """Función fitness para el problema de 8 reinas"""
    matrix = np.zeros((s,s))
    for i,j in enumerate(array):
        matrix[i,j-1] = 1
    
    err = 0
    queens = np.stack(np.where(matrix == 1)).T
    for i,j in queens:
        for k in range(1,s+1):
            #Revisa la diagonal
            if i+k<s and j+k<s:
                if [i+k,j+k] in queens.tolist():
                    err += 1
            if i-k>=0 and j-k>=0: 
                if [i-k,j-k] in queens.tolist():
                    err += 1
            if i-k>=0 and j+k<s:
                if matrix[i-k, j+k] ==1:
                    err += 1
            if i+k<s and j-k>=0:
                if matrix[i+k, j-k] ==1:
                    err += 1
                    
            #Revisa las columnas
            if i+k<s:
                if matrix[i+k,j]== 1:
                    err += 1
            if i-k >= 0:
                if matrix[i-k,j]== 1:
                    err += 1
            
            #Revisa los renglones
            if j+k<s:
                if matrix[i,j+k]== 1:
                    err += 1
            if j-k >= 0:
                if matrix[i,j-k]== 1:
                    err += 1
    return -err

# c) Define la función de selección con los siguientes métodos:
#  Ruleta
#  Aleatorio
#  Ranking

def selection(population, weights, size=2, method='Roulette'):
    """Función de selección"""
    if method == 'Roulette':
        idx1, idx2 = np.random.choice(range(len(population)), replace=False, size=size, p=weights)
        return population[idx1], population[idx2]
    elif method == 'Random':
        idx1, idx2 = np.random.choice(range(len(population)), replace=False, size=size)
        return population[idx1], population[idx2]
    elif method == 'Ranking':
        sorted_indices = np.argsort(weights)
        selected_indices = np.random.choice(sorted_indices, size=size)
        return population[selected_indices[0]], population[selected_indices[1]]


# d) Define la fuinción de reproducción con los siguientes métodos:

# 1 punto

# n puntos

# uniforme
