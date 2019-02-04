class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(5)
node8 = Node(6)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

head2 = node5
node5.next = node6
node6.next = node7
node7.next = node8

def contains_cycle(head):
    nodes = set()
    while head:
        if head in nodes:
            return True
        nodes.add(head)
        head = head.next
    return False


def contains_cycle2(head):
    """

    :param head: head of list
    :return: The start of the loop in list if it exists, False if no loop
    :method: using fast and slow pointers
    """

    fast_pointer = head
    slow_pointer = head

    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if fast_pointer == slow_pointer:
            break

    if not fast_pointer or not fast_pointer.next:
        return False

    slow_pointer = head

    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    return slow_pointer




def printLL(head):
    while head:
        print(head.data,end=", ")
        head = head.next
    print("")

# printLL(head)
printLL(head2)
print(contains_cycle2(head).data)
print(contains_cycle2(head2))