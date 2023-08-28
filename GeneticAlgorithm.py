import random

class Individual:
    def __init__(self, attr, fitness, max_val, mutation_rate):
        self._attr = attr
        self._fitness = fitness
        self._max_val = max_val
        self._mutation_rate = mutation_rate

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, new_attr):
        self._attr = new_attr

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, new_fitness):
        if isinstance(new_fitness, (int, float)):
            self._fitness = new_fitness
        else:
            raise ValueError("Fitness must be a number")

    def mutation(self):
        for i in range(len(self._attr)):
            if random.random() < self._mutation_rate:  # Check mutation chance
                new_value = random.randint(0, self._max_val)
                while new_value in self._attr:
                    new_value = random.randint(0, self._max_val)
                self._attr[i] = new_value


class Population:
    def __init__(self, num_individuals, chromosome, max_val, mutation_rate, random_seed):
        self._num_individuals = num_individuals
        self._chromosome = chromosome
        self._max_val = max_val
        self._mutation_rate = mutation_rate
        self._individuals = self._create_individuals(random_seed)

    def _create_individuals(self, random_seed):
        random.seed(random_seed)  # Set the random seed here
        individuals = []
        possible_values = list(range(self._max_val + 1))  # Possible values from 0 to max_val

        for _ in range(self._num_individuals):
            random.shuffle(possible_values)  # Shuffle the values
            attr = possible_values[:self._chromosome]
            individual = Individual(attr, 0, self._max_val, self._mutation_rate)
            individuals.append(individual)
        return individuals

    def rank_individuals(self):
        self._individuals.sort(key=lambda ind: ind.fitness, reverse=True)

    def combine_individuals(self):
        self.rank_individuals()
        new_attrs = []

        for i in range(0, self._num_individuals, 2):
            attr_ind1 = self._individuals[i].attr[:self._chromosome // 2]
            attr_ind2 = self._individuals[i + 1].attr[self._chromosome // 2:]
            new_attr = attr_ind1 + attr_ind2

            if len(new_attr) > self._chromosome:
                new_attr = new_attr[:self._chromosome]  # Truncate if new_attr is too long

            new_attr = self._resolve_duplicates(new_attr)
            new_attrs.append(new_attr)

        for i in range(self._num_individuals // 2):
            self._individuals[-(i + 1)].attr = new_attrs[i]

    def _resolve_duplicates(self, attr):
        while len(attr) != len(set(attr)):
            for i in range(len(attr)):
                while attr.count(attr[i]) > 1:
                    attr[i] = random.randint(0, self._max_val)
        return attr

    def list_individuals(self):
        self.rank_individuals()
        for idx, individual in enumerate(self._individuals):
            print(f"Individual {idx + 1}:")
            print("Attributes:", individual.attr)
            print("Fitness:", individual.fitness)
            print()

    def apply_mutation(self):
        for individual in self._individuals:
            individual.mutation()


class GeneticAlgorithm:
    def __init__(self, num_individuals, chromosome, max_val, mutation_rate, random_seed):
        self._num_individuals = num_individuals
        self._chromosome = chromosome
        self._max_val = max_val
        self._mutation_rate = mutation_rate
        self._random_seed = random_seed
        self._population = self._create_population()

    def _create_population(self):
        return Population(self._num_individuals, self._chromosome, self._max_val, self._mutation_rate, self._random_seed)

    def fitness_function(self, individual):
        return sum(individual.attr)

    def evaluate_population(self):
        for individual in self._population._individuals:
            individual.fitness = self.fitness_function(individual)

    def run(self, generations):
        print(f"Initial population:")
        self._population.list_individuals()

        for i in range(0, generations):
            print(f"\n>>Generation {i+1}")
            self.evaluate_population()
            self._population.combine_individuals()
            self._population.apply_mutation()
            self._population.list_individuals()

def main():
    num_individuals = 10
    chromosome = 6
    max_val = 33
    mutation_rate = 0.05
    random_seed = 42
    generations = 100

    genetic_algorithm = GeneticAlgorithm(num_individuals, chromosome, max_val, mutation_rate, random_seed)
    genetic_algorithm.run(generations)


if __name__ == "__main__":
    main()
