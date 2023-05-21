from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""
        self.g = Graph()

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
    def test_add_vertex(self):
        self.g.add_vertex('A')
        self.assertIn('A', self.g.vertices)

    def test_remove_vertex(self):
        self.g.add_vertex('A')
        self.g.remove_vertex('A')
        self.assertNotIn('A', self.g.vertices)

    def test_add_edge(self):
        self.g.add_vertex('A')
        self.g.add_vertex('B')
        self.g.add_edge('A', 'B', 5)
        self.assertIn(('A', 'B', 5), self.g.edges)

    def test_remove_edge(self):
        self.g.add_vertex('A')
        self.g.add_vertex('B')
        self.g.add_edge('A', 'B', 5)
        self.g.remove_edge('A', 'B', 5)
        self.assertNotIn(('A', 'B', 5), self.g.edges)
        
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_fewest_flights(self):
        """ADD DOCSTRING"""
 

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_shortest_path(self):
        """ADD DOCSTRING"""

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_minimum_salt(self):
        """ADD DOCSTRING"""

unittest.main()