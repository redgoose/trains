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

        for i in range(0, len(path)-1):
            current_vertex = path[i]
            next_vertex = path[i+1]

            if next_vertex in self.__adjacency_list[current_vertex]:
                distance += self.__adjacency_list[current_vertex][next_vertex]
            else:
                return 'NO SUCH ROUTE'

        return distance


    def get_num_paths(self, start, end, restriction):

        if start not in self.__adjacency_list:
            raise KeyError(start)
        if end not in self.__adjacency_list:
            raise KeyError(end)

        paths_found = list()
        self._find_paths([start], end, paths_found, restriction)

        # print paths_found

        return len(paths_found)


    def _find_paths(self, path, end, paths_found, restriction):

        last_vertex = path[-1]

        if (restriction.get('max_vertices') and len(path) >= restriction.get('max_vertices')):
            return

        if (restriction.get('num_vertices') and len(path) >= restriction.get('num_vertices')):
            return

        for neighbour in self.__adjacency_list[last_vertex]:

            if (restriction.get('max_distance') and self.get_distance_for_path(path + [neighbour]) > restriction.get('max_distance')):
                continue

            if restriction.get('num_vertices'):
                if neighbour == end and len(path + [neighbour]) == restriction.get('num_vertices'):
                    paths_found.append(path + [neighbour])

            elif neighbour == end:
                paths_found.append(path + [neighbour])


            self._find_paths(path + [neighbour], end, paths_found, restriction)


    def get_min_distance(self, start, end):

        if start == end:
            distance = float('inf')

            next_node = None
            for v in self.__adjacency_list[start]:
                dist, prev = self._dijkstra(v)
                if dist[start] < distance:
                    next_node = v
                    distance = dist[start] + self.__adjacency_list[start][next_node]
        else :
            dist, prev = self._dijkstra(start)
            distance = dist[end]

        return distance


    def _dijkstra(self, source):
        q = set()
        dist = {}
        prev = {}

        for v in self.__adjacency_list: # initialization
            dist[v] = float('inf') # unknown distance from source to v
            prev[v] = float('inf') # previous node in optimal path from source
            q.add(v) # all nodes initially in q (unvisited nodes)

        # # distance from source to source
        dist[source] = 0

        while q:
            # node with the least distance selected first
            min_dist = float('inf')
            node = next(iter(q))
            for u in q:
                if dist[u] < min_dist:
                    min_dist = dist[u]
                    node = u
            u = node

            q.remove(u)

            for v in self.__adjacency_list[u]: # where v is still in q
                alt = dist[u] + self.__adjacency_list[u][v]
                if alt < dist[v]: # a shorter path to v has been found
                    dist[v] = alt
                    prev[v] = u

        return dist, prev

