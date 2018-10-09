class Edge(object):

 def __init__(self, u, v, weight=1):

    self.u = u
    self.v = v
    self.weight = weight


class Graph(object):

    def __init__(self):
        self.__adjacency_list = {}


    def add_edge(self, edge):
        self.__adjacency_list.setdefault(edge.u, {})[edge.v] = edge.weight


    def get_distance_for_path(self, path):

        if len(path) < 2:
            raise Exception('must have minimum 2 paths')

        distance = 0

        for i in xrange(0, len(path)-1):
            current_vertex = path[i]
            next_vertex = path[i+1]

            if next_vertex in self.__adjacency_list[current_vertex]:
                distance += self.__adjacency_list[current_vertex][next_vertex]
            else:
                return 'NO SUCH ROUTE'

        return distance


    def get_num_paths(self, start, end, max_vertices=0, num_vertices=0):

        if not max_vertices and not num_vertices:
            raise ValueError('One of max_vertices or num_vertices must be defined')
        if start not in self.__adjacency_list:
            raise KeyError(start)
        if end not in self.__adjacency_list:
            raise KeyError(end)

        paths_found = list()
        max_length = max(max_vertices, num_vertices)
        self._find_paths([start], end, paths_found, max_length)

        # print paths_found

        num_paths = 0
        for path in paths_found:
            if max_vertices and len(path) - 1 <= max_vertices:
                num_paths += 1
            elif num_vertices and len(path) - 1 == num_vertices:
                num_paths += 1

        return num_paths


    def _find_paths(self, path, end, paths_found, max_length):

        if max_length and len(path) - 1 >= max_length:
            # no need to proceed if excdeeding defined max
            return

        last_vertex = path[-1]

        for neighbour in self.__adjacency_list[last_vertex]:
            if neighbour == end:
                paths_found.append(path + [neighbour])
            self._find_paths(path + [neighbour], end, paths_found, max_length)
