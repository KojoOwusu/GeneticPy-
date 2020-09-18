#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GA library :)
"""
import numpy as np

#fitness function calculation
def calc_fitness(eqn_inputs,pop):
    fitness = np.sum(pop*eqn_inputs,axis=1)
    return fitness

#mating pool
def select_mating_pool(pop,fitness,num_parents):
    parents = np.empty((num_parents,pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num,:] = pop[max_fitness_idx,:]
        fitness[max_fitness_idx] = -999999999
    return parents

def crossover(parents,offspring_size):
    offspring = np.empty(offspring_size)
    crossover_point = np.uint8(offspring_size[1]/2)
    for k in range(offspring_size[0]):
         # Index of the first parent to mate.
         parent1_idx = k%parents.shape[0]
         # Index of the second parent to mate.
         parent2_idx = (k+1)%parents.shape[0]
         # The new offspring will have its first half of its genes taken from the first parent.
         offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
         # The new offspring will have its second half of its genes taken from the second parent.
         offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring
 
def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover
    
    