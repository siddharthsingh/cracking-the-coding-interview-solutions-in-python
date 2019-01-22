class Node():
    def __init__(self,data):
        self.data = data
        self.next = None



to_insert = ['a','b','b','a']
head = Node(to_insert[0])
temp = head
for num in to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next

to_insert = ['a','b','c','b','a']
head2 = Node(to_insert[0])
temp = head2
for num in to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next

to_insert = ['a','b','b','c','a']
head3 = Node(to_insert[0])
temp = head3
for num in to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next

to_insert = ['a','b','c','a']
head4 = Node(to_insert[0])
temp = head4
for num in to_insert[1:]:
    temp.next = Node(num)
    temp = temp.next



def printLL(head):
    while head:
        print(head.data,end="")
        head = head.next
    print('')


def is_palindrome(head):
    if not head:return False
    forward_pointer = head
    trailing_pointer = head
    while forward_pointer and forward_pointer.next and trailing_pointer:
        trailing_pointer = trailing_pointer.next
        forward_pointer = forward_pointer.next.next
    stop_forward_at = trailing_pointer
    if forward_pointer:
    #     odd length

        trailing_pointer = trailing_pointer.next


    forward_pointer = head
    temp = trailing_pointer
    stack = []
    while temp:
        stack.append(temp.data)
        temp = temp.next
    # print(stack)
    while forward_pointer != stop_forward_at:
        if forward_pointer.data != stack.pop():
            return False
        forward_pointer = forward_pointer.next
    return True

printLL(head)
printLL(head2)
printLL(head3)
printLL(head4)


print(is_palindrome(head))
print(is_palindrome(head2))
print(is_palindrome(head3))
print(is_palindrome(head4))
