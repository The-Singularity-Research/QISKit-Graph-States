import networkx as nx
from networkx.algorithms import bipartite
import numpy as np
from qiskit import *


class BipartiteGraphState(QuantumCircuit):

    def __init__():
        super().__init__(self, bipartite_graph)
        self.graph = bipartite_graph
        # Create a quantum register based on the number of nodes
        # in W + the number of nodes in B (= total number of nodes in G)
        self.white_nodes, self.black_nodes = bipartite.sets(self.graph)
        self.qreg = QuantumRegister(len(self.black_nodes) + len(self.white_nodes))
        self.creg = ClassicalRegister(len(self.black_nodes) + len(self.white_nodes))
        # Create a circuit using the quantum register
        self.circuit = QuantumCircuit(self.qreg, self.creg)
        # For each vertex in W, apply a Hadamard gate
        for vertex in self.white_nodes:
            self.circuit.h(vertex)
        # For each vertex in B, apply a Hadamard gate
        for vertex in self.black_nodes:
            self.circuit.h(vertex)
        # For each edge e={x,y} apply a controlled-Z gate on its vertices
        for x, y in self.graph.edges:
            self.circuit.cz(x, y)
        self.node_dict = self.build_node_dict()

        def build_node_dict(self):
            self.node_dict = dict()
            for count, node in enumerate(self.graph.nodes):
                self.node_dict[node] = count

        def x_measurement(self, qubit, cbit):
            """Measure 'qubit' in the X-basis, and store the result in 'cbit'"""
            self.circuit.h(qubit)
            self.circuit.measure(qubit, cbit)
            self.circuit.h(qubit)

        def x_measure_white(self):
            self.circuit.barrier()
            for vertex in self.black_nodes:
                self.circuit.measure(vertex, vertex)
            self.circuit.barrier()
            for vertex in self.white_nodes:
                self.x_measurement(self.circuit, vertex, vertex)

        def x_measure_black(self):
            self.circuit.barrier()
            for vertex in self.white_nodes:
                self.circuit.measure(vertex, vertex)
            self.circuit.barrier()
            for vertex in self.black_nodes:
                self.x_measurement(self.circuit, vertex, vertex)

        def apply_stabilizer(self, node):
            self.circuit.x(self.node_dict[node])
            for neighbor in self.graph.neighbors(node):
                self.circuit.cz(self.node_dict[node], self.node_dict[neighbor])
