"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
  return f'{msg}, {nome}!'
  

def executa(funcao, *args):
  return funcao(*args)
  

# saudacao_2 = saudacao
# v = saudacao('Bom dia')
# v = saudacao_2('Bom dia')

print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Maria'))
