"""
	Implementation of the Dijkstra algorithm
"""

from copy import deepcopy
import numpy as np

def dijkstra(graph, start_at=0, end_at=-1):
    """
    DIJKSTRA implements dijkstra's shortest path solution routing a path from the start_at node to the end_at node

    :param graph: A Graph object containing the graph to search
    :param start_at: A Integer denoting the index of the starting node
    :param end_at: A Integer denoting the index of target node, if -1 the last node of the graph is taken
    :return: A List object containing the node sequence of the shortest path to the target
    """
    # init graph for dijkstra
    for node in graph:
        node.previous = None
        if node.index == start_at:
            node.distance = 0
        else:
            node.distance = float("inf")
    # copy graph
    working_graph = deepcopy(graph)
    # start dijkstra algorithm
    while len(working_graph):
        closest_node = working_graph[np.argmin(working_graph)]
        working_graph.remove_by_index(closest_node.index)
        for neighbor in closest_node.neighbors:
            if neighbor in working_graph:
                new_distance = closest_node.distance + np.linalg.norm(closest_node.position - neighbor.position)
                if new_distance < neighbor.distance:
                    # update working graph
                    neighbor.distance = new_distance
                    neighbor.previous = closest_node
                    # update original graph
                    graph[neighbor.index].distance = new_distance
                    graph[neighbor.index].previous = graph[closest_node.index]
    # create sequence of shortest path
    sequence = [graph[end_at]]
    while sequence[0].previous != None:
        sequence.insert(0, sequence[0].previous)
    return sequence
