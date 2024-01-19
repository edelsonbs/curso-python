"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = []

while True:
  print('Selecione uma opção: ')
  opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

  if opcao == 'i':
    # os.system('cls')  # Comando para limpar a tela no Windows
    os.system('clear')  # Comando para limpar a tela no Unix/Linux
    valor = input('Valor: ')
    lista.append(valor)
  elif opcao == 'a':
    indice_str = input('Escolha o índice para apagar: ')

    try:
      indice = int(indice_str)
      del lista[indice]
    except ValueError:
      print('Por favor digite um número inteiro.')
    except IndexError:
      print('Índice não existe na lista.')
    except Exception:
      print('Erro desconhecido.')
  elif opcao == 'l':
    os.system('clear')

    if len(lista) == 0:
      print('Não há nada para listar')

    for i, valor in enumerate(lista):
      print(i, valor)
  elif opcao == 's':
    break
  else:
    print('Por favor escolha i, a ou l')
