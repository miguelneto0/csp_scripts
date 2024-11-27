import networkx as nx
import matplotlib.pyplot as plt
from itertools import product, chain
from scenarios import domains_ex, scenarios

def expand_value(value, domain):
    """Expande os valores com base nos operadores especiais."""
    if isinstance(value, int):
        return [value], False
    
    if value == '*':
        return domain, True
    elif '>' in value or '<' in value:
        if '>=' in value:
            return [x for x in domain if x >= int(value[2:])], True
        elif '<=' in value:
            return [x for x in domain if x <= int(value[2:])], True
        elif '>' in value:
            return [x for x in domain if x > int(value[1:])], True
        elif '<' in value:
            return [x for x in domain if x < int(value[1:])], True
        elif '!=' in value:
            return [x for x in domain if x != int(value[2:])], True
    else:
        if isinstance(value, int):
            return [int(value)], False
        elif isinstance(value, str):
            return [str(value)], False
        
def generate_standard_table(table, domains):
    """Gera a tabela extensional expandindo valores com operadores."""
    attributes = table[0]
    std_table = []
    cmp_table = []
    idxs_smart = []

    for row in table[1:]:
        expanded_rows = []
        hasSmart = False
        for attr, value in zip(attributes, row):
            new_rows, isSmart = expand_value(value, domains[attr])
            expanded_rows.append(new_rows)
            if isSmart == True:
                hasSmart = True
        cmp_table.append(expanded_rows)
        prev = len(std_table)
        std_table.extend(product(*expanded_rows))
        crrt = len(std_table)
        if hasSmart == True:
            thrs = crrt - prev
            indexes = list(range(len(std_table) - thrs, len(std_table)))
            for i in indexes:
                idxs_smart.append(i)
    print(f'idxs_smart = {idxs_smart}')
        
    return std_table, cmp_table

def compress_table(std_table):
    """ Gera a tabela compacta (compressed table) a partir da tabela standard (std_table) """
    compressed_table = []

    # Itera pelas colunas (índices das colunas)
    for col_idx in range(len(std_table[0])):  # Número de colunas na primeira linha
        unique_values = set()  # Para armazenar valores únicos dessa coluna
        
        # Itera pelas linhas e coleta valores da coluna atual
        for row in std_table:
            unique_values.add(row[col_idx])
        
        # Adiciona os valores únicos como uma lista para a tabela compactada
        compressed_table.append(sorted(unique_values))

    # Transforma em formato de lista de listas
    return [[list(column) for column in compressed_table]]

def create_csp_graph(table, domains):
    """Cria o grafo e identifica colisões."""
    G = nx.DiGraph()
    G.add_node("ROOT")
    G.add_node("SINK")

    standard_tab, compres_tab = generate_standard_table(table, domains)

    # Rastreamento de caminhos únicos e conflitos
    unique_paths = set()
    collisions = []

    # Processa cada tupla na tabela standard
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

def print_tab(standard_tab):
    print(f'Table:')
    for i, row in enumerate(standard_tab):
        print(f"{i}: {row}")

def plot_graph(G):
    pos = nx.spring_layout(G)  # Layout automático
    plt.figure(figsize=(12, 8))

    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1400, font_size=8, font_weight='bold')
    plt.title("CSP Graph with Collision Detection", fontsize=14)
    plt.show()


def update_collision_table(standard_tab, collisions, show_collisions):
    indexes_to_remove = []

    if show_collisions == True:
        # Exibe conflitos detectados
        print("Detected collisions:")
    for collision in collisions:
        idx_collis = collision["tuple_index"]
        if idx_collis not in indexes_to_remove:
            indexes_to_remove.append(idx_collis)
        if show_collisions == True:
            print(collision)

        print(f'collision tuples: {indexes_to_remove}')

    # Atualiza tabela sem conflitos
    standard_tab = [row for i, row in enumerate(standard_tab) if i not in indexes_to_remove]
    print("Table after removal:")
    for i, row in enumerate(standard_tab):
        print(f"{i}: {row}")
    return standard_tab, indexes_to_remove

scenario = scenarios[2]

if __name__ == "__main__":
    # Criação e visualização do grafo
    graph, collisions = create_csp_graph(scenario, domains_ex)
    plot_graph(graph)

    print("Original table:")
    for i, row in enumerate(scenario):
        print(f"{row}")

    # Cria e mostra standard table
    standard_tab, compres_tab = generate_standard_table(scenario, domains_ex)
    print(f'Standard -')
    print_tab(standard_tab)
    print(f'Compressed - ')
    print_tab(compres_tab)

    update_collision_table(standard_tab, collisions, True)
    # compr = compress_table(std_tab)
    # print_tab(compr)
    