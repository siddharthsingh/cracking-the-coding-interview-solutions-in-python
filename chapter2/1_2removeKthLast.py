class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

nums_to_insert = [1,2,3,3,4,5,6]
head = Node(nums_to_insert[0])
temp = head
for num in nums_to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next


def removeKthLast(head_, k):
    if k==0 and not head_.next:
        global head
        head = None

    delete_pointer = head_
    i = 0
    while head_:
        if i > k+1:
            delete_pointer = delete_pointer.next
        head_ = head_.next

        i += 1

    if delete_pointer and delete_pointer.next and i > k:
        delete_pointer.next = delete_pointer.next.next

def printLL(head):
    while head:
        print(head.data, end = ", ")
        head = head.next

printLL(head)
removeKthLast(head,1)
print("")
printLL(head)









