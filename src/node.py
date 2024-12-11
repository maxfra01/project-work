import numpy as np
from numpy_mapping import numpy_function_map, numpy_binary_operator_list, numpy_unary_operator_list

class Node:
    def __init__(self, value = None, operator_name = None, level = 1, parent=None):
        self.value = value
        self.operator_name = operator_name
        self.function = numpy_function_map.get(operator_name, None)
        self.level = level
        self.parent = parent
        self.right = None
        self.left = None
        
    def add_child(self, child):
        child.parent = self
        if self.left is None:
            self.left = child
            return
        elif self.right is None:
            self.right = child
            return
        else:
            raise ValueError("Node already has two children")
        
        
        
    def copy(self):
        new_node = Node(self.value, self.operator_name, self.level)
        if self.left:
            new_node.add_child(self.left.copy())
        if self.right:
            new_node.add_child(self.right.copy())
        return new_node
    
    def to_expression(self):
        if self.operator_name is None:
            return str(self.value)
        else:
            if self.operator_name in ['add', 'subtract', 'multiply', 'divide', 'power', 'pow']:
                if self.operator_name == 'add':
                    return f"({self.left.to_expression()} + {self.right.to_expression()})"
                elif self.operator_name == 'subtract':
                    return f"({self.left.to_expression()} - {self.right.to_expression()})"
                elif self.operator_name == 'multiply':
                    return f"({self.left.to_expression()} * {self.right.to_expression()})"
                elif self.operator_name == 'divide':
                    return f"({self.left.to_expression()} / {self.right.to_expression()})"
                elif self.operator_name in ['power', 'pow']:
                    return f"({self.left.to_expression()} ** {self.right.to_expression()})"
            elif self.operator_name in numpy_unary_operator_list:
                return f"{self.operator_name}({self.left.to_expression()})"
            else:
                return f"{self.operator_name}({self.left.to_expression()}, {self.right.to_expression()})"
    def __str__(self):
        return self.to_expression()
    
    def evaluate(self, x: np.ndarray):
        if self.value is not None: # could be a number or x[i]
            if 'x' in str(self.value):
                return x[int(self.value[2])] # Notation 'x[i]' so i is value[2]
            else:
                return float(self.value)
        else:
            if self.operator_name in numpy_unary_operator_list:
                return self.function(self.left.evaluate(x))
            elif self.operator_name in numpy_binary_operator_list:
                return self.function(self.left.evaluate(x), self.right.evaluate(x))
            else:
                raise "Invalid operator at node evaluation"
        
