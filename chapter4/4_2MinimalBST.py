import queue


class Node():
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None



def create_bst(sorted_list, start, end):
    if start > end:return
    mid = (start+end)//2
    node = Node(sorted_list[mid])
    left = create_bst(sorted_list,start,mid-1)
    right = create_bst(sorted_list,mid+1,end)
    node.left = left
    node.right = right
    return node

def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

root = create_bst([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 0, 13)
print(inorder(root))