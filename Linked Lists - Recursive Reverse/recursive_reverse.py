'''Module provides reverse'''

class Node(object):
    '''Class of node'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    '''Reverse recursively'''
    if head is None or head.next is None:
        return head
    
    next_node = head.next
    new_head = reverse(next_node)
    
    next_node.next = head
    head.next = None

    return new_head
