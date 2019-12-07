import file_handler
import Chromosome
import plot
import copy
import random
import numpy as np

# Mu is the length of data set
Mu = 0
# Todo change Mu's coefficient below to attain the best result
# Lambda is evaluated after data set read
Lambda = 0

# problem parameters
number_of_generations = 10
Lambda_coefficient = .8
crossover_probability = .5
mutation_rate = .7
sigma = 5

file_num = '2'
min_val = 1
max_val = 10

def generate_initial_population(chro_len, min_val, max_val):
    # Todo
    list_of_chromosomes = []
    for i in range(Mu):
        list_of_chromosomes.append(Chromosome.Chromosome(chro_len, min_val, max_val))
    return list_of_chromosomes


def generate_new_seed(pops):
    """
    :return: return lambda selected parents
    """
    # Todo

    parents = []
    for i in range(Lambda):
        f1 = copy.copy(pops[random.randrange(0, Mu)])
        f2 = copy.copy(pops[random.randrange(0, Mu)])
        parents.append([f1, f2])
    return parents


def parent_crossover(parents):
    off_spring = []
    for i in parents:
        if random.uniform(0, 1) < crossover_probability:
            off_spring.append(crossover(i[0], i[1]))
    return off_spring


def crossover(chromosome1, chromosome2):
    # Todo
    child = Chromosome.Chromosome(2, -1, 1)
    r1 = random.randrange(0, 2)
    r2 = random.randrange(0, 2)
    child.gene[r1] = chromosome1.gene[r1]
    child.gene[r2] = chromosome2.gene[r2]
    return child


def list_mutation(lis):
    mutated = []
    for i in lis:
        mutated.append(mutation(i))
    return mutated


def mutation(chromosome):
    """
    Don't forget to use Gaussian Noise here !
    :param chromosome:
    :return: mutated chromosome
    """
    # Todo
    rand = random.uniform(0, 1)
    if rand < mutation_rate:
        noise = np.random.normal(0, sigma, 2)
        chromosome.gene[0] += noise[0]
        chromosome.gene[1] += noise[1]
    return chromosome
    return


def evaluate_new_generation(pops, pointss):
    # Todo
    """
    Call evaluate method for each new chromosome
    :return: list of chromosomes with evaluated scores
    """
    for i in range(len(pops)):
        pops[i].evaluate(pointss)
    return pops


def choose_new_generation(pops, offs):
    #Todo
    """
    Use one of the discussed methods in class.
    Q-tournament is suggested !
    :return: Mu selected chromosomes for next cycle
    """
    whole = offs + pops
    whole.sort(key=lambda x: x.score, reverse=True)
    half = whole[:Mu//2]
    return half + whole[-(Mu-len(half)):]


def average(p):
    return np.average([i.score for i in p])


def normalize_list(p):
    for i in p:
        i.normalize()
    return p


if __name__ == '__main__':
    # Todo -- Use Methods In a proper arrangement

    points = []
    pop = []
    new_parents = []
    offspring = []
    # read points from data set
    points = file_handler.read_from_file(file_num)
    Mu = len(points)
    Lambda = int(Lambda_coefficient*Mu)

    # obviously generate random population
    pop = generate_initial_population(chro_len=2, min_val=min_val, max_val=max_val)
    # eval population scores
    pop = evaluate_new_generation(pop, points)

    for i in range(number_of_generations):
        # choose new parents
        new_parents = generate_new_seed(pop)
        # cross over of new parents to make the offspring
        offspring = parent_crossover(new_parents)
        # mutation of the offspring and pop (main population)
        pop = list_mutation(pop)
        offspring = list_mutation(offspring)
        # evaluation the score of offspring and new population
        pop = evaluate_new_generation(pop, points)
        offspring = evaluate_new_generation(offspring, points)
        # choose the generation from offspring and parents
        pop = choose_new_generation(pop, offspring)
        # normalize the result
        pop = normalize_list(pop)
        print(f'[{i}] - best score: {pop[0].score} | worst score: {pop[-1].score}')
        print(f'average {average(pop)}')
    plot.plot(points, pop)
