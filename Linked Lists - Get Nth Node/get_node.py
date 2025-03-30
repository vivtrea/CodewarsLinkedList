'''Module provides getter for nth node'''

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next1=None):
        self.data = data
        self.next = next1
        
def get_nth(node, index):
    '''Get nth node'''
    if index < 0 or node is None:
        raise IndexError
    i = 0
    current = node
    while i != index and current is not None:
        current = current.next
        if current is None and index>i:
            raise IndexError
        i += 1
    return current
