import numpy as np
from numpy_mapping import numpy_function_map, numpy_binary_operator_list, numpy_unary_operator_list
from node import Node

class Tree:
    def __init__(self, max_depth, num_variables, root=None):
        self.max_depth = max_depth
        self.num_variables = num_variables
        self.depth = 1
        if root is None:
            self.root = Node(None, np.random.choice(list(numpy_function_map.keys())), 1)
            self._expand_tree(self.root)
        else:
            self.root = root
        
    def copy(self):
        return Tree(self.max_depth, self.num_variables, self.root.copy())
    
    def __str__(self):
        return self.root.to_expression()
    
    def evaluate(self, x: np.ndarray):
        return self.root.evaluate(x)
    
    def _expand_tree(self, node: Node, current_depth: int = 1):
        self.depth = max(self.depth, current_depth)
        if node.left is not None or node.right is not None:
            raise ValueError("Node already has children")
        
        if current_depth >= self.max_depth:
            if np.random.rand() < 0.9:
                x_index = np.random.randint(0, self.num_variables)
                node.value = f'x[{x_index}]'
                node.operator_name = None
                node.function = None
            else:
                node.value = round(np.random.uniform(-10, 10))
                node.operator_name = None
                node.function = None                
           
        else:
            if np.random.rand() < 0.95:
                operator_name = np.random.choice(list(numpy_function_map.keys()))
                node.operator_name = operator_name
                node.function = numpy_function_map[operator_name]
                
                if operator_name in numpy_binary_operator_list:
                    child1 = Node(None, None, current_depth + 1)
                    child2 = Node(None, None, current_depth + 1)
                    node.add_child(child1)
                    node.add_child(child2)
                    self._expand_tree(child1, current_depth + 1)
                    self._expand_tree(child2, current_depth + 1)
                else:
                    child1 = Node(None, None, current_depth + 1)
                    node.add_child(child1)
                    self._expand_tree(child1, current_depth + 1)
            else:
                
                if np.random.rand() < 0.9:
                    x_index = np.random.randint(0, self.num_variables)
                    node.value = f'x[{x_index}]'
                    node.operator_name = None
                    node.function = None
                else:
                    node.value = round(np.random.uniform(-10, 10))
                    node.operator_name = None
                    node.function = None
    
    def _get_all_nodes(self,node, nodes = []):
        nodes.append(node)
        if node.left:
            self._get_all_nodes(node.left, nodes)
        if node.right:
            self._get_all_nodes(node.right, nodes)
        return nodes
        
                                       
    def get_random_node(self):
        nodes = self._get_all_nodes(self.root)
        return np.random.choice(nodes)                
                    

    def mutate_point(self, node: Node):
        if node.operator_name is not None:
            if node.operator_name in numpy_binary_operator_list:
                node.operator_name = np.random.choice(list(numpy_binary_operator_list))
                node.function = numpy_function_map[node.operator_name]
            elif node.operator_name in numpy_unary_operator_list:
                node.operator_name = np.random.choice(list(numpy_unary_operator_list))
                node.function = numpy_function_map[node.operator_name]
            else:
                raise "Invalid operator" 
        else:
            if np.random.rand() < 0.9:
                x_index = np.random.randint(0, self.num_variables)
                node.value = f'x[{x_index}]'
                node.operator_name = None
                node.function = None
            else:
                node.value = round(np.random.uniform(-10, 10))
                node.operator_name = None
                node.function = None
                