# genetic_algorithm.py
import numpy as np
from selection_methods import roulette_wheel_selection, random_selection, ranking_selection
from crossover_methods import one_point_crossover, n_point_crossover, uniform_crossover
from mutation_methods import flipping_mutation, swap_mutation, reverse_mutation
from n_queens import Board, calculate_fitness

def weak_replacement(population, fitnesses, offspring, offspring_fitnesses):
    """
    Realiza un reemplazo débil. Reemplaza a los peores individuos de la población con los hijos generados.
    """
    combined_population = np.concatenate((population, offspring), axis=0)
    combined_fitnesses = np.concatenate((fitnesses, offspring_fitnesses), axis=0)
    
    # Ordenamos a la población combinada según fitness, de mayor a menor (mejores primero)
    sorted_indices = np.argsort(combined_fitnesses)[::-1]
    
    # Mantenemos a los mejores individuos de la población combinada
    new_population = [combined_population[i] for i in sorted_indices[:len(population)]]
    new_fitnesses = [combined_fitnesses[i] for i in sorted_indices[:len(population)]]
    
    return np.array(new_population), np.array(new_fitnesses)

def genetic_algorithm(population_size=100, board_size=8, max_generations=1000, crossover_method='one_point', 
                      mutation_method='flipping', selection_method='roulette', mutation_rate=0.1):
    """
    Ejecuta el algoritmo genético para resolver el problema de las n reinas.
    """
    # Inicializamos la población aleatoria
    population = [Board(board_size).queens for _ in range(population_size)]
    fitnesses = np.array([calculate_fitness(individual) for individual in population])

    # Iteramos a través de las generaciones
    for generation in range(max_generations):
        print(f"Generación {generation} - Mejor fitness: {np.max(fitnesses)}")
        
        if np.max(fitnesses) == 0:
            print("Solución encontrada!")
            break
        
        # Selección de padres
        if selection_method == 'roulette':
            parents = roulette_wheel_selection(population, fitnesses)
        elif selection_method == 'random':
            parents = random_selection(population)
        elif selection_method == 'ranking':
            parents = ranking_selection(population, fitnesses)
        
        # Cruce para generar hijos
        if crossover_method == 'one_point':
            offspring = one_point_crossover(parents[0], parents[1])
        elif crossover_method == 'n_point':
            offspring = n_point_crossover(parents[0], parents[1], n_points=2)
        elif crossover_method == 'uniform':
            offspring = uniform_crossover(parents[0], parents[1])

        offspring = list(offspring)
        
        # Aplicamos mutación a los hijos
        for i in range(len(offspring)):
            if np.random.rand() < mutation_rate:
                if mutation_method == 'flipping':
                    offspring[i] = flipping_mutation(offspring[i])
                elif mutation_method == 'swap':
                    offspring[i] = swap_mutation(offspring[i])
                elif mutation_method == 'reverse':
                    offspring[i] = reverse_mutation(offspring[i])
        
        # Calculamos el fitness de los hijos
        offspring_fitnesses = np.array([calculate_fitness(ind) for ind in offspring])
        
        # Reemplazo débil
        population, fitnesses = weak_replacement(population, fitnesses, offspring, offspring_fitnesses)

    # Retornamos la mejor solución encontrada
    best_solution_index = np.argmax(fitnesses)
    return population[best_solution_index], fitnesses[best_solution_index]

if __name__ == "__main__":
    best_solution, best_fitness = genetic_algorithm(
        population_size=8, 
        board_size=10, 
        max_generations=1000, 
        crossover_method='one_point', 
        mutation_method='flipping', 
        selection_method='roulette', 
        mutation_rate=0.1
    )
    
    print(f"Mejor solución: {best_solution}")
    print(f"Mejor fitness: {best_fitness}")








