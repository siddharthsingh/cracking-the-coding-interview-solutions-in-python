class Node():
    def __init__(self,data):
        self.data  = data
        self.next = None

nums_to_insert = [3,5,8,5,10,2,1]
head = Node(0)
temp = head
for num in nums_to_insert:
    temp.next = Node(num)
    temp = temp.next

def partition(head,key):
    pointer_to_lower = None
    temp = head
    while temp:
        if temp.data<key:
            if not pointer_to_lower:
                pointer_to_lower = head
                head.data,temp.data = temp.data,head.data
            else:
                pointer_to_lower.next.data,temp.data = temp.data,pointer_to_lower.next.data
                pointer_to_lower = pointer_to_lower.next
        temp = temp.next

def printLL(head):
    while head:
        print(head.data,end=", ")
        head = head.next
    print("")

printLL(head)
partition(head,5)

printLL(head)

