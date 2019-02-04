class Node():
    def __init__(self,val):
        self.val = val
        self.next = None


nums_to_insert = [1,2,3,3,4,5,6]
head = Node(nums_to_insert[0])
temp = head
for num in nums_to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next

def printLL(head):
    while head:
        print(head.val, end = ", ")
        head = head.next
    print("")

def reverse_linked_list(node,prev):
    if not node:
        global head
        head = prev
        return None
    reverse_linked_list(node.next,node)
    node.next = prev

printLL(head)
reverse_linked_list(head, None)
printLL(head)



