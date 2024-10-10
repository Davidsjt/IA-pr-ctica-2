# main.py
from genetic_algorithm import genetic_algorithm
from n_queens import Board

def evaluate_10_queens():
    # Definir las combinaciones de operadores genéticos
    selection_methods = ['roulette', 'random', 'ranking']
    crossover_methods = ['one_point', 'n_point', 'uniform']
    mutation_methods = ['flipping', 'swap', 'reverse']
    
    # Parámetros del problema
    board_size = 10  # 10 reinas
    population_size = 8  # Tamaño de la población
    max_generations = 10  # Máximo de 10 iteraciones
    
    # Evaluar todas las combinaciones de operadores genéticos
    for selection in selection_methods:
        for crossover in crossover_methods:
            for mutation in mutation_methods:
                print(f"Evaluando combinación: Selección: {selection}, Cruce: {crossover}, Mutación: {mutation}")
                
                # Ejecutar el algoritmo genético con la combinación actual
                best_solution, best_fitness = genetic_algorithm(
                    population_size=population_size,
                    board_size=board_size,
                    max_generations=max_generations,
                    crossover_method=crossover,
                    mutation_method=mutation,
                    selection_method=selection,
                    mutation_rate=0.1  # Tasa de mutación fija
                )
                
                # Si se encuentra la solución perfecta (fitness == 0)
                if best_fitness == 0:
                    print(f"Solución perfecta encontrada con combinación: Selección: {selection}, Cruce: {crossover}, Mutación: {mutation}")
                    print(f"Mejor solución (posiciones de las reinas): {best_solution}")
                    
                    # Imprimir el tablero con la mejor solución
                    board = Board(board_size)
                    board.queens = best_solution  # Colocar la mejor solución en el tablero
                    print("Tablero de ajedrez:")
                    print(board)  # Mostrar el tablero en texto
                    
                    # Dibujar el tablero
                    board.draw()
                    
                    # Salir del bucle ya que se encontró la solución perfecta
                    return

if __name__ == "__main__":
    evaluate_10_queens()






