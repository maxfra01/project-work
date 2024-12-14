import numpy as np
from numpy_mapping import numpy_function_map, numpy_binary_operator_list, numpy_unary_operator_list
from node import Node

VARIABLE_PROB = 0.8

class Tree:
    def __init__(self, max_depth, num_variables, root=None):
        self.max_depth = max_depth
        self.num_variables = num_variables
        self.depth = 1
        self.num_nodes = 1
        if root is None:
            self.root = Node(None, np.random.choice(list(numpy_function_map.keys())), 1)
            self._expand_tree(self.root)
            self.depth = self.root.get_depth()
        else:
            self.root = root
            self.depth = self.root.get_depth()
        
    def copy(self):
        return Tree(self.max_depth, self.num_variables, self.root.copy())
    
    def __str__(self):
        return self.root.to_expression()
    
    def evaluate(self, x: np.ndarray):
        return self.root.evaluate(x)
    
    def _expand_tree(self, node: Node, current_depth: int = 1):
        self.depth = max(self.depth, current_depth)
        node.level = current_depth
        
        if node.left is not None or node.right is not None:
            raise ValueError("Node already has children")
        
        if node.operator_name is not None:
            operands_number = 2 if node.operator_name in numpy_binary_operator_list else 1
            
        if current_depth >= self.max_depth: # Need to insert leaf nodes
            for _ in range(operands_number):
                new_node = Node(None, None, current_depth + 1)
                if np.random.rand() < 0.6:
                    x_index = np.random.randint(0, self.num_variables)
                    new_node.value = f'x[{x_index}]'
                    new_node.operator_name = None
                    new_node.function = None
                else:
                    new_node.value = round(np.random.uniform(-10, 10))
                    new_node.operator_name = None
                    new_node.function = None   
                node.add_child(new_node)
           
        else: # Expand tree with either operator or leaf nodes (truncate with 0.2 probability)
            
            for _ in range(operands_number):
                if np.random.rand() < 0.6 : # Insert operator nodes
                    new_node = Node(None, np.random.choice(list(numpy_function_map.keys())), current_depth + 1)
                    node.add_child(new_node)
                    self._expand_tree(new_node, current_depth + 1)
                else: # Insert leaf nodes
                    
                    new_node = Node(None, None, current_depth + 1)
                    if np.random.rand() < 0.6:
                        x_index = np.random.randint(0, self.num_variables)
                        new_node.value = f'x[{x_index}]'
                        new_node.operator_name = None
                        new_node.function = None
                    else:
                        new_node.value = round(np.random.uniform(-10, 10))
                        new_node.operator_name = None
                        new_node.function = None
                    node.add_child(new_node)
    
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
          
    def get_depth(self):
        d = self.root.get_depth()  
        return d 

    def mutate_subtree(self, node: Node):
        parent = node.parent
        if parent is None:
            new_tree = Tree(self.max_depth, self.num_variables)
            self.root = new_tree.root
            self.depth = new_tree.depth
        else:
            parent.right = None
            parent.left = None
            self._expand_tree(parent, parent.level)        

    def mutate_point(self, node: Node):
        if node.operator_name is not None:
            if node.operator_name in numpy_binary_operator_list:
                new_op= np.random.choice(list(numpy_binary_operator_list))
                while new_op == node.operator_name:
                    new_op= np.random.choice(list(numpy_binary_operator_list))
                node.operator_name = new_op
                node.function = numpy_function_map[node.operator_name]
            elif node.operator_name in numpy_unary_operator_list:
                new_op = np.random.choice(list(numpy_unary_operator_list))
                while new_op == node.operator_name:
                    new_op = np.random.choice(list(numpy_unary_operator_list))
                node.operator_name = new_op
                node.function = numpy_function_map[node.operator_name]
            else:
                raise ValueError("Invalid operator")
        else:
            if np.random.rand() < 0.8:
                x_index = np.random.randint(0, self.num_variables)
                node.value = f'x[{x_index}]'
                node.operator_name = None
                node.function = None
            else:
                node.value = round(np.random.uniform(-10, 10))
                node.operator_name = None
                node.function = None
    
    def mutate_collapse(self, node: Node):
        node.right = None
        node.left = None
        node.operator_name = None
        self.mutate_point(node)
    
      
    def get_depth(self):
        d = self.root.get_depth()  
        return d
        
