"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
# frase = 'Olha só que, coisa interesante'
frase = '   Olha só que   , coisa interesante             '
# lista_palavras = frase.split()
# lista_frases = frase.split(',')
lista_frases_cruas = frase.split(',')

lista_frases = []
# for i, frase in enumerate(lista_frases):
#   # print(lista_frases[i].strip())  # strip() -> remove espaços
#   # print(lista_frases[i].rstrip())  # rstrip() -> remove espaços da direita
#   # print(lista_frases[i].lstrip())  # rstrip() -> remove espaços da esquerda
#   lista_frases[i] = lista_frases[i].strip()

for i, frase in enumerate(lista_frases_cruas):
  lista_frases.append(lista_frases_cruas[i].strip())
  
# print(lista_frases_cruas)
# print(lista_frases)
# frases_unidas = '-'.join('abc')
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
