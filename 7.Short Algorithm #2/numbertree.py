'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

import pprint
from itertools import combinations
from collections import defaultdict
from sys import getsizeof

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = {}
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2, weight in connections:
            self.add(node1, node2, weight)

    def add(self, node1, node2, weight):
        """ Add connection between node1 and node2 """

        try:
            f = self._graph[node1]
        except KeyError:
            self._graph[node1] = []

        self._graph[node1].append([node2,weight])
        if not self._directed:

            try:
                f = self._graph[node2]
            except KeyError:
                self._graph[node2] = []

            self._graph[node2].append([node1, weight])

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[], cost = ""):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path, cost
        if node1 not in self._graph:
            return None, cost
        for node in self._graph[node1]:
            if node[0] not in path:  
                new_cost = cost + node[1]
                new_path, finalcost = self.find_path(node[0], node2, path, new_cost)
                if new_path:
                    # print(finalcost)
                    return new_path, finalcost
        return None, ""

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


if __name__ == '__main__':


    # file = open('inputtext.txt', 'r')

    # pretty_print = pprint.PrettyPrinter()
    # number_of_nodes = int(file.readline())
    number_of_nodes = int(input())

    connections = []

    try:
        while True:
            
            # temp = file.readline()
            temp = input()
            node1, node2, weight = temp.split()
            connections.append((node1, node2, weight))

    except Exception:
        # print("Finished loading")
        pass

    
    g = Graph(connections, directed=False)


    # connections = list(combinations(range(1,number_of_nodes+1), 2))
    total_cost = 0
    for i in range(1, number_of_nodes + 1):
        for j in range(1, number_of_nodes + 1):
            if i < j:
                path, cost = g.find_path(str(i),str(j))
                # c = get_path_cost(path)
                if cost != "":
                    total_cost += int(cost)

    print(total_cost)









