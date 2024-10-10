# n_queens.py
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12345)

class Board:
    
    def __init__(self, size=8):
        self.size = size
        self.queens = np.random.permutation(size)

    def __str__(self):
        """Muestra el tablero en formato de texto."""
        board = np.zeros((self.size, self.size))
        for row, col in enumerate(self.queens):
            board[row][col] = 1
        return str(board)

    def draw(self):
        """Dibuja el tablero con las reinas."""
        board = np.zeros((self.size, self.size))
        for row, col in enumerate(self.queens):
            board[row][col] = 1
        plt.imshow(board, cmap='Greys', extent=[0, self.size, 0, self.size])
        plt.xticks([])
        plt.yticks([])
        plt.show()

def calculate_fitness(queens):
    n = len(queens)
    conflicts = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                conflicts += 1

    return -conflicts


