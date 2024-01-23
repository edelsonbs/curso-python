"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma(x, y, z):
  print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3)
# soma(y=2, z=3, x=1)
soma(1, 2, z=5)
