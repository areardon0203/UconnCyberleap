class AdjacencySet:
    def __init__(self):
        self.V = set()
        self.nbrs = dict()

    def add_vertex(self,v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e, weight):
        a, b = e
        if a not in self.nbrs:
            self.nbrs[a] = {b: weight}
        else:
            self.nbrs[a][b] = weight

        # If the graph is undirected, you may also add the reverse edge with the same weight
        if b not in self.nbrs:
            self.nbrs[b] = {a: weight}
        else:
            self.nbrs[b][a] = weight

    def remove_edge(self, e):
        a, b = self.nbrs[a].remove(b)

        if len(self.nbrs[a]) == 0:
            self.nbrs.pop(a)
    
    def __iter__(self):
        return iter(self.V)
    
    def _neighbors(self, v):
        return  iter(self.nbrs[v])

class Graph(AdjacencySet):
    
    def dfs(self, v):
#        tree = {None:v}
        tree = {v:None}
        return self._dfs(v, tree)
    
    def _dfs(self, v, tree):
        for n in self._neighbors(v):
            if n not in tree:
                tree[n] = v
                return self._dfs(n, tree)
        return tree
    
    def dfs_iter(self,v):
        tree = {} #dictionary of child: parent pairs
        to_visit = [(None,v)] #stack of parent, child tuples

        while to_visit:
            a, b = to_visit.pop() # a,b = (parent, child)
            if b not in tree:
                tree[b] = a
                for n in self._neighbors(b):
                    to_visit.append((b,n))

        return tree

if __name__ == '__main__':
    g = Graph()
    vs = {1,3,2,4,5,6}
    es = {(1,2), (1,3), (1,4),
          (2,1), (2,3),
          (3,1), (3,2), (3,4), (3,5),(3,6),      
          (4,1), (4,3),
          (5,3), (5,6),
          (6,3), (6,4), (6,5)
          }
    for v in vs: g.add_vertex(v)
    for e in es: g.add_edge(e)

    for v in g:
        print(f"v = {v}, neighbors:")
        for nbr in g._neighbors(v):
            print(f"\t{nbr}")
        print()

    print(f"dfs(4) = {g.dfs(4)}")
    print()
    print(f"dfs_iter(4) = {g.dfs_iter(4)}")
