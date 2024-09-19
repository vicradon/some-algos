import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    """
    Visualizes a weighted graph.

    Parameters:
    graph (dict): A dictionary where keys are node identifiers and values are dictionaries
                  of neighboring nodes and their respective weights.
                  
    Example:
    graph = {
        'A': {'B': 2, 'G': 4},
        'B': {'A': 2, 'C': 3},
        'C': {'B': 3, 'D': 5, 'E': 2},
        'D': {'C': 5, 'E': 1, 'F': 6},
        'E': {'C': 2, 'D': 1},
        'F': {'D': 6, 'G': 7},
        'G': {'A': 4, 'F': 7}
    }
    """
    
    # Create a new graph
    G = nx.Graph()

    # Add edges with weights to the graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Get positions for nodes
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)

    # Show the plot
    plt.axis('off')  # Hide the axes
    plt.show()
