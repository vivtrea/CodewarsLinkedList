'''
Module provides functions to push new head of 
linked list and create a base list
'''

class Node:
    '''Class for node in linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    '''Pushes new head of list'''
    new_head = Node(data)
    new_head.next = head
    return new_head

def build_one_two_three():
    '''builds a base linked list with 3 nodes'''
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
