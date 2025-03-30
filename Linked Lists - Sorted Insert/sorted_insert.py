'''Module provides sorted insert in linked list'''

class Node(object):
    '''Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    '''Insert in sorted linked list'''
    insert_node = Node(data)
    if head is None:
        insert_node.next = head
        head = insert_node
        return head

    if head.data >= data:
        insert_node.next = head
        head = insert_node
        return head

    current = head
    while current.next is not None and current.next.data < insert_node.data:
        current = current.next
    insert_node.next = current.next
    current.next = insert_node
    return head