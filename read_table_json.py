import json
import sys
from mdd_from_table import create_csp_graph, generate_standard_table, print_standard_table, scenario

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
    columns = table_data.get("columns", [])
    rows = table_data.get("rows", [])
    
    # Converte rows para o formato de tabela
    modified_table = extract_rows_as_table(columns, rows)
    
    return domains, modified_table

if __name__ == "__main__":
    # Lê o arquivo JSON 
    with open("D:\Visual Studio 2019\C++\gl_projects\scripts_csp\csp_scripts\csp_scripts\data_example.json", "r") as file:
        input_data = json.load(file)

    # Processa os dados
    domains, modified_table = process_data(input_data)
    scenario = modified_table[1:]

    print(f'domains = {domains}')
    for row in scenario:
        print(row)
    g, c = create_csp_graph(modified_table, domains)
    standard = generate_standard_table(domains, modified_table[1:])
    print_standard_table(standard)
    
    # Retorna a tabela modificada em JSON
    # output_data = {
    #     "modified_table": modified_table
    # }
    
    # # Escreve o resultado no console
    # print(json.dumps(output_data, indent=4))