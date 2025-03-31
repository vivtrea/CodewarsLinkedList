"""Module provides moving node"""

class Node(object):
    '''Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''Contains source and destination'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: 'Node', dest:'Node'):
    """Moves node"""
    head_d = source.data
    new_dest = Node(head_d)
    new_dest.next = dest

    new_source = source.next
    return Context(new_source, new_dest)
