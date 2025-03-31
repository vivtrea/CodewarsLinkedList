'''Module provides node swap'''

class Node:
    '''Node class'''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    '''Swap node pairs recursively'''
    if head is None or head.next is None:
        return head

    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head

    return new_head