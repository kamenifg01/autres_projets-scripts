import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def louvain_algorithm(graph):
    # Initialisation : Chaque nœud est initialisé dans sa propre communauté
    communities = {node: [node] for node in graph.nodes()}

    while True:
        # Phase 1 : Optimisation locale de la modularité pour chaque nœud
        for node in graph.nodes():
            current_community = communities[node]
            best_community = current_community
            max_modularity_gain = 0.0

            for neighbor in graph.neighbors(node):
                # Ajouter le voisin à communities s'il n'est pas déjà présent
                if neighbor not in communities:
                    communities[neighbor] = [neighbor]

                # Calcul du gain de modularité en déplaçant le nœud vers la communauté du voisin
                new_community = communities[neighbor]
                modularity_gain = calculate_modularity_gain(graph, communities, node, current_community, new_community)

                # Mise à jour du meilleur gain
                if modularity_gain > max_modularity_gain:
                    max_modularity_gain = modularity_gain
                    best_community = new_community

            # Déplacer le nœud vers la communauté offrant le meilleur gain
            if best_community != current_community:
                current_community.remove(node)
                best_community.append(node)

        # Phase 2 : Agréger les nœuds des mêmes communautés
        new_communities = {}
        for nodes in communities.values():
            if nodes:
                community_repr = nodes[0]
                new_communities[community_repr] = nodes

        # Vérifier s'il y a eu un changement dans les communautés
        if communities == new_communities:
            break

        communities = new_communities

    return communities



def calculate_modularity_gain(graph, communities, node, current_community, new_community):
    # Calcul de la modularité avant le déplacement
    Q_before = calculate_modularity(graph, communities)

    # Effectuer le déplacement virtuel du nœud
    current_community.remove(node)
    new_community.append(node)

    # Calcul de la modularité après le déplacement
    Q_after = calculate_modularity(graph, communities)

    # Annuler le déplacement virtuel
    new_community.remove(node)
    current_community.append(node)

    # Calculer le gain de modularité
    modularity_gain = Q_after - Q_before

    return modularity_gain

def calculate_modularity(graph, communities):
    m = graph.number_of_edges()
    Q = 0.0

    for community in communities.values():
        for i in range(len(community)):
            for j in range(len(community)):
                node_i = community[i]
                node_j = community[j]

                A_ij = 1 if graph.has_edge(node_i, node_j) else 0
                k_i = graph.degree(node_i)
                k_j = graph.degree(node_j)

                Q += (A_ij - (k_i * k_j) / (2 * m))

    return Q / (2 * m)


# Fonction pour visualiser le graphe avec les communautés détectées
def plot_communities(graph, communities):
    pos = nx.spring_layout(graph)  # Positionnement des nœuds pour une meilleure visualisation
    colors = [i for i in range(len(communities))]
    community_colors = [colors.index(community_repr) for community_repr in communities.values() for _ in community_repr]

    nx.draw(graph, pos, node_color=community_colors, with_labels=True, cmap=plt.cm.rainbow)
    plt.show()

# Construction du graphe
edges = [('A', 'B'), ('A', 'E'), ('B', 'C'), ('C', 'F'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('E', 'F')]
G = nx.Graph()
G.add_edges_from(edges)

# Exécution de l'algorithme de Louvain
communities = louvain_algorithm(G)

# Affichage des communautés
for i, nodes in enumerate(communities.values(), 1):
    print(f'Communauté {i}: {nodes}')

    # Visualisation du graphe avec les communautés
plot_communities(G, communities)
