from tree import Tree
from node import Node
import numpy as np

def fitness(tree: Tree, X: np.ndarray, Y: np.ndarray) -> float:
    """
    Returns the fitness of a tree: MSE and the depth of the tree 
    """
    X = X.T
    Y = Y.T
    mse = 0
    try:
        for i in range(len(X)):
            y_pred = tree.evaluate(X[i])
            if np.isnan(y_pred):
                return -np.inf
            mse += (y_pred - Y[i]) ** 2
        return (- mse /len(X) )* tree.depth
    except RecursionError:
        print("Recursion error for tree: ", tree)
        return -np.inf

def tournament_selection(population: list[Tree], X: np.ndarray, Y: np.ndarray, tournament_size: int) -> Tree:
    tournament = list(np.random.choice(population, tournament_size))
    tournament.sort(key=lambda tree: fitness(tree, X, Y ), reverse=True)
    return tournament[0]
    
def mutation_subtree(tree: Tree):
    new_tree = tree.copy()
    node = new_tree.get_random_node()
    new_tree.mutate_subtree(node)
    return new_tree

def mutation_collapse(tree: Tree):
    new_tree = tree.copy()
    node = new_tree.get_random_node()
    new_tree.mutate_collapse(node)
    return new_tree

def mutation_hoist(tree: Tree):
    new_tree = tree.copy()
    node = new_tree.get_random_node()
    while node.operator_name is None:
        node = new_tree.get_random_node()
    return Tree(new_tree.max_depth, new_tree.num_variables, node)
   
def mutation_point(tree: Tree):
    new_tree = tree.copy()
    node = new_tree.get_random_node()
    new_tree.mutate_point(node)
    return new_tree

def recombination_xover(tree1: Tree, tree2: Tree):
    tree1_copy = tree1.copy()
    tree2_copy = tree2.copy()

    node1: Node = tree1_copy.get_random_node()
    node2: Node = tree2_copy.get_random_node()
    while node1.operator_name is None:
        node1 = tree1_copy.get_random_node()
    while node2.operator_name is None:
        node2 = tree2_copy.get_random_node()
        
    if node1.parent is not None:
        if node1.parent.left == node1:
            node1.parent.left = node2
        if node1.parent.right == node1:
            node1.parent.right = node2
    else:
        tree1_copy.root = node2
    return tree1_copy
