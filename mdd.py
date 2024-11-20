import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, value, node):
        self.children[value] = node

    def __repr__(self):
        return f"Node({self.name}, Children: {list(self.children.keys())})"


class MDD:
    def __init__(self):
        self.root = Node("Root")
        self.sink = Node("Sink")

    def add_path(self, path):
        current_node = self.root
        for value in path:
            if value not in current_node.children:
                current_node.add_child(value, Node(value))
            current_node = current_node.children[value]
        current_node.add_child("End", self.sink)

    def to_graph(self):
        graph = nx.DiGraph()  # Grafo direcionado
        self._add_edges(self.root, graph, "Root")
        return graph

    def _add_edges(self, node, graph, parent_name):
        for value, child in node.children.items():
            child_name = f"{child.name}"  # Nome do nó filho
            edge_label = str(value)  # Valor da aresta
            graph.add_edge(parent_name, child_name, label=edge_label)  # Adiciona a aresta ao grafo
            self._add_edges(child, graph, child_name)  # Recursão para processar os filhos


def plot_graph(graph):
    # Layout do grafo
    pos = nx.spring_layout(graph, seed=42)  # Define o layout para consistência
    labels = nx.get_edge_attributes(graph, "label")  # Obtém os rótulos das arestas

    # Desenha o grafo
    plt.figure(figsize=(10, 7))
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=9)
    plt.title("MDD Graph", fontsize=16)
    plt.show()


# Exemplo de uso
def generate_mdd(table):
    mdd = MDD()
    for row in table:
        mdd.add_path(row)
    return mdd

# Tabela de exemplo
table = [
    [1, 2, 1],
    [1, 2, 3],
    [1, 3, 2],
    [1, 3, 1]
]

# Gera o MDD e converte para um grafo
mdd = generate_mdd(table)
graph = mdd.to_graph()

# Plota o grafo
plot_graph(graph)
