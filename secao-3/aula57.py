"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2         3
    ['Luiz', 'João', 'Eduarda', ],  # 2
    # ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2 -> referente ao print da linha 19
]

# print(salas)
# print(salas[1])  # Acessando a lista
# print(salas[1][0])  # Acessando o valor
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
  print(f'A sala é {sala}')
  for aluno in sala:
    print(aluno)
