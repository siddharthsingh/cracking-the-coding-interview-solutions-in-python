class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(0)
temp = head
for i in range(1,10):
    temp.next = Node(i)
    temp = temp.next

for i in range(100,110):
    temp.next = Node(i)
    temp = temp.next


def printLL(head):
    print("-------------------------")
    while head:
        print(head.data)
        head = head.next

def runner(head):
    pointer1 = head
    pointer2 = head
    while(pointer1):
        pointer1 = pointer1.next.next
        pointer2 = pointer2.next

    # print(pointer1.data,pointer2.data)
    temp1 = head
    temp2 = pointer2
    pointer2_cache = pointer2
    while temp1 and temp2:
        if temp1.next == pointer2_cache:
            temp1.next = temp2
            break
        pointer1 = temp1
        pointer2 =  temp2
        temp1 = pointer1.next
        pointer1.next = pointer2
        temp2 = pointer2.next
        pointer2.next = temp1


runner(head)
printLL(head)