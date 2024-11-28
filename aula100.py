# Exercicios:
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},
]

novos_produtos = [
    {**p, 'preço': round(p['preço'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
]

print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_nome)
produtos_ordenados_por_preco.sort(key=lambda item: item['preço'])
print(*produtos_ordenados_por_preco, sep='\n')
