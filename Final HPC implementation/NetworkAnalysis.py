from igraph import Graph
import random
import networkx as nx


def nodesAndEdges(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    return num_nodes, num_edges


def avgDegree(G):

    num_nodes, num_edges = nodesAndEdges(G)
    avg_degree = (2 * num_edges) / num_nodes if num_nodes > 0 else 0
    print(f"Average Degree: {avg_degree:.2f}")


def avgPathLength(G):
    num_nodes, num_edges = nodesAndEdges(G)
    if num_nodes > 0:
        largest_component = max(nx.connected_components(G), key=len)
        G_largest = G.subgraph(largest_component).copy()
    ig_G = Graph.from_networkx(G_largest)
    # print(nodesAndEdges(G_largest))

    # Get approximate average path length
    approx_avg_path_length = ig_G.average_path_length()
    print("Approximate average path length:", approx_avg_path_length)



def clusteringCoefficient(G):

    global_clustering_coeff = nx.transitivity(G)
    print(f"Average Clustering Coefficient: {global_clustering_coeff:.2f}")


def approximate_avg_path_length(G):
    sample_size = 10000
    if not nx.is_connected(G):
        raise ValueError("Graph must be connected to compute average path length.")

    nodes = list(G.nodes())
    total_path_length = 0
    sampled_pairs = 0

    for _ in range(sample_size):
        u, v = random.sample(nodes, 2)  # Randomly select two distinct nodes
        try:
            length = nx.shortest_path_length(G, source=u, target=v)
            total_path_length += length
            sampled_pairs += 1
        except nx.NetworkXNoPath:
            continue
    avg_path_len = total_path_length / sampled_pairs if sampled_pairs > 0 else float("inf")
    print(f"Approximate Average Path Length: {avg_path_len}")
