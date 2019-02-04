class Node():
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

root1 = Node(5)
root14 = Node(4)
root13 = Node(3)
root16 = Node(6)
root17 = Node(7)
root1.left =  root14
root1.right = root16
root14.left = root13
root16.right = root17


root2  = Node(12)
root210  = Node(10)
root29  = Node(9)
root28  = Node(8)
root211  = Node(11)
root213  = Node(13)

root2.left = root210
root2.right = root213
root210.left = root29
root210.right = root211
root29.left = root28


root3  = Node(12)
root310  = Node(10)
root39  = Node(1)
root38  = Node(8)
root311  = Node(11)
root313  = Node(13)

root3.left = root310
root3.right = root313
root310.left = root39
root310.right = root311
root39.left = root38


def bst_is_valid(root):
    if not root:return True
    a = True
    if root.left and root.name < root.left.name:
        return False
    elif root.left:
        a = bst_is_valid(root.left)
    if root.right and root.name > root.right.name:
        return False
    elif root.right:
        a &= bst_is_valid(root.right)

    return a

print(bst_is_valid(root1))
print(bst_is_valid(root2))
print(bst_is_valid(root3))