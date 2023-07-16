import numpy as np
from .common import zeros_below_diagonal, reversal_sustitution, get_column, swap_rows

def parcial(matriz, array_col, unknowns):
  only_nums = np.array(matriz).astype(float)
  dic_steps = []
  cont_step = 0
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)
  for i in range(len(np_matriz[0])-2):
    curret_column = get_column(np_matriz, i)
    higer = get_max_abs(curret_column)

    #optimizar evitar n al cubo
    index_pivot = [np.where(np_matriz[:, i] == higer)[0][0], higer]
    matrices = []

    if not(index_pivot[0] == i):
      #matrices.append(np.copy(np_matriz).tolist())
      print(np_matriz)
      np_matriz = swap_rows(np_matriz, i, index_pivot[0])
      print(np_matriz)
      #matrices.append(np.copy(np_matriz).tolist())
      #cont_step +=1
      #dic_steps.append({'description': update_swap_log(index_pivot[0], i), 'matrices': matrices, "step": cont_step })
    print(np_matriz) 
    np_matriz = make_zero(np_matriz, i, dic_steps)
    print(np_matriz)
    print('----------------------------------------------------------------')
  
  if(zeros_below_diagonal(np_matriz) == False):
    return {"matrix" :np_matriz.tolist(), "Error": "We could'nt convert the numbers below the diagonal to zero"}
  
  
  result = reversal_sustitution(np_matriz, unknowns)
  return {"solution": result, "steps": []}


def get_max_abs(array):
  output = array[0]
  for i in range(len(array)):
    if(np.abs(output) < np.abs(array[i])):
      output = array[i]
  return output


def make_zero(matriz, indexI, dic):
  print('INDEX', indexI, indexI+1)
  elemental_operation =   (matriz[indexI+1][indexI] / matriz[indexI][indexI]) 
  print("ELEMENTAL", matriz[indexI+1][indexI], '/', matriz[indexI][indexI])
 
  for i in range(indexI+1, len(matriz)):
    for j in range(indexI, len(matriz[i])):
      if(matriz[i][j] == 0): break
      print(matriz[i][j], (elemental_operation), matriz[indexI][j], "CEROO" )
      op = matriz[i][j] - (elemental_operation * matriz[indexI][j])
      print("RESULT = ", op)
      matriz[i][j] = op
  return matriz


#if the numbers below the main digonal are not zeros then we will return false,
def are_zeros(matriz):
  for i in range(1, len(matriz)):
    for j in range(i):
      print(matriz[i][j])
      if( matriz[i][j] != 0): return False
  return True

def get_max_abs(array):
  output = array[0]
  for i in range(len(array)):
    if(np.abs(output) < np.abs(array[i])):
      output = array[i]
  return output