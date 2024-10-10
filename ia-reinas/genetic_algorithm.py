import numpy as np
from selection_methods import roulette_wheel_selection, random_selection, ranking_selection
from crossover_methods import one_point_crossover, n_point_crossover, uniform_crossover
from mutation_methods import flipping_mutation, swap_mutation, reverse_mutation
from n_queens import Board, calculate_fitness

class GeneticAlgorithm:
    def __init__(self, problem, population_size=8, max_iterations=10, mutation_rate=0.1):
        self.problem = problem
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.mutation_rate = mutation_rate

    def weak_replacement(self, population, children, fitnesses):
        population_fitnesses = [calculate_fitness(board) for board in population]
        
        combined_population = np.concatenate((population, children))
        combined_fitnesses = np.concatenate((population_fitnesses, fitnesses))
        
        sorted_indices = np.argsort(combined_fitnesses)[::-1]  
        new_population = combined_population[sorted_indices][:self.population_size]  
        
        return new_population

    def run(self):
        population = [Board(size=10).queens for _ in range(self.population_size)]
        fitnesses = [calculate_fitness(board) for board in population]

        selection_methods = [roulette_wheel_selection, random_selection, ranking_selection]
        crossover_methods = [one_point_crossover, n_point_crossover, uniform_crossover]
        mutation_methods = [flipping_mutation, swap_mutation, reverse_mutation]
        
        best_fitness_per_combination = {}

        for selection in selection_methods:
            for crossover in crossover_methods:
                for mutation in mutation_methods:
                    best_fitness = float('-inf')

                
                    for generation in range(self.max_iterations):
                        # Selección
                        if selection == random_selection:
                            selected_population = selection(population, self.population_size)
                        else:
                            selected_population = selection(population, fitnesses, self.population_size)
                        children = []
                        for i in range(0, self.population_size, 2):
                            child1, child2 = crossover(np.array(selected_population[i]), np.array(selected_population[i + 1]))
                            children.extend([child1, child2])

                        mutated_population = [mutation(child) if np.random.rand() < self.mutation_rate else child for child in children]

                        fitnesses = [calculate_fitness(board) for board in mutated_population]

                        population = self.weak_replacement(population, mutated_population, fitnesses)
                        
                        current_best_fitness = max(fitnesses)
                        if current_best_fitness > best_fitness:
                            best_fitness = current_best_fitness

                    best_fitness_per_combination[(selection.__name__, crossover.__name__, mutation.__name__)] = best_fitness

                    print(f"Selection: {selection.__name__}, Crossover: {crossover.__name__}, Mutation: {mutation.__name__}, Best Fitness: {best_fitness}")

        return best_fitness_per_combination
if __name__ == "__main__":
    problem_size = 10

    ga = GeneticAlgorithm(problem=problem_size)
    results = ga.run()

    print("Resultados de fitness para cada combinación de operadores genéticos:")
    for combination, fitness in results.items():
        print(f"{combination}: {fitness}")






