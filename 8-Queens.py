#!/usr/bin/env python
# coding: utf-8

# How to Solve 8-Queens with the Genetic Algorithm

# In[2]:


import random 
import numpy as np 


# Initialization

# In[3]:


iteration = 0
best_fit = 0
N = 8
MUTATION_RATE = 0.05


# Funtions

# In[5]:


def initail_population():
	population = np.random.randint(low = 0, high = N-1, size = (N, N), dtype = int )
	return population

def fitness_function(seq):
	score = 0
	for row in range (N):
		col = seq[row]
		for other_row in range (N):
			if other_row == row:
				continue 
			elif seq[other_row] == col:
				continue
			elif (other_row + seq[other_row]) == row + col:
				continue
			elif (other_row - seq[other_row]) == row - col:
				continue
			else:
				score += 1

	return score/2 


def crossover(parent1, parent2):
	cross_point = random.randint(0, N-1)
	offspring1 = []
	offspring2 = []
	for i in range(N):
		if i < cross_point:
			offspring1.append(parent1[i])
		else:
			offspring1.append(parent2[i])

		if (i + cross_point) < N:
			offspring2.append(parent1[i + cross_point])
		else:
			offspring2.append(parent2[i-cross_point-2])

	return offspring1, offspring2

def mutate(seq):
	for row in range (len(seq)):
		if random.random() < MUTATION_RATE:
			seq[row] = random.randrange(N)
	return seq


def best_fitness():
	best_fit = 0
	for i in range (N):
		temp = fitness_function(population[i, :])
		if best_fit < temp:
			best_fit = temp
	return best_fit


def selection(population):
    fitness = np.zeros((2,N))
    for i in range (N):
        x = fitness_function(population[i])
        fitness[0, i] = x 
        fitness[1, i] = i
    f2=fitness[:, fitness[0].argsort()]
    parent1 = f2[1,N-1]
    parent2 = f2[1,N-2]
    return int(parent1), int(parent2)


# Main

# In[6]:


population = initail_population()
for i in range (N):
	if fitness_function(population[i]) == 28:
		print ("the best solution has finded")

while (iteration<700 and best_fit<28):
	parent1, parent2 = selection(population)
	offspring1, offspring2 = crossover(population[parent1, :], population[parent2, :])
	offspring1 = mutate(offspring1)
	offspring2 = mutate(offspring2)
	population[parent1] = offspring1
	population[parent2] = offspring2

	temp = best_fitness()
	if temp > best_fit:
		best_fit = temp
	iteration += 1

print ("best_fit is ", best_fit)


# In[ ]:




