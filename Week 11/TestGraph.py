from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""
        self.g = Graph()
        vs = {"Seattle", "Chicago", "Boston", "New Orleans","Los Angeles"}
        es = {(("Seattle", "Chicago"),2040),
              (("Chicago", "Boston"),980),
              (("Boston", "New Orleans"),1520),
              (("New Orleans", "Los Angeles"),1890),
              (("Los Angeles", "Seattle"),1140)
            }
        for v in vs: self.g.add_vertex(v)
        for e, weight in es: self.g.add_edge(e, weight)


        

    # # TODO: Add unittests for public interface of Graph class (except traversal algs)
    def test_add_vertex(self):
        self.g.add_vertex('New York')
        self.g.add_edge(("New York", "Los Angeles"),3000)
        self.assertIn('New York', self.g)
        # print("New York has been added")

    def test_remove_vertex(self):
        self.g.add_vertex('New York')
        self.g.remove_vertex("New York")
        self.assertNotIn('New York', self.g)
        # print("New York never existed")

    def test_add_edge(self):
        self.g.add_edge(("Boston", "Los Angeles"), 3500)
        self.assertEqual(self.g.nbrs["Boston"]["Los Angeles"], 3500)
        self.assertEqual(self.g.nbrs["Los Angeles"]["Boston"], 3500)
        # print("added edge with weights!")

    def test_remove_edge(self):
        self.g.add_edge(("Boston", "Los Angeles"), 3500)
        self.assertEqual(self.g.nbrs["Boston"]["Los Angeles"], 3500)
        self.g.remove_edge(("Boston", "Los Angeles"))
        self.assertNotIn((("Boston", "Los Angeles"),3500), self.g)
        # print("Boston LA Route Terminated")
        
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """Setup Flight and weighted flight routes"""
        self.g = Graph()
        vs = {"Seattle", "Chicago", "Boston", "New Orleans","Los Angeles"}
        es = {(("Seattle", "Chicago"),2040),
              (("Chicago", "Boston"),980),
              (("Boston", "New Orleans"),1520),
              (("New Orleans", "Los Angeles"),1890),
              (("Los Angeles", "Seattle"),1140)
            }
        for v in vs: self.g.add_vertex(v)
        for e, weight in es: self.g.add_edge(e, weight)
        # print("Graph Traversal has been initialized")

    # TODO: Which alg do you use here, and why?
    # Alg: Breadth first search
    # Why: We should use a breadth first serach because we are looking to return the shortest path from one node to a terminal node and can short circuit at the first solution.
    def test_fewest_flights(self):
        """Test to find out if you can get what the fewest number of flights are from one node to another node within the graph"""
        num_flights = self.g.fewest_flights("Seattle", "Boston")
        print(num_flights)
        # num_flights2 = self.g.fewest_flights("Seattle", "Los Angeles")
        # self.assertEqual(num_flights, 2)
        # self.assertEqual(num_flights2, 1)
        # print("Shortest flight numbers are good!")
        

    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra's Search
    # Why: We should use Dijkstra's because it specifically seeks out the minimum distance from node to node.
    def test_shortest_path(self):
        """ADD DOCSTRING"""
        shortest_distance = self.g.shortest_distance("Seattle", "New Orleans")
        print(shortest_distance)  # Output: The shortest distance between Seattle and Boston
        


    # TODO: Which alg do you use here, and why?
    # Alg: Prim's Algorithm
    # Why: Because it is return the minimum distance of all nodes
    def test_salt(self):
        """ADD DOCSTRING"""
        minimum_distance = self.g.salt()
        print(minimum_distance)


unittest.main(verbosity=2)