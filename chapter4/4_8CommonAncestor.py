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
root39  = Node(1)
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



def common_ancestor(node1,node2):
    temp1 = node1
    temp2 = node2
    count1 = 0
    count2 = 0
    while temp1:
        temp1 = temp1.parent
        count1 += 1
    while temp2:
        temp2 = temp2.parent
        count2 += 1
    longer_node,shorter_node = (node1,node2) if count1 > count2 else (node2,node1)
    diff = abs(count1-count2)

    while diff:
        diff -= 1
        longer_node = longer_node.parent
    while longer_node != shorter_node:
        longer_node = longer_node.parent
        shorter_node = shorter_node.parent

    return longer_node


print(common_ancestor(root311,root39))
print(common_ancestor(root311,root38))
print(common_ancestor(root311,root310))
print(common_ancestor(root311,root313))
print(common_ancestor(root38,root313))

