class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: 'Node'):
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

print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
print(stringify(Node(1, Node(2, Node(3)))))
print(stringify(Node(None)))