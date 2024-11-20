import pandas as pd
import networkx as nx
import hypernetx as hnx
import matplotlib.pyplot as plt

def criar_grafo(tabela):
    G = nx.DiGraph()            # Criando um grafo direcionado
    G.add_node("root")          # Nodo inicial
    nodos_finais = ["root"]     # Iniciando com o nodo 'root'
    
    # Iterando sobre os atributos do dicionário
    for key, valores in tabela.items():
        novos_nodos = []
        
        # Conectar cada nodo final anterior com os novos valores
        for nodo in nodos_finais:
            for valor in valores:
                G.add_edge(nodo, valor)  # Adiciona aresta do nodo anterior para o valor
                novos_nodos.append(valor)
        
        # Atualizar a lista de nodos finais
        nodos_finais = novos_nodos
    
    # Conectar todos os nodos finais ao nodo 'sink'
    G.add_node("sink")
    for nodo in nodos_finais:
        G.add_edge(nodo, "sink")

    return G

def plotar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Layout do grafo
    plt.figure(figsize=(10, 8))
    nx.draw(grafo, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
    plt.show()

# Dicionário de atributos e seus domínios
atributos_dominios = {
    'A': [0, 1],
    'B': [2, 3, 4],
    'C': ['x', 'y']
}

# DataFrame com a tabela de combinações
dados = {
    'A': [1, 0],
    'B': [2, 3],
    'C': ['x', 'y']
}
tabela = pd.DataFrame(dados)

# Criar o grafo
grafo = criar_grafo(atributos_dominios)
hyper = {}
id = 0
for h in grafo.edges():
    name = 'e'
    name += str(id)
    hyper[name] = h
    id += 1

# hiperarestas = hyper
# # Cria grafo com hypernetx
# H = hnx.Hypergraph(hiperarestas)

# # Plotar o hiper-grafo
# hnx.draw(H, with_node_labels=True)

# plt.show()

# Plotar o grafo
plotar_grafo(grafo)