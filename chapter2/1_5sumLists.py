class Node():
    def __init__(self,digit):
        self.digit = digit
        self.next = None

number_one = Node(7)
number_one.next = Node(1)
number_one.next.next = Node(6)
# number_one.next.next.next = Node(9)

number_two = Node(5)
number_two.next = Node(9)
number_two.next.next = Node(2)

def forward_sum(num1,num2):
    ans = Node((num1.digit+num2.digit)%10)
    ans_temp = ans
    carry = (num1.digit+num2.digit)//10
    num1 = num1.next
    num2 = num2.next
    while num1 or num2:
        if not num1:
            num1 = Node(0)
        if not num2:
            num2 = Node(0)

        ans_temp.next = Node((num1.digit + num2.digit+carry) % 10)
        carry = (num1.digit + num2.digit+carry) // 10
        num1 = num1.next
        num2 = num2.next
        ans_temp = ans_temp.next
    if carry:
        ans_temp.next = Node(carry)
    return ans


def reverseSum(num1,num2):
    if not num1 or not num2:return None
    if num1.next and num2.next:
        temp_ret_node,ret_carry = reverseSum(num1.next,num2.next)
        temp_node = Node((num1.digit + num2.digit+ret_carry) % 10)
        carry = (num1.digit + num2.digit + ret_carry) // 10
        temp_node.next = temp_ret_node
        return temp_node,carry
    elif num1.next:
        temp_ret_node, ret_carry = reverseSum(num1.next,Node(0))
        temp_node = Node((num1.digit + num2.digit+ret_carry) % 10)
        carry = (num1.digit + num2.digit + ret_carry) // 10
        temp_node.next = temp_ret_node
        return temp_node,carry
    elif num2.next:
        temp_ret_node, ret_carry = reverseSum(Node(0),num2.next)
        temp_node = Node((num1.digit + num2.digit+ret_carry) % 10)
        carry = (num1.digit + num2.digit + ret_carry) // 10
        temp_node.next = temp_ret_node
        return temp_node,carry
    else:
    #     noth none
        temp_node = Node((num1.digit + num2.digit)%10)
        carry = (num1.digit + num2.digit) // 10
        return temp_node,carry


def printLL(head):
    while head:
        print(head.digit,end=", ")
        head = head.next
    print("")
temp_ans,carry = reverseSum(number_one,number_two)
# print(carry)
ans = Node(carry)
ans.next = temp_ans
printLL(ans)
printLL(forward_sum(number_one,number_two))



