"""
    This script demonstrates the use of the dijkstra module written in Python 3.6

    Dependencies: numpy, matplotlib

    Note: Due to the random generation of the graph it can generate targets that are unable to reach.
          Therefore, if no path is plotted try running the simulation again.
"""

from dijkstra import dijkstra
from graph import Graph
from plotting import plot_results

import numpy as np
import matplotlib.pyplot as plt

# generate random graph
graph = Graph()
graph.create_random_graph(n_nodes=10, max_edges_per_node=4, graph_size=20)

# randomly select start and end point
start_at = int(np.random.rand() * graph.get_number_of_nodes())
end_at = start_at
while (end_at == start_at):
    end_at = int(np.random.rand() * graph.get_number_of_nodes())

# generate shortest path
path = dijkstra(graph, start_at, end_at)
print(graph)

# visualize results
fig = plot_results(graph, path, start_at, end_at)
plt.show()
