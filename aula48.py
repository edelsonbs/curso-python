"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create   Read   Update      Delete
Criar    Ler    Alterar     Apagar = lista[i] (CRUD)
"""
#        +12345
#        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#         0    1         2          3   4
#        -5   -4        -3         -2   -1
# lista = [123, True, 'Luiz Otávio', 1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

#        0   1   2   3   4   5
# lista = [10, 20, 30, 40, 50, 60]
# numero = lista[2]
# print(numero)
# lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(70)
# lista.pop()
# lista.append(80)
# lista.append(90)
# # ultimo_valor = lista.pop()
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido', ultimo_valor)

# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# # lista.insert(0, 'Luiz')
# lista.insert(0, 5)
# print(lista)

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_c)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
