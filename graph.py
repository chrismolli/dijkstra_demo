"""
    Definition of the Graph and Node classes
"""

import numpy as np

class Node:
    """
    NODE implements a node of the Graph class
    """

    def __init__(self, index):
        self.index = index
        self.distance = None
        self.previous = None
        self.neighbors = []
        self.position = np.zeros([0, 0, 0]).squeeze()

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def plot(self, axis, marker="ko", label="", fillstyle="none"):
        axis.plot([self.position[0]], [self.position[1]], [self.position[2]], marker, label=label,
                  fillstyle=fillstyle, markersize=15)


class Graph:
    """
    GRAPH implements a multi-directional graph
    """

    def __init__(self):
        self.nodes = []

    def __str__(self):
        text = f"Graph Object containing {len(self.nodes)} nodes:\n"
        for i, node in enumerate(self.nodes):
            text += f"node {i}, distance {node.distance}, edges {len(node.neighbors)}, position {node.position}\n"
        return text

    def __getitem__(self, key):
        return self.nodes[key]

    def __len__(self):
        return len(self.nodes)

    def create_random_graph(self, n_nodes=20, max_edges_per_node=5, graph_size=10):
        # limit edges
        max_edges_per_node = min(n_nodes - 1, max_edges_per_node)
        # create nodes
        self.nodes = [Node(i) for i in range(n_nodes)]
        # connect nodes randomly
        for node in self.nodes:
            node.position = np.random.rand(1, 3).squeeze() * graph_size
            n_edges = int(np.random.rand() * (max_edges_per_node - 1) + 1)
            for e in range(max(0,n_edges-len(node.neighbors))):
                neighbor = node
                while (neighbor is node or neighbor in node.neighbors):
                    neighbor = self.nodes[int(np.round(np.random.rand() * (n_nodes - 1)))]
                node.neighbors.append(neighbor)
                neighbor.neighbors.append(node)

    def get_number_of_nodes(self):
        return len(self.nodes)

    def remove_by_index(self, index):
        for node in self.nodes:
            if node.index == index:
                self.nodes.remove(node)
            else:
                for neighbor in node.neighbors:
                    if neighbor.index == index:
                        node.neighbors.remove(neighbor)

    def plot(self, axis):
        for node in self.nodes:
            node.plot(axis)
            for neighbor in node.neighbors:
                axis.plot([node.position[0], neighbor.position[0]],
                          [node.position[1], neighbor.position[1]],
                          [node.position[2], neighbor.position[2]], 'k-', lw=0.5)
