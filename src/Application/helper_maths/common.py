import numpy as np
import sympy as sp

def get_column(matriz, pos): return matriz[:, pos][pos:,]


def swap_rows(matriz, row1, row2):
  temp_row = np.array(matriz[row1])
  matriz[row1] = np.array(matriz[row2])
  matriz[row2] = temp_row
  return matriz

def zeros_below_diagonal(matriz):
  for i in range(1, len(matriz)):
    for j in range(i):
      print(matriz[i][j])
      if( matriz[i][j] != 0): return False
  return True


def reversal_sustitution(matriz, symbols):
  print(matriz)
  symbols_dic = {}
  for item in symbols:
    symbols_dic[item] = sp.Symbol(item)
  result = []
  added = []

  for i in range(len(symbols)-1, -1, -1):
    added.insert(0, symbols[i])
    for j in range(len(added)):
      incognit = symbols_dic[added[j]]
      if(isinstance(incognit, sp.Symbol) == False):
        continue
      no_zeros = matriz[i][i:len(symbols)][j]
      arr_no_zeros = matriz[i][i:len(symbols)]
      constant = matriz[i][-1]
      eq = 0
      test = []
      for k in range(len(added)):
        num = arr_no_zeros[k]
        current_symbol = symbols_dic[added[k]]
        test.append(str(num) + '*' + str(current_symbol) )
        test.append('+')
        eq += (current_symbol * num)
      test.append(str((constant*-1)))
      test.append(" = 0")
      result = sp.solve(eq + (constant*-1) )
      print("Ecuacion ",test)
      print('resultado ', result[0])
      if len(result) > 0 and isinstance(incognit, sp.Symbol):
        symbols_dic[added[j]] = float(result[0])

  return symbols_dic