class LLNode():
    def __init__(self,graph_node):
        self.graph_node = graph_node
        self.next =  None

class Node():
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.distance = float('inf')
        self.visited = False
        self.start_time = float('inf')
        self.end_time = float('inf')

    def __repr__(self):
        return self.name + ", "+str(self.start_time) + " , "+ str(self.end_time)+ str(self.visited)

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')

edges = {}
edges[node_a] = [node_d]
edges[node_b] = [node_d]
edges[node_c] = []
edges[node_d] = [node_c]
edges[node_e] = []
edges[node_f] = [node_b, node_a]

time = 0
list_ = []
head_ll = None


def insert_start_list(graph_node):
    global head_ll
    node = LLNode(graph_node)
    node.next = head_ll
    head_ll = node


def dfs(start_node):
    global time
    start_node.start_time = time
    start_node.visited = True
    time += 1
    for adj_node in edges[start_node]:
        if not adj_node.visited:
            dfs(adj_node)
        elif adj_node.visited and adj_node.end_time == float('inf'):
            raise Exception("cycle detected",start_node,adj_node)

    start_node.end_time = time
    insert_start_list(start_node)
    time += 1

def print_ll():
    temp = head_ll
    while temp:
        print(temp.graph_node.name, end = ", ")
        temp = temp.next

    print("")

for node in edges:
    if not node.visited:
        dfs(node)

print_ll()
for node in edges:
    print(node)

