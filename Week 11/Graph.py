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
            self.nbrs[a] = {b:weight}
        else:
            self.nbrs[a][b]= weight

        if b not in self.nbrs:
            self.nbrs[b] = {a: weight}
        else:   
            self.nbrs[b][a] = weight

    def remove_edge(self, e):
        a, b = e
        del self.nbrs[a][b]

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
        
    def bfs(self,v):
        tree = {} #dictionary of child: parent pairs
        to_visit = [(None,v)] #stack of parent, child tuples

        while to_visit:
            a, b = to_visit.pop(0) # a,b = (parent, child)
            if b not in tree:
                tree[b] = a
                for n in self._neighbors(b):
                    to_visit.append((b,n))

        return tree
    
    def fewest_flights(self, source, destination):
        visited = set()
        to_visit = [(None, source)]  # (parent, vertex) tuples
        traversal_tree = {None: source}  # Dictionary to store the traversal tree

        while to_visit:
            parent, current = to_visit.pop(0)
            if current == destination:
                return traversal_tree  # Return the traversal tree instead of the level

            visited.add(current)
            for neighbor in self._neighbors(current):
                if neighbor not in visited:
                    to_visit.append((current, neighbor))
                    traversal_tree[neighbor] = current  # Store the parent-child relationship in the traversal tree

        # If the destination is not reachable, return None or a specific value indicating unreachability
        return None
    
    def shortest_distance(self, source, destination):
        distances = {v: None for v in self.V}
        distances[source] = 0

        visited = set()
        traversal_tree = {}

        while len(visited) < len(self.V):
            min_distance = float('inf')
            min_vertex = None

            for v in self.V:
                if v not in visited and distances[v] is not None and distances[v] < min_distance:
                    min_distance = distances[v]
                    min_vertex = v

            visited.add(min_vertex)

            for neighbor in self._neighbors(min_vertex):
                weight = self.nbrs[min_vertex][neighbor]
                new_distance = distances[min_vertex] + weight

                if distances[neighbor] is None or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    traversal_tree[neighbor] = min_vertex

        return traversal_tree

    
    def salt(self):
        visited = set()  # Set to keep track of visited vertices
        min_span_tree = {}  # Dictionary to store the minimum spanning tree

        # Start with an arbitrary vertex as the initial vertex
        initial_vertex = next(iter(self.V))
        visited.add(initial_vertex)

        while len(visited) < len(self.V):
            min_edge = None
            min_weight = float('inf')

            # Find the minimum weight edge that connects a visited vertex to an unvisited vertex
            for v in visited:
                for neighbor, weight in self.nbrs[v].items():
                    if neighbor not in visited and weight < min_weight:
                        min_edge = (v, neighbor)
                        min_weight = weight

            if min_edge:
                u, v = min_edge
                min_span_tree[v] = (u, min_weight)
                visited.add(v)

        return min_span_tree

if __name__ == '__main__':
    g = Graph()
    vs = {1,2,3}
    es = {((1,2),5), ((2,3),5),((1,3),12)
          }
    
    
    for v in vs: g.add_vertex(v)
    for e,weight in es: g.add_edge(e,weight)


    print(f"bfs(2) = {g.bfs(2)}")

    # for v in g:
    #     print(f"v = {v}, neighbors:")
    #     for nbr in g._neighbors(v):
    #         print(f"\t{nbr}")
    #     print()

    # print(f"dfs(4) = {g.dfs(4)}")
    # print()
    # print(f"dfs_iter(4) = {g.dfs_iter(4)}")

    # print(f"bfs(4) = {g.bfs(4)}")
