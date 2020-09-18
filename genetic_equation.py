#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
equation solving using genetic algorithm
Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
(x1,x2,x3,x4,x5,x6)=(4,-2,7,5,11,1)

'''

import numpy as np
import GA 

EQN_INPUTS = [4,-2,7,5,11,1]
NUM_WEIGHTS = 6


sol_per_pop = 8
pop_size = (sol_per_pop,NUM_WEIGHTS)
new_population = np.random.uniform(low=-4.0,high=4.0,size=pop_size)

print(new_population.shape[1])

num_generations = 50
num_parents_mating = 2

for generation in range(num_generations):
    #calculate fitness
    fitness= GA.calc_fitness(EQN_INPUTS,new_population)
    #select best parents
    parents = GA.select_mating_pool(new_population, fitness, 
                                       num_parents_mating)
 
     # Generating next generation using crossover.
    offspring_crossover = GA.crossover(parents,
                                        offspring_size=(pop_size[0]-parents.shape[0], NUM_WEIGHTS))
 
     # Adding some variations to the offsrping using mutation.
    offspring_mutation = GA.mutation(offspring_crossover)
# Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation
    print("Best result : ", np.max(np.sum(new_population*EQN_INPUTS, axis=1)))


fitness = GA.calc_fitness(EQN_INPUTS, new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = np.where(fitness == np.max(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])

