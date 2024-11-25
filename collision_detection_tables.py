from itertools import product

class SmartTable:
    def __init__(self, domains):
        self.domains = domains
        self.table = []

    def expand_cell(self, value, domain):
        if value == "*":
            return domain
        if isinstance(value, str):
            if value.startswith(">"):
                return [x for x in domain if x > int(value[1:])]
            elif value.startswith("<"):
                return [x for x in domain if x < int(value[1:])]
            elif value.startswith(">="):
                return [x for x in domain if x >= int(value[2:])]
            elif value.startswith("<="):
                return [x for x in domain if x <= int(value[2:])]
            elif value.startswith("!="):
                try:
                    return [x for x in domain if x != int(value[2:])]
                except ValueError:
                    # Se não for possível converter, ignora o filtro e mantém o domínio original
                    return domain
        return [value]

    def detect_conflict(self, row1, row2):
        for col, (val1, val2) in enumerate(zip(row1, row2)):
            domain = list(self.domains.values())[col]
            expanded1 = self.expand_cell(val1, domain)
            expanded2 = self.expand_cell(val2, domain)
            if not set(expanded1).intersection(set(expanded2)):
                return False
        return True

    def resolve_conflict(self, smart_row, conflicting_row):
        conflicted_val_list = []
        for col, (smart_val, conflict_val) in enumerate(zip(smart_row, conflicting_row)):
            domain = list(self.domains.values())[col]
            expanded_smart = self.expand_cell(smart_val, domain)
            expanded_conflict = self.expand_cell(conflict_val, domain)
            if isinstance(conflict_val,int):
                conflicted_val_list.append(conflict_val)
            print(conflicted_val_list)

            print(f'tupla atualizada = {conflicting_row} pelo valor = {smart_val} com {conflict_val}')
            if set(expanded_smart).intersection(set(expanded_conflict)):
                if smart_val == "*":
                    # Caso 1: Conflito entre "*" e um valor específico
                    for c in conflicted_val_list:
                        smart_row[col] = f"!={c}"
                elif isinstance(smart_val, str) and any(op in smart_val for op in [">", "<", ">=", "<="]):
                    if conflict_val == "*":
                        # Caso 2: Conflito entre operadores smart (>, <, >=, <=) e "*"
                        if smart_val.startswith(">"):
                            threshold = int(smart_val[1:])
                            conflicting_row[col] = f"<={threshold}"
                        elif smart_val.startswith(">="):
                            threshold = int(smart_val[2:])
                            conflicting_row[col] = f"<{threshold}"
                        elif smart_val.startswith("<"):
                            threshold = int(smart_val[1:])
                            conflicting_row[col] = f">={threshold}"
                        elif smart_val.startswith("<="):
                            threshold = int(smart_val[2:])
                            conflicting_row[col] = f">{threshold}"
                    else:
                        # Caso 3: Conflito entre operadores smart (>, <, >=, <=) e valor específico
                        if "!=" not in smart_val:
                            smart_row[col] = f"{smart_val},!={conflict_val}"
                        else:
                            exclusions = smart_val.split(",")
                            smart_row[col] = ",".join(exclusions + [f"!={conflict_val}"])
                            
    def add_row(self, row):
        for existing_row in self.table:
            if self.detect_conflict(existing_row, row):
                print(f"Conflito detectado: {row} com {existing_row}")
                if any(isinstance(cell, str) and any(op in cell for op in [">", "<", "<=", ">=", "*", "!="]) for cell in existing_row):
                    self.resolve_conflict(existing_row, row)
                else:
                    self.resolve_conflict(row, existing_row)
        self.table.append(row)

    def add_rows(self, rows):
        for row in rows:
            self.add_row(row)

        # Verificar e resolver conflitos até que a tabela esteja consistente
        conflicts_resolved = False
        while not conflicts_resolved:
            conflicts_resolved = True  # Assume que todos os conflitos foram resolvidos
            for i, smart_row in enumerate(self.table):
                for j, conflicting_row in enumerate(self.table):
                    if i != j:  # Não comparar a mesma linha
                        for col, (smart_val, conflict_val) in enumerate(zip(smart_row, conflicting_row)):
                            domain = list(self.domains.values())[col]
                            expanded_smart = self.expand_cell(smart_val, domain)
                            expanded_conflict = self.expand_cell(conflict_val, domain)

                            if set(expanded_smart).intersection(set(expanded_conflict)):
                                self.resolve_conflict(smart_row, conflicting_row)
                                conflicts_resolved = False  # Há conflitos, repetir a verificação
                                break
    
    def add_rows(self, rows):
        for row in rows:
            self.add_row(row)

    def show_table(self):
        for row in self.table:
            print(row)

table = [
    [1, ">2", 1],
    [2, 2, 2],   
    [1, "*", 1]]

table1 = [
    [1, 1, 1],
    [2, 2, 2],   
    [1, 1, "*"]]

table2 = [
    [1, ">2", 1],
    [2, 2, 2],   
    [1, 3, 1]]

table3 = [
    [1, 1, "*"],
    [2, 2, 2],   
    [1, "*", 1]]

table4 = [
    [1, 1, "*"],
    [2, 2, 2],   
    [1, 1, 1], 
    [2, "*", 2]]

table5 = [
    [1, "*", 1],
    [1, 1, "*"]
    ]

table6 = [
    [1, "*", 1],
    [1, "*", "*"],
    [1, 1, "*"]]

table7 = [
    [1, 1, "*"],
    [1, "*", 1],
    [1, "*", "*"]]

if __name__ == "__main__":
    # Definição do domínio
    domains = {"A": [1, 2, 3], "B": [1, 2, 3, 4], "C": [1, 2, 3, 4, 5, 6, 7, 8]}

    # Inicializa a tabela smart
    smart_table = SmartTable(domains)
    
    scenario = table7
    print("\nTabela original:")
    for row in scenario:
            print(row)

    # Adiciona linhas à tabela
    smart_table.add_rows(scenario)

    print("\nTabela final:")
    smart_table.show_table()
