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


if __name__ == '__main__':
    main()
