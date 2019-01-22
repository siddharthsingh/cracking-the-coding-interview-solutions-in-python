class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

head = node1
head.next = node2
head.next.next = node3
head.next.next.next = node4
head.next.next.next.next = node5



head2 = node6
head2.next = node3


head3 = node7
node7.next = node8
node8.next = node9


def printLL(head):
    while head:
        print(head.data,end=", ")
        head = head.next
    print("")

def intersection(list1,list2):
    if not list1 or not list2:return False
    len1 = 0
    len2 = 0
    temp1 = list1
    temp2 = list2
    while temp1:
        len1 += 1
        temp1 = temp1.next

    while temp2:
        len2 += 1
        temp2 = temp2.next

    larger_list, shorter_list = (list1,list2) if len1>len2 else (list2,list1)
    to_remove = abs(len1-len2)
    # print(larger_list.data)
    while to_remove:
        to_remove -= 1
        larger_list = larger_list.next

    while larger_list:
        if larger_list == shorter_list:
            return True
        larger_list = larger_list.next
        shorter_list = shorter_list.next
    return False




printLL(head)
printLL(head2)
printLL(head3)

print(intersection(head,head2))
print(intersection(head,head3))
print(intersection(head2,head3))