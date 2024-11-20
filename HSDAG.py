class HSDAGNode:
    def __init__(self, conflict_set=None):
        self.conflict_set = conflict_set if conflict_set is not None else set()  # Conjunto de conflito
        self.children = []  # Filhos na árvore HSDAG

def hdag_find_conflicts(diagnoses):
    root = HSDAGNode(conflict_set=set())  # Raiz da árvore HSDAG
    conflict_sets = []  # Armazena os conjuntos mínimos de conflito
    stack = [root]  # Pilha de nós a serem processados

    while stack:
        node = stack.pop()

        # Verificar se o conflito cobre pelo menos uma restrição de cada diagnóstico
        if all(any(restr in node.conflict_set for restr in diag) for diag in diagnoses):
            # Adicionar se for um novo conflito mínimo
            if not any(node.conflict_set.issuperset(cs) for cs in conflict_sets):
                conflict_sets.append(node.conflict_set)
            continue

        # Expandir o nó, adicionando uma nova restrição de cada diagnóstico
        for diag in diagnoses:
            # Adiciona apenas restrições que não estão no conflito atual
            for restr in diag:
                if restr not in node.conflict_set:
                    new_conflict_set = node.conflict_set | {restr}
                    # Evita duplicação de conflito
                    if not any(new_conflict_set.issuperset(cs) for cs in conflict_sets):
                        child = HSDAGNode(conflict_set=new_conflict_set)
                        node.children.append(child)
                        stack.append(child)

    return conflict_sets

# Exemplo de diagnósticos mínimos
diagnoses = [
    {"A", "B", "C"},
    {"A", "D", "B"},
    {"E", "A", "B"},
    {"F", "G", "A", "H", "B"},
    {"F", "G", "A", "I", "B"},
    {"F", "J", "G", "A", "B", "K"}
]

# Cenario toy
diagnoses_toy = [
    {"A", "B"},
    {"B", "a"},
    {"A", "b"},
    {"a", "b"},
    {"x"}
 ]

# Diagnosticos AW10
# diagnoses_aw10 = [
#     {'A': 'OverspeedTimeTransfer'},  E, A, B eh o conflito minimo
#     {'B': 'CLASS_ShaftAW10'},
#     {'C': 'CLASS_EndshAW10'},
#     {'D': 'CLASS_EndshProtLidAct'},
#     {'E': 'INTERFACE_endshANDEndshProtLid'}, 
#     {'F': 'CLASS_EndshBrngSetGlobalAttributesNend'},
#     {'G': 'INTERFACE_statorMainAndEndshNend_StatorAndEndshRestr'},
#     {'H': 'CLASS_BrngAW10SideRestr_ACTIVATION'},
#     {'I': 'INTERFACE_shaftAndBrngDend_ShaftAndBrngAW10Restr'}, --> Aparentemente onde tem ProtLid/FixHolePosDiam
#     {'J': 'CLASS_RollingElementBrngDimensions_ACTIVATION'},
#     {'K': 'CLASS_RollingElementBrngVT'},
# ]

# Executar o HSDAG no exemplo
conflict_sets = hdag_find_conflicts(diagnoses_toy)

# Exibir os conflitos mínimos encontrados
print("Conjuntos mínimos de conflitos encontrados:")
for idx, conflict in enumerate(conflict_sets):
    print(f"Conflito {idx + 1}: {conflict}")
