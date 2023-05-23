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

# class Graph:
#     def __init__(self, V=(), E=()):
#         """ADD DOCSTRING"""
#         self.vertices = set(V)
#         self.edges = set(E)

#     def add_vertex(self, v):
#         """ADD DOCSTRING"""
#         self.vertices.add(v)

#     def remove_vertex(self, v):
#         """ADD DOCSTRING"""
#         self.vertices.discard(v)
#         self.edges = {(u, w, wt) for (u, w, wt) in self.edges if u != v and w != v}

#     def add_edge(self, u, v, wt):
#         """ADD DOCSTRING"""
#         self.edges.add((u, v, wt))

#     def remove_edge(self, u, v, wt):
#         """ADD DOCSTRING"""
#         self.edges.discard((u, v, wt))

#     def nbrs(self, v):
#         """ADD DOCSTRING"""
#         return [w for (u, w, _) in self.edges if u == v] + [u for (u, w, _) in self.edges if w == v]