class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


to_insert = [1,2,3,4,5,6,7,7,8,1,0,0]
head = Node(to_insert[0])
temp = head
for num in to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next

def printLL(head):
    while head:
        print(head.data)
        head = head.next
# printLL(head)

def removeDups(head):
    nums = set()
    prev = head
    nums.add(head.data)
    head = head.next
    while head:
        if head.data in nums:
            prev.next = head.next
            head = head.next
            continue
        nums.add(head.data)
        prev = head
        head = head.next

def removeDups2(head):
    while head:
        forward_pointer = head.next
        prev = head
        while forward_pointer:
            if forward_pointer.data == head.data:
                prev.next = forward_pointer.next
            else:
                prev = forward_pointer
            forward_pointer = forward_pointer.next
        head = head.next



removeDups2(head)
printLL(head)





