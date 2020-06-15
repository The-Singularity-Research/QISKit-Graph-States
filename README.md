# QISKit-Graph-States 

For two notebook tutorials on graph states, see the [error correction notebook](https://github.com/The-Singularity-Research/error-correction) and the [quantum cryptography notebook](https://github.com/The-Singularity-Research/graph-state-quantum-cryptography).

Graph states in this repository can be used for:

- Measurement Based Quantum Computing (MBQC) (see [Completeness of classical spin models and universal
quantum computation](https://arxiv.org/pdf/0812.2368.pdf))
- error correction, 
- Quantum Cryptography and blind quantum computation (see for example [Graph States for Quantum Secret Sharing](https://arxiv.org/pdf/0808.1532.pdf) and [Verifiable measurement-only blind quantum computing with stabilizer testing](https://arxiv.org/pdf/1505.07535.pdf), 
- modeling Ising type models to study quantum complexity using partition functions (see Section 5 of [Measurement-based quantum computation](https://arxiv.org/pdf/0910.1116.pdf)
- modeling quantum phase transitions (see A. Kitaev's lecture on [Topological quantum phases](https://www.youtube.com/watch?v=W2vUbTR2RWQ&t=898s)), 
- studying entanglement entropy and entanglement as a computational resource (see [Entanglement in Graph States and its Applications](https://arxiv.org/pdf/quant-ph/0602096.pdf)
- modeling condensed matter physics on IBM quantum computers. 
- Modeling quantum/classical information processing in DNA for applications to Bio-informatics, protien folding, and understanding applications of CRISPR (see for example [Adiabatic graph-state quantum computation](https://arxiv.org/pdf/1309.1443.pdf) and [Quantum entanglement between the electron clouds of nucleic acids in DNA](https://arxiv.org/pdf/1006.4053.pdf), which also has an accompanying Google lecture [Classical and Quantum Information in DNA (Google Workshop on Quantum Biology)](https://www.youtube.com/watch?v=2nqHOnVTxJE&t=66s))


### MBQC

---

Measurement Based Quantum Computing is one way of performing adaptive measurements on a highly entangled system of qubits so that entanglement is used as a resource, which is gradually reduced after each measurement on individual qubits. This is one of the primary uses of graph states, and using the graphs given by surface codes, this can be done in a way that is topologically protected from errors. Morevover, the measurement based approach makes the computation "one-way", which can also protect against errors by making the thermal requirements less strict (see [From molecular biology to quantum computing - Charles H. Bennett](https://www.youtube.com/watch?v=a-i_yhLLkiY&t=48s)).

The classes are subclasses of IBM Qiskit objects or of NetworkX objects. 
