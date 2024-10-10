# mutation_methods.py
import numpy as np

def flipping_mutation(queens):
    mutated_queens = np.array(queens.copy())
    size = len(mutated_queens)

    row = np.random.randint(0, size)
    
    current_col = mutated_queens[row]
    new_col = np.random.choice([col for col in range(size) if col != current_col])

    mutated_queens[row] = new_col
    
    return mutated_queens

def swap_mutation(queens):
    """Mutación por intercambio: Intercambia las posiciones de dos reinas."""
    mutated_queens = np.array(queens.copy())
    size = len(mutated_queens)

    row1, row2 = np.random.choice(size, size=2, replace=False)
    
    mutated_queens[row1], mutated_queens[row2] = mutated_queens[row2], mutated_queens[row1]
    
    return mutated_queens

def reverse_mutation(queens):
    mutated_queens = np.array(queens.copy())
    size = len(mutated_queens)
 
    point1, point2 = sorted(np.random.choice(size, size=2, replace=False))
   
    mutated_queens[point1:point2 + 1] = mutated_queens[point1:point2 + 1][::-1]
    
    return mutated_queens
