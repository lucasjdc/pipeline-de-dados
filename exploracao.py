#Lendo os dados da empresa A

path_json = '../data_raw/dados_empresaA.json'

import json

with open(path_json, 'r') as file:
    dados_json = json.load(file)

# Lendo os dados da empresa B
with open(path_csv, 'r') as file:
    print(file.readlines())


import csv

dados_csv = []
with open(path_csv, 'r') as file:
    spamreader = csv.DictReader(file, delimiter=',')
    for row in spamreader:
        dados_csv.append(row)

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja' : 'Filial',
               'Data da Venda' : 'Data da Venda'}
key_mapping

new_dados_csv = []

for old_dict in dados_csv:
    dict_temp = {}
    for old_key, value in old_dict.items():
        dict_temp[key_mapping[old_key]] = value
    new_dados_csv.append(dict_temp)
new_dados_csv[0]


# Unindo a lista das duas empresas
combined_list = []
combined_list.extend(dados_json)
combined_list.extend(new_dados_csv)