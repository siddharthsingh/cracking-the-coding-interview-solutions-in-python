import random
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


def count_nodes(root):
    if not root:return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

store = []

def store_nodes_in_list(root):
    if not root:return
    global store
    store.append(root)
    store_nodes_in_list(root.left)
    store_nodes_in_list(root.right)

def get_random():
    ran = random.randint(0,count-1)
    return store[ran]

def insert(root,value):
    if not root:
        return Node(value)
    if value < root.name:
        if root.left:
            insert(root.left,value)
        else:
            root.left = Node(value)
            root.left.parent = root
    else:
        if root.right:
            insert(root.right, value)
        else:
            root.right.parent = root
            root.right = Node(value)


def find(root, value):
    if not root: return False
    if root.name == value:
        return root
    #binary tree not BST, otherwise we can check value to see if we have to go left or right
    a = find(root.left,value)
    if a:return a
    return find(root.right,value)

def delete(root,val):
    node = find(root,val)
    if not node:
        raise Exception("Node not in tree")
    if not node.left and not node.right:
        if node.parent.left == node:
            node.parent.left = None
        elif node.parent.right == node:
            node.parent.right = None

    else:
        temp = node
        while node.left or node.right:
            if node.left:
                node = node.left
            else:
                node = node.right
    # print(node)
    if node.parent.left == node:
        node.parent.left = None
    elif node.parent.right == node:
        node.parent.right = None
    temp.name = node.name

count = count_nodes(root3)
store_nodes_in_list(root3)
print(get_random())
print(get_random())
print(get_random())
print(get_random())
print(get_random())
print(get_random())
insert(root3,2)
print(count_nodes(root3))

print(find(root3,99))
print(find(root3,13))
print(find(root3,12))
print(find(root3,1))

print(count_nodes(root3))
delete(root3,9)
print(root310.left,"Asda")
print(count_nodes(root3))
print(root310.left)