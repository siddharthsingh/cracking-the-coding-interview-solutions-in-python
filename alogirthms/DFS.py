
class Node():
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.distance = 0
        self.visited = False

node_0 = Node('0')
node_1 = Node('1')
node_2 = Node('2')
node_3 = Node('3')
node_4 = Node('4')
node_5 = Node('5')

edges = {}
edges[node_0] = [node_1,node_4,node_5]
edges[node_1] = [node_4,node_3]
edges[node_2] = [node_1]
edges[node_3] = [node_4,node_2]
edges[node_4] = []
edges[node_5] = []


def DFS(start_node):
    print(start_node.name)
    start_node.visited = True
    for node in edges[start_node]:
        if not node.visited:
            DFS(node)

DFS(node_0)
print(node_5.distance)



