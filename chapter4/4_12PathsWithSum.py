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


def total_paths(root,sum):
    if not root:return 0
    diff = sum-root.name
    if diff < 0:
        return 0
    if diff == 0:
        return 1
    return total_paths(root.left, diff) + total_paths(root.right, diff)


def start_count(root,sum):
    if not root:return 0
    count = total_paths(root, sum)
    left_count = start_count(root.left, sum)
    right_count = start_count(root.right, sum)
    return count+left_count+right_count

print(start_count(root3,9))
print(start_count(root3,18))