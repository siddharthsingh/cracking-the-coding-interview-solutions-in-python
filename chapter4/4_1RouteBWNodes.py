import queue


class Node():
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.distance = float('inf')
        self.visited = False

node_0 = Node('0')
node_1 = Node('1')
node_2 = Node('2')
node_3 = Node('3')
node_4 = Node('4')
node_5 = Node('5')
node_6 = Node('5')

edges = {}
edges[node_0] = [node_1,node_4,node_5]
edges[node_1] = [node_4,node_3]
edges[node_2] = [node_1]
edges[node_3] = [node_4,node_2]
edges[node_4] = []
edges[node_5] = []
edges[node_6] = []


def route_bw_nodes(start_node):
    start_node.distance = 0
    level = 1
    q = queue.Queue()
    q.put(start_node)
    start_node.visited = True
    while not q.empty():
        for adj_nodes in edges[q.get()]:
            if not adj_nodes.visited:
                q.put(adj_nodes)
                adj_nodes.visited = True
                adj_nodes.distance = level
        level += 1

route_bw_nodes(node_0)
print(node_5.distance)
print(node_6.distance)
