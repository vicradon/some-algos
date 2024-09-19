from collections import deque
from graph_visualizer import visualize_graph

def dijkstra_shortest_path(graph, starting_node):
    spanning_tree = dict()
    visited = set()
    queue = deque([starting_node])
    inf = float("inf")

    for key in graph:
        spanning_tree[key] = [inf, None]

    spanning_tree[starting_node] = [0, None]


    while queue:
        current_vertex = queue.popleft()
        children = graph[current_vertex]
        min_neighbor_dist = inf
        next_node = None

        for node in children:
            calculated_distance = spanning_tree[current_vertex][0] + children[node]

            if calculated_distance < spanning_tree[node][0]:
                spanning_tree[node][0] = calculated_distance

                spanning_tree[node][1] = current_vertex


        for node in children:
            if spanning_tree[node][0] < min_neighbor_dist:
                min_neighbor_dist = spanning_tree[node][0]
                next_node = node

        visited.add(current_vertex)

        if next_node not in visited:
            queue.append(next_node)

    return spanning_tree
    

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    graph1 = {
        'A': {'B': 2, 'D': 3},
        'B': {'A': 2, 'C': 4},
        'C': {'B': 4, 'D': 1, 'E': 7},
        'D': {'A': 3, 'C': 1},
        'E': {'C': 7}
    }

    graph2 = {
        'A': {'B': 1, 'E': 2},
        'B': {'A': 1, 'C': 5},
        'C': {'B': 5, 'D': 1},
        'D': {'C': 1, 'E': 3},
        'E': {'A': 2, 'D': 3}
    }


    graph3 = {
        'A': {'B': 3, 'F': 2},
        'B': {'A': 3, 'C': 1},
        'C': {'B': 1, 'D': 6, 'E': 2},
        'D': {'C': 6, 'E': 1},
        'E': {'C': 2, 'D': 1, 'F': 4},
        'F': {'A': 2, 'E': 4}
    }


    graph4 = {
        'A': {'B': 2, 'G': 4},
        'B': {'A': 2, 'C': 3},
        'C': {'B': 3, 'D': 5, 'E': 2},
        'D': {'C': 5, 'E': 1, 'F': 6},
        'E': {'C': 2, 'D': 1},
        'F': {'D': 6, 'G': 7},
        'G': {'A': 4, 'F': 7}
    }

    graph4 = {
        'A': {'B': 2, 'G': 4},
        'B': {'A': 2, 'C': 3},
        'C': {'B': 3, 'D': 5, 'E': 2},
        'D': {'C': 5, 'E': 1, 'F': 6},
        'E': {'C': 2, 'D': 1},
        'F': {'D': 6, 'G': 7},
        'G': {'A': 4, 'F': 7}
    }

    starting_node = "A"


    spanning_tree = dijkstra_shortest_path(graph4, starting_node)
    print(spanning_tree)

    visualize_graph(graph4)

