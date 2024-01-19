"""
Introdução ao desempacotamento
"""
# nome, *_ = ['Maria', 'Helena', 'Luiz']
# _, nome, *_ = ['Maria', 'Helena', 'Luiz']
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome)
print(nome, resto)
