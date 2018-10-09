import unittest

from graph import Edge, Graph

class TestEdge(unittest.TestCase):

    def test_edge(self):

        edge = Edge('A', 'B')

        self.assertEqual(edge.u, 'A')
        self.assertEqual(edge.v, 'B')
        self.assertEqual(edge.weight, 1)

        edge = Edge('X', 'Y', 15)

        self.assertEqual(edge.u, 'X')
        self.assertEqual(edge.v, 'Y')
        self.assertEqual(edge.weight, 15)

class TestGraph(unittest.TestCase):

    def test_adjacency_list(self):

        graph = Graph()
        graph.add_edge(Edge('A', 'B', 5))
        graph.add_edge(Edge('B', 'C', 4))
        graph.add_edge(Edge('C', 'D', 8))
        graph.add_edge(Edge('D', 'C', 8))
        graph.add_edge(Edge('D', 'E', 6))
        graph.add_edge(Edge('A', 'D', 5))
        graph.add_edge(Edge('C', 'E', 2))
        graph.add_edge(Edge('E', 'B', 3))
        graph.add_edge(Edge('A', 'E', 7))

        # accessing private attribute which is frowned upon, figured this was a valid exception
        adjacency_list = graph._Graph__adjacency_list

        self.assertEqual(adjacency_list['A'], {'B': 5, 'E': 7, 'D': 5})
        self.assertEqual(adjacency_list['E'], {'B': 3})
        self.assertEqual(len(adjacency_list), 5)

        graph = Graph()
        graph.add_edge(Edge('A', 'B', 5))
        graph.add_edge(Edge('B', 'C', 4))
        graph.add_edge(Edge('C', 'D', 8))
        graph.add_edge(Edge('D', 'E', 8))
        graph.add_edge(Edge('E', 'A', 6))
        graph.add_edge(Edge('A', 'C', 1))

        adjacency_list = graph._Graph__adjacency_list

        self.assertEqual(adjacency_list['A'], {'B': 5, 'C': 1})
        self.assertEqual(adjacency_list['E'], {'A': 6})
        self.assertEqual(len(adjacency_list), 5)

    def test_get_distance_for_path(self):

        graph = Graph()
        graph.add_edge(Edge('A', 'B', 5))
        graph.add_edge(Edge('B', 'C', 4))
        graph.add_edge(Edge('C', 'D', 8))
        graph.add_edge(Edge('D', 'E', 8))
        graph.add_edge(Edge('E', 'A', 6))
        graph.add_edge(Edge('A', 'C', 1))

        self.assertEqual(graph.get_distance_for_path(['A', 'C', 'D']), 9)
        self.assertEqual(graph.get_distance_for_path(['A', 'C']), 1)
        self.assertEqual(graph.get_distance_for_path(['A', 'A']), 'NO SUCH ROUTE')
        self.assertEqual(graph.get_distance_for_path(['E', 'A']), 6)
        self.assertEqual(graph.get_distance_for_path(['A', 'E']), 'NO SUCH ROUTE')

        with self.assertRaises(Exception):
            graph.get_distance_for_path(['A'])

    def test_get_num_paths(self):

        graph = Graph()
        graph.add_edge(Edge('A', 'B', 5))
        graph.add_edge(Edge('B', 'C', 4))
        graph.add_edge(Edge('C', 'D', 8))
        graph.add_edge(Edge('D', 'E', 8))
        graph.add_edge(Edge('E', 'A', 6))
        graph.add_edge(Edge('A', 'C', 1))

        self.assertEqual(graph.get_num_paths(start='A', end='C', max_vertices=3), 2)

        # unbounded lookup
        with self.assertRaises(ValueError):
            graph.get_num_paths(start='A', end='C')

        # invalid end
        with self.assertRaises(KeyError):
            graph.get_num_paths(start='A', end='F', max_vertices=3)

        # invalid start
        with self.assertRaises(KeyError):
            graph.get_num_paths(start='G', end='A', max_vertices=3)

        self.assertEqual(graph.get_num_paths(start='A', end='C', num_vertices=2), 1)

        self.assertEqual(graph.get_num_paths(start='A', end='E', num_vertices=2), 0)


    def test_get_min_distance(self):

        graph = Graph()
        graph.add_edge(Edge('A', 'E', 1))
        graph.add_edge(Edge('A', 'B', 5))
        graph.add_edge(Edge('B', 'C', 4))
        graph.add_edge(Edge('C', 'D', 8))
        graph.add_edge(Edge('D', 'E', 8))
        graph.add_edge(Edge('E', 'A', 6))
        graph.add_edge(Edge('A', 'C', 1))

        self.assertEqual(graph.get_min_distance(start='A', end='A'), 7)
        self.assertEqual(graph.get_min_distance(start='A', end='C'), 1)
        self.assertEqual(graph.get_min_distance(start='A', end='B'), 5)
        self.assertEqual(graph.get_min_distance(start='A', end='E'), 1)
        self.assertEqual(graph.get_min_distance(start='E', end='A'), 6)

if __name__ == '__main__':
    unittest.main()
