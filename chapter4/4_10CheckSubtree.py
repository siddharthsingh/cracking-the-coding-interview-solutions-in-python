class Node():
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None


    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

root3  = Node(12)
root310  = Node(10)
root39  = Node(9)
root38  = Node(8)
root311  = Node(11)
root313  = Node(13)
root31  = Node(1)
root34  = Node(4)
root33  = Node(3)
root35  = Node(5)

root3.left = root310
root310.parent = root3
root3.right = root313
root313.parent = root3
root310.left = root39
root39.parent = root310
root310.right = root311
root311.parent = root310
root39.left = root38
root38.parent = root39
root38.left = root31
root31.parent = root38
root31.right = root34
root34.parent = root31
root34.left = root33
root33.parent = root34
root34.right = root35
root35.parent = root34


def inorder(groot):
    if not groot:return []
    a = inorder(groot.left)
    b = [groot.name]
    c = inorder(groot.right)
    return a+b+c


def pre_order(groot):
    if not groot:return []
    a = [groot.name]
    b = inorder(groot.left)
    c = inorder(groot.right)
    return a+b+c

def check_subtree(tree1,tree2):
    while tree2 and tree2 != tree1:
        tree2 = tree2.parent
    return bool(tree2)


def check_subtree2(tree1,tree2):
    inorder_tree1 = inorder(tree1)
    inorder_tree2 = inorder(tree2)
    a = all(x in inorder_tree1 for x in inorder_tree2)

    pre_order_tree1 = pre_order(tree1)
    pre_order_tree2 = pre_order(tree2)
    b = all(x in pre_order_tree1 for x in pre_order_tree2)
    return a&b


print(check_subtree2(root310,root34))
print(inorder(root3))


