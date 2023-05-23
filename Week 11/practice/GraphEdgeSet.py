class EdgeSet:
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self,v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        self.E.remove(e)
    
    def __iter__(self):
        return iter(self.V)
    
    def _neighbors(self, v):
        nbrs = set()
        for e in self.E:
            #edges that look like (v,?)
            if e[0] == v: nbrs.add(e[1])
        return nbrs

class Graph(EdgeSet):
    pass

if __name__ == '__main__':
    g = Graph()
    vs = {1,3,2,4}
    es = {(1,2), (1,3), (1,4),
          (2,1), (2,3),
          (3,1), (3,2), (3,4),         
          (4,1), (4,3)
          }
    for v in vs: g.add_vertex(v)
    for e in es: g.add_edge(e)

    for v in g:
        print(f"v = {v}, neighbors:")
        for nbr in g._neighbors(v):
            print(f"\t{nbr}")
        print()