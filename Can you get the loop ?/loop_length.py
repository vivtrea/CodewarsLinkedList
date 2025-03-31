'''Module provides loop detection'''

class Node:
    '''Node class'''
    def __init__(self, next1=None):
        self.next = next1

def loop_size(node):
    '''Detect loop and its length'''
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = node
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next
                if slow == fast:
                    break
            break
    current = slow.next
    l = 1
    while current != slow:
        current = current.next
        l += 1
    return l
