class Node:
    def __init__(self, data, next1=None): 
        self.data = data
        self.next = next1

def linked_list_from_string(s):
    nodes = list(map(int, s.split(' -> ')[:-1]))

    if not nodes:
        return None

    head = Node(nodes[0])
    current = head

    for value in nodes[1:]:
        current.next = Node(value)
        current = current.next
    return head
