import networkx as nx
import matplotlib.pyplot as plt
from itertools import product

def expand_value(value, domain):
    """Expande os valores com base nos operadores especiais."""
    if isinstance(value, int):
        return [value]
    
    if value == '*':
        return domain
    elif '>' in value or '<' in value:
        if '>=' in value:
            return [x for x in domain if x >= int(value[2:])]
        elif '<=' in value:
            return [x for x in domain if x <= int(value[2:])]
        elif '>' in value:
            return [x for x in domain if x > int(value[1:])]
        elif '<' in value:
            return [x for x in domain if x < int(value[1:])]
        elif '!=' in value:
            return [x for x in domain if x != int(value[2:])]
    else:
        return [int(value)]

def generate_standard_table(table, domains):
    """Gera a tabela extensional expandindo valores com operadores."""
    attributes = table[0]
    pure_table = []

    for row in table[1:]:
        expanded_rows = []
        for attr, value in zip(attributes, row):
            expanded_rows.append(expand_value(value, domains[attr]))
        pure_table.extend(product(*expanded_rows))

    return pure_table

def create_csp_graph(table, domains):
    """Cria o grafo e identifica colisões."""
    G = nx.DiGraph()
    G.add_node("ROOT")
    G.add_node("SINK")

    standard_tab = generate_standard_table(table, domains)

    # Rastreamento de caminhos únicos e conflitos
    unique_paths = set()
    collisions = []

    # Processa cada tupla na tabela pura
    for index, row in enumerate(standard_tab, start=0):
        path = ["ROOT"]
        conflict_detected = False

        for attr, value in zip(table[0], row):
            current_node = f"{attr}{value}"
            path.append(current_node)

        path.append("SINK")
        path_tuple = tuple(path)

        # Verifica se o caminho já existe
        if path_tuple in unique_paths:
            conflict_detected = True
            for attr, value in zip(table[0], row):
                collisions.append({
                    "attribute": attr,
                    "value": value,
                    "tuple_index": index
                })
        else:
            unique_paths.add(path_tuple)  # Adiciona caminho único
            # Adiciona arestas no grafo
            for i in range(len(path) - 1):
                G.add_edge(path[i], path[i + 1])

    return G, collisions

def plot_graph(G):
    pos = nx.spring_layout(G)  # Layout automático
    plt.figure(figsize=(12, 8))

    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1400, font_size=8, font_weight='bold')
    plt.title("CSP Graph with Collision Detection", fontsize=14)
    plt.show()

# Domínios dos atributos
domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3, 4],
    'C': [1, 2, 3, 4, 5],
    'D': [8, 9, 10]
}

# Nova tabela de exemplo
table = [
    ['A', 'B', 'C'],  # Atributos
    [1, 2, 3],
    [3, 2, 4]
]

table1 = [
    ['A', 'B', 'C'],  # Atributos
    [1, 2, '*'],
    [3, '>2', 4],
    [1, 2, '>3']
]
table2 = [
    ['A', 'B', 'C'],
    [1, ">2", 1],
    [2, 2, 2],   
    [1, "*", 1]]

table3 = [
    ['A', 'B', 'C'],
    [1, 1, 1],
    [2, 2, 2],   
    [1, 1, "*"]]

table4 = [
    ['A', 'B', 'C'],
    [1, ">2", 1],
    [2, 2, 2],   
    [1, 3, 1]]

table5 = [
    ['A', 'B', 'C'],
    [1, 1, "*"],
    [2, 2, 2],   
    [1, "*", 1]]

table6 = [
    ['A', 'B', 'C'],
    [1, 1, "*"],
    [2, 2, 2],   
    [1, 1, 1], 
    [2, "*", 2]]

table7 = [
    ['A', 'B', 'C'],
    [1, 1, "*"],
    [1, "*", 1]]

table8 = [
    ['A', 'B', 'C'],
    [1, "*", 1],
    [1, "*", "*"],
    [1, 1, "*"]]

table9 = [
    ['A', 'B', 'C'],
    [1, 1, "*"],
    [1, "*", 1],
    [1, "*", "*"]]

table10 = [
    ['A', 'B', 'C'],
    [1, 1, "*"],
    [1, 1, "*"],
    [1, "*", "*"]]

table11 = [
    ['A', 'B', 'C'],
    [1, '>5', 1],
    ['<=10', 2, '<3'],
    ['>=4', 1, '*']
]

scenario = table2

# Criação e visualização do grafo
graph, collisions = create_csp_graph(scenario, domains)
plot_graph(graph)

print("Original table:")
for i, row in enumerate(scenario):
    print(f"{row}")

standard_tab = generate_standard_table(scenario, domains)
print("Standard table:")
for i, row in enumerate(standard_tab):
    print(f"{i}: {row}")

indexes_to_remove = []

# Exibe conflitos detectados
print("Detected collisions:")
for collision in collisions:
    idx_collis = collision["tuple_index"]
    if idx_collis not in indexes_to_remove:
        indexes_to_remove.append(idx_collis)
    print(collision)

print(f'collision tuples: {indexes_to_remove}')
standard_tab = [row for i, row in enumerate(standard_tab) if i not in indexes_to_remove]
print("Table after removal:")
for i, row in enumerate(standard_tab):
    print(f"{i}: {row}")