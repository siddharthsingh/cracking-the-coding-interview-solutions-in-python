import queue


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


def BFS(start_node):
        # initialize
    for edge in edges:
        edge.distance = float('inf')
        edge.parent = None

    q = queue.Queue(maxsize = 20)
    q.put(start_node)
    start_node.distance = 0
    level = 1
    while not q.empty():
        node = q.get()
        for adj_node in edges[node]:
            if not adj_node.visited:
                q.put(adj_node)
                adj_node.visited = True
                adj_node.distance = level
        level += 1

BFS(node_0)
print(node_5.distance)


