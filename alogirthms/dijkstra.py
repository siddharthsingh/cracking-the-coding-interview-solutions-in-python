import heapq
class Node():
    def __init__(self,name):
        self.d = None
        self.name = name
        self.pi = None

weight_function = {}

s = Node("s")

t = Node('t')
y = Node('y')
x = Node('x')
z = Node('z')

weight_function[(s,t)] = 3
weight_function[(s,y)] = 5
weight_function[(t,y)] = 2
weight_function[(y,t)] = 1
weight_function[(z,s)] = 3
weight_function[(y,x)] = 4
weight_function[(t,x)] = 6
weight_function[(y,z)] = 6
weight_function[(x,z)] = 2
weight_function[(z,x)] = 7

adjacency_dict = {}

adjacency_dict[s] = [t,y]
adjacency_dict[t] = [x,y]
adjacency_dict[y] = [t,z,x]
adjacency_dict[x] = [z]
adjacency_dict[z] = [s,x]


def dijkstra(adj_dic,weights,start_node):
    keys = []
    for key in adj_dic:
        if key !=start_node:
            key.d = 9999999
        else:
            key.d = 0
        key.pi = None
        keys.append(key)

    s = []
    while keys:
        u = min(keys, key=lambda x:(x.d,x.name))
        keys.remove(u)
        s.append(u)
        for vertex in adj_dic[u]:
            if vertex not in s and vertex.d > u.d+weights[(u,vertex)]:
                vertex.d = u.d+weights[(u,vertex)]
                vertex.pi = u

    print(keys)

dijkstra(adjacency_dict,weight_function,s)
print(z.d)
print("")
st = z
while st:
    print(st.d,st.name)
    st = st.pi

