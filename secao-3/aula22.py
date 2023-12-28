# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
#   ...
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
  print('Entar')
else:
  print('Sair')

# Avaliação de curto circuito
# print(True or False or 0 or 'abc' or True) -> Retorna o último valor avaliado como verdadeiro ('abc')
senha = input('Senha: ') or 'Sem senha'
print(senha)