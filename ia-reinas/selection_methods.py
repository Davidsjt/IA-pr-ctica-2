import numpy as np

def roulette_wheel_selection(population, fitnesses, num_selected=2):
    total_fitness = np.sum(fitnesses)
    probabilities = fitnesses / total_fitness
    selected_indices = np.random.choice(len(population), size=num_selected, replace=False, p=probabilities)
    selected = [population[i] for i in selected_indices]
    return selected

def random_selection(population, num_selected=2):
    selected_indices = np.random.choice(len(population), size=num_selected, replace=False)
    selected = [population[i] for i in selected_indices]
    return selected

def ranking_selection(population, fitnesses, num_selected=2):
    sorted_indices = np.argsort(fitnesses)[::-1]
    sorted_population = [population[i] for i in sorted_indices]
  
    ranks = np.arange(1, len(population) + 1)
    probabilities = ranks / np.sum(ranks)
    
    selected_indices = np.random.choice(len(sorted_population), size=num_selected, replace=False, p=probabilities)
    selected = [sorted_population[i] for i in selected_indices]
    return selected



