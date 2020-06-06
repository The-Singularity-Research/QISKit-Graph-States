
from qiskit import *

class GraphState(QuantumCircuit):

    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        # Create a quantum register based on the number of nodes in G
        self.qreg = QuantumRegister(len(self.graph.nodes))
        self.creg = ClassicalRegister(len(self.graph.nodes))
        # Create a circuit using the quantum register
        self.circuit = QuantumCircuit(self.qreg, self.creg)
        # For each vertex, apply a Hadamard gate
        for vertex in self.graph.nodes:
            self.circuit.h(vertex)
        # For each edge e={x,y} apply a controlled-Z gate on its vertices
        for x, y in self.graph.edges:
            self.circuit.cz(x, y)
        self.node_dict = self.build_node_dict()


    def build_node_dict(self):
        """
        create a node dictionary from node to integer index of a qubit
        in a Qiskit circuit
        :param self:
        """
        self.node_dict = dict()
        for count, node in enumerate(self.graph.nodes):
        self.node_dict[node] = count

    def x_measurement(self, qubit, cbit):
        """Measure 'qubit' in the X-basis, and store the result in 'cbit'"""
        self.circuit.h(qubit)
        self.circuit.measure(qubit, cbit)
        self.circuit.h(qubit)
    
    def apply_stabilizer(self, node):
        """
        applies the stabilizer generator corresponding to node
        :param self:
        :param node: a node in self.graph
        """
        self.circuit.x(self.node_dict[node])
        for neighbor in self.graph.neighbors(node):
        self.circuit.cz(self.node_dict[node], self.node_dict[neighbor])


