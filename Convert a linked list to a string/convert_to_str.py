'''Module provides linked list string repr conversion'''

class Node():
    '''Class for node in linked list'''
    def __init__(self, data, next1 = None):
        self.data = data
        self.next = next1

def stringify(node: 'Node'):
    '''Convert linked list into string representation'''
    if node is None or node.data is None:
        return 'None'

    string_repr = []
    current_node = node

    while current_node is not None:
        string_repr.append(str(current_node.data))
        current_node = current_node.next

    string_repr.append('None')
    string_repr = ' -> '.join(string_repr)

    return string_repr
