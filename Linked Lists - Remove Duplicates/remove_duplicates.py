'''Provides duplicates removal from sorted linked list'''

class Node(object):
    '''Class for node'''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''Removed duplicates from sorted linked lists'''
    current = head
    if head is None:
        return None

    while current and current.next:

        if current.data == current.next.data:
            skip = current.next.next
            current.next = skip
        else:
            current = current.next

    return head
