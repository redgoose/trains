import unittest

from graph import Graph

class TestGraph(unittest.TestCase):

    def test_adjacency_list(self):

        graph = Graph([
            ['A', 'B', 5],
            ['B', 'C', 4],
            ['C', 'D', 8],
            ['D', 'C', 8],
            ['D', 'E', 6],
            ['A', 'D', 5],
            ['C', 'E', 2],
            ['E', 'B', 3],
            ['A', 'E', 7]
        ])

        # accessing private attribute which is frowned upon, figured this was a valid exception
        adjacency_list = graph._Graph__adjacency_list

        self.assertEqual(adjacency_list['A'], {'B': 5, 'E': 7, 'D': 5})
        self.assertEqual(adjacency_list['E'], {'B': 3})
        self.assertEqual(len(adjacency_list), 5)

        graph = Graph([
            ['A', 'B', 5],
            ['B', 'C', 4],
            ['C', 'D', 8],
            ['D', 'E', 8],
            ['E', 'A', 6],
            ['A', 'C', 1]
        ])

        adjacency_list = graph._Graph__adjacency_list

        self.assertEqual(adjacency_list['A'], {'B': 5, 'C': 1})
        self.assertEqual(adjacency_list['E'], {'A': 6})
        self.assertEqual(len(adjacency_list), 5)

    def test_get_distance_for_path(self):

        graph = Graph([
            ['A', 'B', 5],
            ['B', 'C', 4],
            ['C', 'D', 8],
            ['D', 'E', 8],
            ['E', 'A', 6],
            ['A', 'C', 1]
        ])

        self.assertEqual(graph.get_distance_for_path(['A', 'C', 'D']), 9)
        self.assertEqual(graph.get_distance_for_path(['A', 'C']), 1)
        self.assertEqual(graph.get_distance_for_path(['A', 'A']), 'NO SUCH ROUTE')
        self.assertEqual(graph.get_distance_for_path(['E', 'A']), 6)
        self.assertEqual(graph.get_distance_for_path(['A', 'E']), 'NO SUCH ROUTE')

        with self.assertRaises(Exception):
            graph.get_distance_for_path(['A'])

    def test_get_num_paths(self):

        graph = Graph([
            ['A', 'B', 5],
            ['B', 'C', 4],
            ['C', 'D', 8],
            ['D', 'E', 8],
            ['E', 'A', 6],
            ['A', 'C', 1]
        ])

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
