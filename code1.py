# -*- coding: utf-8 -*-
'''
Genetic algorithm
'''
import random
import datetime

gene_Set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "To be or not to be"

def generate_pop(length):
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_Set))
        genes.extend(random.sample(gene_Set,sample_size))
    return ''.join(genes)
    

#fitness function
def get_fitness(guess):
    return sum(1 for expected,actual in zip(guess, target) if expected == actual)

def mutate(parent):
    index = random.randrange(len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(gene_Set,2)
    if newGene == childGenes[index]:
       childGenes[index] = alternate
    else:
        childGenes[index] = newGene
    return ''.join(childGenes)

#print(mutate(parent))

#display function to monitor distin
def display(guess):
    timediff = datetime.datetime.now()-starttime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess,fitness,str(timediff)))
    
random.seed()
starttime = datetime.datetime.now()
parent = generate_pop(len(target))
parent_fitness = get_fitness(parent)
display(parent)

while(True):
    child = mutate(parent)
    childFitness = get_fitness(child)
    if parent_fitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(parent):
        break
    parent_fitness = childFitness
    parent = child
    

    
    
    
