import networkx as nx
import matplotlib.pyplot as plt

frontier = []


def generate_graph(num_v, num_e):
    return nx.gnm_random_graph(num_v, num_e)


def main():
    for i in range(10):
        graph = generate_graph(10, 5)
        subax1 = plt.subplot(121)
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()
        print(nx.is_connected(graph))

        # for graph with e edges, k can be in the range 1 to e - 1
        # if k is e - 1, the graph will be fully connected. If edges
        # are unweighted, shortest path computation is trivial
        # if k is 1, graph will be simple and shortest path is straight forward
        aug = nx.k_edge_augmentation(graph, 5)
        graph.add_edges_from(aug)
        subax1 = plt.subplot(121)
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()
        print(nx.is_connected(graph))



if __name__ == '__main__':
    main()
