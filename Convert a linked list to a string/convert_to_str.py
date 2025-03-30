class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: 'Node'):
    head = node.data
    if head is None:
        return 'None'

    string_repr = f'{head}'
    current_node = node.next

    while current_node.data is not None:
        string_repr += f' -> {current_node.data}'
        current_node = current_node.next
        if current_node is None:
            break
    string_repr += ' -> None'

    return string_repr

print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
print(stringify(Node(1, Node(2, Node(3)))))
print(stringify(Node(None)))