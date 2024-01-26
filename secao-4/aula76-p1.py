# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

# pessoa = {
#   'nome': 'Luiz Otávio',
#   'sobrenome': 'Miranda',
#   'idade': 900,
# }

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
# print(pessoa.__len__())
# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))


# for chave in pessoa.keys():
#   print(chave)

# for valor in pessoa.values():
#   print(valor)

# for chave, valor in pessoa.items():
#   print(chave, valor)

d1 = {
  'c1': 1,
  'c2': 2,
  'l1': [0 , 1, 2],
}

# d2 = d1
d2 = d1.copy()
# d2 = copy.copy(d1)  # Cópia rasa
# d2 = copy.deepcopy(d1)  # Cópia profunda

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
