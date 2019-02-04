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
root14 = Node(5)
root13 = Node(5)
root16 = Node(5)
root17 = Node(5)
root1.left =  root14
root1.right = root16
root14.left = root13
root16.right = root17


root2  = Node(12)
root210  = Node(12)
root29  = Node(12)
root28  = Node(12)
root211  = Node(12)
root213  = Node(12)

root2.left = root210
root2.right = root213
root210.left = root29
root210.right = root211
root29.left = root28


def is_balanced(root):
    if not root:return 0
    lh = is_balanced(root.left)
    rh = is_balanced(root.right)
    if abs(lh - rh) > 1:
        print("not balanced")
    return lh+1 if lh > rh else rh+1


is_balanced(root1)
print("balanced")
is_balanced(root2)