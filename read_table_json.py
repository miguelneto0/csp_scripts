import json
import sys
from mdd_from_table import create_csp_graph, generate_standard_table, print_tab, update_collision_table

def extract_rows_as_table(columns, rows):
    # Inicializa a tabela com as colunas
    table = [columns]
    
    # Processa cada linha em rows
    for row in rows:
        processed_row = []
        for cell in row:
            op = cell.get("op")
            values = cell.get("values", [])
            
            if op == "EQ":
                # Se for "EQ", pega o primeiro valor da lista (se existir)
                processed_row.append(values[0] if values else None)
            elif op == "IN":
                # Se for "IN", usa a lista completa
                processed_row.append(values)
            elif op == "ST":
                # Se for "ST", usa "*"
                processed_row.append("*")
            elif op == "GT":
                # Se for "GT", adiciona ">" concatenado com o primeiro valor
                processed_row.append(f">{values[0]}" if values else None)
            elif op == "GE":
                # Se for "GE", adiciona ">=" concatenado com o primeiro valor
                processed_row.append(f">={values[0]}" if values else None)
            elif op == "LE":
                # Se for "LE", adiciona "<=" concatenado com o primeiro valor
                processed_row.append(f"<={values[0]}" if values else None)
            elif op == "LT":
                # Se for "LT", adiciona "<" concatenado com o primeiro valor
                processed_row.append(f"<{values[0]}" if values else None)
            else:
                # Caso op desconhecido, insere um valor padrão (None)
                processed_row.append(None)
        
        # Adiciona a linha processada à tabela
        table.append(processed_row)
    
    return table

def process_data(input_data):
    # Extração dos dados de entrada
    domains = input_data.get("domains", {})
    table_data = input_data.get("table", {})
    out_idx = table_data.get("outputStartIndex")
    columns = table_data.get("columns", [])
    rows = table_data.get("rows", [])
    
    new_rows = []
    for r in rows:
        n_row = []
        for cell in range(len(r)):
            if cell < out_idx:
                n_row.append(r[cell])
        new_rows.append(n_row)
        
    if out_idx > 0:
        columns = columns[:out_idx]
        rows = new_rows

    # Converte rows para o formato de tabela
    modified_table = extract_rows_as_table(columns, rows)

    return domains, modified_table

if __name__ == "__main__":
    input_data = None
    # Lê o arquivo JSON 
    with open("D:\Visual Studio 2019\C++\gl_projects\scripts_csp\csp_scripts\csp_scripts\data_example.json", "r") as file:
        input_data = json.load(file)
    # input_data = json.loads(sys.stdin.read())

    # Processa os dados
    domains, modified_table = process_data(input_data)
    scenario = modified_table

    print(f'domains = {domains}')
    for row in scenario:
        print(row)
    g, c, p, e = create_csp_graph(scenario, domains)
    standard, compres, indx = generate_standard_table(scenario, domains)
    print_tab(standard)
    
    upd_tab, idxs_rmv = update_collision_table(standard, c, True)
    # Retorna a tabela modificada em JSON
    output_data = {
        "modified_table": upd_tab,
        "tuples_to_rmv": idxs_rmv
    }
    
    # # Escreve o resultado no console
    print(json.dumps(output_data, indent=4))