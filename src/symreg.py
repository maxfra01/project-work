from tree import Tree
from genetic_stuff import xover, fitness, tournament_selection, mutation_point, mutation_hoist
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def real_f(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5

#problem = np.load('FINAL_PROJECT/problem_0.npz')
problem = np.load('data/problem_2.npz')
X = problem['x']
Y = problem['y']

VARIABLES = X.shape[0]
FOREST_SIZE = 500
TOURNAMENT_SIZE = int(FOREST_SIZE * 0.10)
GENERATIONS = 100
PM = 0.05

forest = [Tree(max_depth=5, num_variables=VARIABLES) for _ in range(FOREST_SIZE)]
takeover_time = 0

for _ in tqdm(range(GENERATIONS)):
    parent1 = tournament_selection(forest, X,Y, TOURNAMENT_SIZE)
    parent2 = tournament_selection(forest, X,Y, TOURNAMENT_SIZE)
    if np.random.rand() < PM:
        forest.append(mutation_point(parent1))
        forest.append(mutation_hoist(parent2))
    forest.append(xover(parent1, parent2))
    
    forest.sort(key=lambda tree: fitness(tree, X, Y), reverse=True)
    forest = forest[:FOREST_SIZE]
    print(f"MSE: {-fitness(forest[0], X, Y)}")
    print(f"Best formula so far: ", forest[0])


print(f"formula: {forest[0]}")

predictions = np.array([forest[0].evaluate(x) for x in X.T])

plt.figure(figsize=(10, 5))
plt.plot(Y, label='True Values')
plt.plot(predictions, label='Predicted Values', linestyle='--')
plt.legend()
plt.xlabel('Sample Index')
plt.ylabel('Output')
plt.xticks(np.arange(0, len(Y), step=1))
plt.title('True Values vs Predicted Values')
plt.show()