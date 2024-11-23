import networkx as nx
import random
import NetworkAnalysis as na


def barabasi_albert_graph(n, m):
    G = nx.complete_graph(m)

    degrees = [G.degree[node] for node in G.nodes]
    for new_node in range(m, n):
        targets = set()

        while len(targets) < m:
            node = random.choices(list(G.nodes), weights=degrees, k=1)[0]
            targets.add(node)

        G.add_node(new_node)

        for target in targets:
            G.add_edge(new_node, target)
            degrees[target] += 1

        degrees.append(m)
        if G.number_of_nodes() % 10000 == 0: print(f"Current number of nodes: {G.number_of_nodes()}")

    return G



def analyze_network(n, m):
    # G = nx.read_edgelist("barabasi_albert_network.edgelist", nodetype=int)
    G = barabasi_albert_graph(n,m)
    nx.write_graphml(G, "Barabasi-Twitch.graphml")
    nx.write_edgelist(G, "Barabasi-Twitch", data=True)
    na.avgDegree(G)
    na.clusteringCoefficient(G)
    na.approximate_avg_path_length(G)

