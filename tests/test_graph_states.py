import unittest

import networkx as nx

from GraphStates import *


class GraphStateTest(unittest.TestCase):
    def setUp(self):
        self.G = nx.Graph()
        self.G.add_edges_from([(0, 1), (1, 2)])

    def test_init_edges(self):
        a = GraphState(self.G)
        self.assertEqual(sorted(a.graph.edges), sorted([(0, 1), (1, 2)]))


if __name__ == '__main__':
    unittest.main()
