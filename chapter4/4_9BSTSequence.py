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

ans = [[]]

def generate_sequences(root):
    # global ans
    if not root: return
    an = []
    a = generate_sequences(root.left)
    b = generate_sequences(root.right)
    if not a and not b:
        return [[root.name]]
    if not a:
        for x in b:
            x.insert(0,root.name)
        return b
    if not b:
        for x in a:
            x.insert(0,root.name)
        return a
    for aa in a:
        for bb in b:
            an.append(aa+bb)
            an.append(bb+aa)
    for x in an:
        x.insert(0,root.name)

    return an


generate_sequences(root3)
print(generate_sequences(root3))


