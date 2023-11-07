# Genetic Algorithm for Population Optimization

This Python code defines a genetic algorithm for optimizing a population of individuals through successive generations. The algorithm simulates the process of natural selection, crossover, and mutation to improve individual fitness.

## Classes

### Individual
Represents an individual in the population. It contains the following attributes:
- `attr`: Attributes of the individual
- `fitness`: Fitness value of the individual
- `id`: Identifier of the individual
- `min_max_val`: Minimum and maximum values for attributes
- `mutation_rate`: Mutation rate

The `mutation` method introduces random changes to an individual's attributes.

### Population
Represents a collection of individuals. The population is initialized with the following parameters:
- `num_individuals`: Number of individuals
- `chromosome_size`: Size of the chromosome
- `min_max_val`: Minimum and maximum values for attributes
- `mutation_rate`: Mutation rate
- `random_seed`: Random seed for reproducibility

The population undergoes selection, crossover, and mutation during each generation.

### GeneticAlgorithm
Manages the overall genetic algorithm process. It performs the following tasks:
- Creates a population with specified parameters
- Defines a fitness function that evaluates an individual's attributes
- The `run` method orchestrates the execution of multiple generations, allowing the population to evolve to potentially better solutions.
- `threads`: Indicates whether to use multi-threading for fitness evaluation (True or False).

## Execution

1. The main function (`main`) sets parameters such as:
   - Number of individuals
   - Chromosome size
   - Minimum and maximum values for attributes
   - Mutation rate
   - Random seed for reproducibility
   - Number of generations

2. An instance of `GeneticAlgorithm` is created with the specified parameters, and it's run for the specified number of generations.

3. During each generation, the algorithm performs the following steps:
   - Evaluates the fitness of each individual using the defined fitness function
   - Combines individuals through selection and crossover
   - Applies mutation to introduce variability
   - Lists the individuals' attributes and fitness values for examination.

The purpose of this code is to demonstrate the implementation of a basic genetic algorithm that evolves a population of individuals over multiple generations to optimize their fitness. The fitness evaluation, crossover, and mutation mechanisms allow the algorithm to explore and potentially converge towards better solutions as the generations progress.


# Algoritmo Genético para Otimização de Populações

Este código em Python define um algoritmo genético para otimizar uma população de indivíduos ao longo de gerações sucessivas. O algoritmo simula o processo de seleção natural, cruzamento e mutação para melhorar a aptidão individual.

## Classes

### Indivíduo
Representa um indivíduo na população. Ele contém os seguintes atributos:
- `attr`: Atributos do indivíduo
- `aptidão`: Valor de aptidão do indivíduo
- `id`: Identificador do indivíduo
- `min_max_val`: Valores mínimos e máximos para atributos
- `taxa_mutação`: Taxa de mutação

O método `mutação` introduz mudanças aleatórias nos atributos do indivíduo.

### População
Representa uma coleção de indivíduos. A população é inicializada com os seguintes parâmetros:
- `num_individuals`: Número de indivíduos
- `tamanho_cromossomo`: Tamanho do cromossomo
- `min_max_val`: Valores mínimos e máximos para atributos
- `taxa_mutação`: Taxa de mutação
- `random_seed`: Semente aleatória para reprodutibilidade

A população passa por seleção, cruzamento e mutação durante cada geração.

### Algoritmo Genético
Gerencia o processo global do algoritmo genético. Ele realiza as seguintes tarefas:
- Cria uma população com parâmetros especificados
- Define uma função de aptidão que avalia os atributos de um indivíduo
- O método `executar` orquestra a execução de várias gerações, permitindo que a população evolua para soluções potencialmente melhores.
- `threads`: Indica se deve usar multi-threading para avaliação de aptidão (Verdadeiro ou Falso).

## Execução

1. A função principal (`main`) define parâmetros como:
   - Número de indivíduos
   - Tamanho do cromossomo
   - Valores mínimos e máximos para atributos
   - Taxa de mutação
   - Semente aleatória para reprodutibilidade
   - Número de gerações

2. Uma instância de `AlgoritmoGenético` é criada com os parâmetros especificados e é executada pelo número especificado de gerações.

3. Durante cada geração, o algoritmo realiza as seguintes etapas:
   - Avalia a aptidão de cada indivíduo usando a função de aptidão definida
   - Combina indivíduos por meio de seleção e cruzamento
   - Aplica mutação para introduzir variabilidade
   - Lista os atributos dos indivíduos e seus valores de aptidão para exame.

O objetivo deste código é demonstrar a implementação de um algoritmo genético básico que faz uma população de indivíduos evoluir ao longo de várias gerações para otimizar sua aptidão. Os mecanismos de avaliação de aptidão, cruzamento e mutação permitem que o algoritmo explore e potencialmente atinja soluções melhores à medida que as gerações avançam.
