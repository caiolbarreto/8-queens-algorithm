import random
from DNA import DNA
from utils import integer_to_binary

class Population:
    def __init__(self, population_size):
        self.population = []
        self.population_size = population_size

    def crossover(self, first_parent, second_parent):
        first_chromosome = first_parent.chromosome
        second_chromosome = second_parent.chromosome

        size = len(first_chromosome)

        # Cut-and-crossfill crossover
        cut_point = random.randint(1, size - 2)
        child = first_chromosome[:cut_point]

        for gene in second_chromosome[cut_point:]:
            child.append(gene)

        return DNA(child)

    def create_population(self, number_of_queens):
        self.population = [
            self.__create_chromosome(number_of_queens) for _ in range(self.population_size)
        ]

    def __create_chromosome(self, number_of_queens):
        chromosome = [
            integer_to_binary(random.randint(0, number_of_queens - 1)) for _ in range(number_of_queens)
        ]
        return DNA(chromosome)

    def choose_parents(self, max_fitness):
        parent_pool = random.sample(self.population, 5)

        # Sort the parent pool based on fitness level
        parent_pool.sort(key=lambda dna: dna.fitness(max_fitness), reverse=True)

        # Select the best 2 parents from the parent pool
        return parent_pool[0], parent_pool[1]