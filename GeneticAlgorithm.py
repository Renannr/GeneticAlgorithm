import time
import copy
import random
import concurrent.futures

class Individual:
    def __init__(self, ind_id, attr, min_max_val, mutation_rate):
        self._id = ind_id
        self._attr = attr
        self._fitness = 0
        self._min_max_val = min_max_val
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

    @property
    def id(self):
        return self._id

    def get_fitness(self):
        return self._fitness

    def get_attr(self):
        return self._attr

    def fitness_function(self):
        self._fitness = sum(self._attr)
        time.sleep(1)

    def mutation(self):
        for i in range(len(self._attr)):
            if random.random() < self._mutation_rate:
                new_value = random.randint(self._min_max_val[0], self._min_max_val[1])
                while new_value in self._attr:
                    new_value = random.randint(self._min_max_val[0], self._min_max_val[1])
                self._attr[i] = new_value

class Population:
    def __init__(self, num_individuals, chromosome_size, min_max_val, mutation_rate, random_seed):
        self._num_individuals = num_individuals
        self._chromosome_size = chromosome_size
        self._min_max_val = min_max_val
        self._mutation_rate = mutation_rate
        self._individuals = self._create_individuals(random_seed)
        self._best_individual = None

    def _create_individuals(self, random_seed):
        random.seed(random_seed)
        individuals = []
        possible_values = list(range(self._min_max_val[1] + 1))

        for index in range(self._num_individuals):
            random.shuffle(possible_values)
            attr = possible_values[:self._chromosome_size]
            individual = Individual(index, attr, self._min_max_val, self._mutation_rate)
            individuals.append(individual)
        return individuals

    def rank_individuals(self):
        self._individuals.sort(key=lambda ind: ind.fitness, reverse=True)

        if((not self._best_individual) or (self._individuals[0].fitness > self._best_individual.fitness)):
            self._best_individual = copy.deepcopy(self._individuals[0])

    def combine_individuals(self):
        self.rank_individuals()
        new_attrs = []

        for i in range(0, self._num_individuals - 1, 2):
            attr_ind1 = self._individuals[i].attr[:self._chromosome_size // 2]
            attr_ind2 = self._individuals[i + 1].attr[self._chromosome_size // 2:]
            new_attr = attr_ind1 + attr_ind2

            if len(new_attr) > self._chromosome_size:
                new_attr = new_attr[:self._chromosome_size]

            new_attr = self._resolve_duplicates(new_attr)
            new_attrs.append(new_attr)

        # Handle the last individual if the population size is odd
        if self._num_individuals % 2 == 1:
            last_individual = self._individuals[-1]
            new_attrs.append(self._resolve_duplicates(last_individual.attr + last_individual.attr))

        for i in range(self._num_individuals // 2):
            self._individuals[-(i + 1)].attr = new_attrs[i]

    def _resolve_duplicates(self, attr):
        while len(attr) != len(set(attr)):
            for i in range(len(attr)):
                while attr.count(attr[i]) > 1:
                    attr[i] = random.randint(self._min_max_val[0], self._min_max_val[1])
        return attr

    def list_individuals(self):
        self.rank_individuals()
        for idx, ind in enumerate(self._individuals):
            print(f"Individual {ind.id}:")
            print(f"Attributes: {ind.attr}")
            print(f"Fitness: {ind.fitness}")
            print()

    def apply_mutation(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(individual.mutation) for individual in self._individuals]
            concurrent.futures.wait(futures)


class GeneticAlgorithm:
    def __init__(self, num_individuals, chromosome_size, min_max_val, mutation_rate, random_seed, threads):
        self._num_individuals = num_individuals
        self._chromosome_size = chromosome_size
        self._min_max_val = min_max_val
        self._mutation_rate = mutation_rate
        self._random_seed = random_seed
        self._threads = threads
        self._population = self._create_population()

    def _create_population(self):
        return Population(self._num_individuals, self._chromosome_size, self._min_max_val, self._mutation_rate, self._random_seed)

    def evaluate_population(self):
        if self._threads:
             with concurrent.futures.ThreadPoolExecutor() as executor: 
                futures = [executor.submit(individual.fitness_function) for individual in self._population._individuals]
                concurrent.futures.wait(futures)
        else:
            for individual in self._population._individuals:
                individual.fitness_function()

    def calc_time(self, start_time, end_time):
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

        return minutes, seconds, milliseconds

    def run(self, generations):
        start_total_time = time.time()
        
        print(f"Initial population:")
        self.evaluate_population()
        self._population.list_individuals()

        for i in range(0, generations):
            start_time = time.time()
            
            print(f"\n>>Generation {i+1}")
            self._population.combine_individuals()
            self._population.apply_mutation()
            self.evaluate_population()
            self._population.list_individuals()
            
            end_time = time.time()
            minutes, seconds, milliseconds = self.calc_time(start_time, end_time)
            print(f"\nTotal time gen {i}: {minutes} minutes, {seconds} seconds, and {milliseconds} milliseconds")

        end_total_time = time.time()
        minutes, seconds, milliseconds = self.calc_time(start_total_time, end_total_time)
        print(f"\nTotal time: {minutes} minutes, {seconds} seconds, and {milliseconds} milliseconds")
        print("\nBest individual:")
        print(f"Attributes: {self._population._best_individual.get_attr()}")
        print(f"Fitness: {self._population._best_individual.get_fitness()}")
        print()


def main():
    num_individuals = 10
    chromosome_size = 4
    min_max_val = [0, 9]
    mutation_rate = 0.05
    random_seed = 42
    generations = 20
    threads = True

    genetic_algorithm = GeneticAlgorithm(num_individuals, chromosome_size, min_max_val, mutation_rate, random_seed, threads)
    genetic_algorithm.run(generations)


if __name__ == "__main__":
    main()
