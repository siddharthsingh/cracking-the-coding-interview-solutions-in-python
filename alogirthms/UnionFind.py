from collections import defaultdict


class Graph():
    def __init__(self,number_nodes):
        self.V = number_nodes
        self.E = defaultdict(list)
        self.parents = [-1]*self.V


    def add_edge(self,u,v):
        if u >= self.V or v >= self.V:
            return Exception("Node not in graph")
        self.E[u].append(v)

    def find_parent(self, node):
        if self.parents[node] == -1:
            return node
        return self.find_parent(self.parents[node])

    def union(self, u, v):
        parent_u = self.find_parent(u)
        parent_v = self.find_parent(v)
        self.parents[parent_u] = parent_v

    def find_cycles(self):
        for i in range(self.V):
            for adj_nodes in self.E[i]:
                x = self.find_parent(i)
                y = self.find_parent(adj_nodes)
                if x == y:
                    return True
                self.union(x,y)
        return False


g = Graph(4)
g.add_edge(0,2)
g.add_edge(2,1)
g.add_edge(2,3)
# g.add_edge(3,1)

print(g.find_cycles())

