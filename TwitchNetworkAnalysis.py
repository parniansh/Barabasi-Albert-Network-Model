import networkx as nx
import NetworkAnalysis as na


file_path = 'large_twitch_edges.txt'


def analyze_network():
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)

    na.avgDegree(G)
    na.clusteringCoefficient(G)
    na.approximate_avg_path_length(G)
