from tree import Tree
from genetic_stuff import recombination_xover, fitness, tournament_selection, mutation_point, mutation_hoist, mutation_subtree
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

PROBLEM = 4

problem = np.load(f'data/problem_{PROBLEM}.npz')
X = problem['x']
Y = problem['y']

VARIABLES = X.shape[0]
FOREST_SIZE = 200
OFFSPRING_SIZE = int(FOREST_SIZE * 0.05)
TOURNAMENT_SIZE = int(FOREST_SIZE * 0.1)
GENERATIONS = 100
PM = 0.4

mutation = mutation_subtree
xover = recombination_xover


forest = [Tree(max_depth=VARIABLES+3 , num_variables=VARIABLES) for _ in range(FOREST_SIZE)]


for _ in tqdm(range(GENERATIONS)):
    parent1 = tournament_selection(forest, X, Y, TOURNAMENT_SIZE)
    parent2 = tournament_selection(forest, X, Y, TOURNAMENT_SIZE)
    
    #print(f"Parent 1: {parent1}")
    #print(f"Parent 2: {parent2}")
    
    #input("Press Enter to generate offspring...")
    
    offspring = []
    for _ in range(OFFSPRING_SIZE // 2):
        #if np.random.rand() < PM:
        offspring.append(mutation(parent1))
        offspring.append(mutation(parent2))
        offspring.append(xover(parent1, parent2))
        offspring.append(xover(parent2, parent1))
    

    # print("Offspring: ")
    # for i in range(len(offspring)):
    #     print(f"\t {offspring[i]}")
    
    forest.extend(offspring)
    forest.sort(key=lambda tree: fitness(tree, X, Y), reverse=True)
    forest = forest[:FOREST_SIZE]
    
    print(f"MSE: {-fitness(forest[0], X, Y)  / forest[0].depth}")
    print(f"Best formula so far: {forest[0]}, Depth = {forest[0].depth}")

print(f"Problem: {PROBLEM}")
print(f"\t Number of variables: {VARIABLES}")
print(f"\t Best formula: {forest[0]}")
print(f"\t Depth: {forest[0].depth}")
print(f"\t MSE: {-fitness(forest[0], X, Y) / forest[0].depth}")


predictions = np.array([forest[0].evaluate(x) for x in X.T])

plt.figure(figsize=(10, 5))
plt.plot(Y[:100], label='True Values')
plt.plot(predictions[:100], label='Predicted Values', linestyle='--')
plt.legend()
plt.xlabel('Sample Index')
plt.ylabel('Output')
plt.title('True Values vs Predicted Values')
plt.show()