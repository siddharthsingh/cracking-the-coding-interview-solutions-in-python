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

def printLL(head):
    while head:
        print(head.data,end=", ")
        head = head.next
    print("")

# printLL(head)
printLL(head2)
print(contains_cycle(head))
print(contains_cycle(head2))