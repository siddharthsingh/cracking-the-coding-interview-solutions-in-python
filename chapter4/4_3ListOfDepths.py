import queue


class Node():
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.distance = -1
        self.visited = False


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

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


def dfs(start_node):
    level = 1
    start_node.distance = 0
    start_node.visited = True
    q = queue.Queue()
    q.put(start_node)
    while not q.empty():
        node = q.get()
        added = False
        for adj_nodes in edges[node]:
            if not adj_nodes.visited:
                q.put(adj_nodes)
                adj_nodes.visited = True
                adj_nodes.distance = level
                added = True
        if added:
            level += 1
    create_list_of_depths(level)

def create_list_of_depths(level):
    list_depths = [[] for _ in range(level+1)]
    for node in edges:
        print(node)
        list_depths[node.distance].append(node)
    print(list_depths)
#
# def print_all_levels(list_depths):
#     for list_ in list_depths:
#         print(list_)

dfs(node_0)

