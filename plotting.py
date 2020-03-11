"""
    Plotting template
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_results(graph, path, start_at, end_at):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.patch.set_visible(False)
    ax.axis('off')
    graph.plot(ax)
    for idx in range(1, len(path)):
        ax.plot([path[idx - 1].position[0], path[idx].position[0]],
                [path[idx - 1].position[1], path[idx].position[1]],
                [path[idx - 1].position[2], path[idx].position[2]], "c--", lw=2)
    graph[start_at].plot(ax, "co", "start")
    graph[end_at].plot(ax, "ro", "end")
    plt.title("Dijkstra Shortest Path Demo")
    if len(path) == 1:
        plt.suptitle("WARNING: Target cannot be reached!")
    plt.legend()
    return fig
