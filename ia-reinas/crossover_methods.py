# crossover_methods.py
import numpy as np

def one_point_crossover(parent1, parent2):
    size = len(parent1)
    crossover_point = np.random.randint(1, size)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def n_point_crossover(parent1, parent2, n_points=2):
    size = len(parent1)
    crossover_points = sorted(np.random.choice(range(1, size), n_points, replace=False))
    child1, child2 = parent1.copy(), parent2.copy()
    swap = False
    current_index = 0
    
    for point in crossover_points:
        if swap:
            child1[current_index:point], child2[current_index:point] = child2[current_index:point], child1[current_index:point]
        swap = not swap
        current_index = point

    if swap:
        child1[current_index:], child2[current_index:] = child2[current_index:], child1[current_index:]
    
    return child1, child2

def uniform_crossover(parent1, parent2):
    size = len(parent1)
    child1, child2 = parent1.copy(), parent2.copy()
    
    for i in range(size):
        if np.random.rand() > 0.5:
            child1[i], child2[i] = child2[i], child1[i]
    
    return child1, child2


