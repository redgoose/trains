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
        graph.add_edge(Edge('A', 'E', 1))

        # invalid end
        with self.assertRaises(KeyError):
            graph.get_num_paths(start='A', end='F', restriction={'max_vertices': 3})

        # invalid start
        with self.assertRaises(KeyError):
            graph.get_num_paths(start='G', end='A', restriction={'max_vertices': 3})

        self.assertEqual(graph.get_num_paths(start='A', end='C', restriction={'num_vertices': 2}), 1)

        self.assertEqual(graph.get_num_paths(start='A', end='E', restriction={'num_vertices': 3}), 0)

        self.assertEqual(graph.get_num_paths(start='A', end='A', restriction={'num_vertices': 7}), 3)

        self.assertEqual(graph.get_num_paths(start='A', end='A', restriction={'max_vertices': 7}), 7)


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


    def test_get_paths_with_distance(self):

        graph = Graph()
        graph.add_edge(Edge('A', 'B', 5))
        graph.add_edge(Edge('B', 'C', 4))
        graph.add_edge(Edge('C', 'D', 8))
        graph.add_edge(Edge('D', 'E', 8))
        graph.add_edge(Edge('E', 'A', 1))
        graph.add_edge(Edge('A', 'C', 1))
        graph.add_edge(Edge('A', 'E', 1))

        self.assertEqual(graph.get_num_paths(start='A', end='A', restriction={'max_distance': 6}), 3)

        self.assertEqual(graph.get_num_paths(start='B', end='C', restriction={'max_distance': 1}), 0)

        self.assertEqual(graph.get_num_paths(start='A', end='E', restriction={'max_distance': 1}), 1)

        self.assertEqual(graph.get_num_paths(start='B', end='D', restriction={'max_distance': 12}), 1)


    def test_large_graph(self):

        graph = Graph()

        for i in range(0, 1000):
            graph.add_edge(Edge(str(i), str(i + 1), 5))

            graph.add_edge(Edge(str(i), str(500), 5))
        graph.add_edge(Edge(str(1000), str(250), 5))

        self.assertEqual(graph.get_distance_for_path(['0', '1', '2']), 10)
        self.assertEqual(graph.get_num_paths(start='0', end='500', restriction={'max_distance': 50}), 1023)
        self.assertEqual(graph.get_min_distance(start='50', end='51'), 5)
        self.assertEqual(graph.get_min_distance(start='1000', end='250'), 5)
        self.assertEqual(graph.get_min_distance(start='0', end='1000'), 2505)


class TestQuestions(unittest.TestCase):

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


    def test_question_1(self):
        self.assertEqual(self.graph.get_distance_for_path(['A', 'B', 'C']), 9)


    def test_question_2(self):
        self.assertEqual(self.graph.get_distance_for_path(['A', 'D']), 5)


    def test_question_3(self):
        self.assertEqual(self.graph.get_distance_for_path(['A', 'D', 'C']), 13)


    def test_question_4(self):
        self.assertEqual(self.graph.get_distance_for_path(['A', 'E', 'B', 'C', 'D']), 22)


    def test_question_5(self):
        self.assertEqual(self.graph.get_distance_for_path(['A', 'E', 'D']), 'NO SUCH ROUTE')


    def test_question_6(self):
        self.assertEqual(self.graph.get_num_paths(start='C', end='C', restriction={'max_vertices': 4}), 2)


    def test_question_7(self):
        self.assertEqual(self.graph.get_num_paths(start='A', end='C', restriction={'num_vertices': 5}), 3)


    def test_question_8(self):
        self.assertEqual(self.graph.get_min_distance(start='A', end='C'), 9)


    def test_question_9(self):        
        self.assertEqual(self.graph.get_min_distance(start='B', end='B'), 9)


    def test_question_10(self):
        self.assertEqual(self.graph.get_num_paths(start='C', end='C', restriction={'max_distance': 29}), 7)


if __name__ == '__main__':
    unittest.main()
