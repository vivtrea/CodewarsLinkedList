'''Module provides alternating function'''

class Node(object):
    '''Node class'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''Context class'''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''Alternate lists'''
    if head is None or head.next is None:
        raise ValueError

    first_h = Node(head.data)
    second_h = Node(head.next.data)

    first, second = first_h, second_h
    current = head.next.next
    i = 1
    while current is not None:
        new_node = Node(current.data)
        if i & 1:
            first.next = new_node
            first = first.next
        else:
            second.next = new_node
            second = second.next
        current = current.next
        i += 1

    return Context(first_h, second_h)
