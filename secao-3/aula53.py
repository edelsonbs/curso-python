"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)
# lista_enumerada = list(enumerate(lista))
# lista_enumerada = list(enumerate(lista, start=19))  # enumera a partir do start
# print(lista_enumerada)
# print(next(lista_enumerada))

# # Uma forma de pegar índice e valor
# for item in enumerate(lista):
#   indice, nome = item
#   print(indice, nome)
  
# Forma simplificada do Python de pegar índice e valor
for indice, nome in enumerate(lista):
  print(indice, nome, lista[indice])

# # Uma forma de pegar índice e valor com um for dentro de um for
# for tupla_enumerada in enumerate(lista):
#   print('FOR da tupla')
#   for valor in tupla_enumerada:
#     print(f'\t{valor}')
  