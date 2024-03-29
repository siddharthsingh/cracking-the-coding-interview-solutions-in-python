class Node():
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return self.name

root3  = Node(12)
root310  = Node(10)
root39  = Node(9)
root38  = Node(8)
root311  = Node(11)
root313  = Node(13)

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



def inorder_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    if not node.parent:
        return -1
    q = node
    p = node.parent
    while p and p.left != q:
        q = p
        p = p.parent



    return p if p else -1


print(inorder_successor(root311))
print(inorder_successor(root39))
print(inorder_successor(root313))
print(inorder_successor(root310))
print(inorder_successor(root3))