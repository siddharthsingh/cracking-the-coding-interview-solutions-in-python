class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

nums_to_insert = [1,2,3,4,5,6,7]
head = Node(0)
temp = head
for num in nums_to_insert:
    temp.next = Node(num)
    temp = temp.next
node_to_delete = temp
temp.next = Node(8)

def deleteMiddleNode(node):
    node.data = node.next.data
    node.next = node.next.next

def printLL(head):
    while head:
        print(head.data,end=", ")
        head = head.next
    print("")
printLL(head)
deleteMiddleNode(node_to_delete)

printLL(head)

