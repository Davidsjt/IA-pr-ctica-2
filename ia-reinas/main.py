# main.py
from genetic_algorithm import GeneticAlgorithm

def main():
    # Definir el tamaño del problema d
    problem_size = 10
    ga = GeneticAlgorithm(problem=problem_size, population_size=8, max_iterations=10)
    results = ga.run()

    # Imprimir los resultados finales del mejor fitness para cada combinación
    print("Resultados de fitness para cada combinación de operadores genéticos:")
    for combination, fitness in results.items():
        print(f"{combination}: {fitness}")

if __name__ == "__main__":
    main()




