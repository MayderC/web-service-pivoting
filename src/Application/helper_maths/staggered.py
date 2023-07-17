import numpy as np
from .common import swap_rows, reversal_sustitution, zeros_below_diagonal

def staggered(matriz, array_col, unknowns):
  print("STAGGERED ===================================")
  only_nums = np.array(matriz).astype(float)
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)

  dic_steps = []
  matrices = []
  cont_step = 0
  for i in range(len(np_matriz)-1):
    position = get_position_to_swap(np_matriz, i, i)
    if(position > 0):    
      string = 'Se intercambio la Fila ' + str(position) + ' Por la fila ' + str(i)
      matrices.append(np.copy(np_matriz).tolist())
      np_matriz = swap_rows(np_matriz, i, position)
      matrices.append(np.copy(np_matriz).tolist())
      cont_step +=1
      dic_steps.append({'description': string, 'step_matrices' : matrices, "step": cont_step })
    np_matriz = make_zero(np_matriz, i)

  if(zeros_below_diagonal(np_matriz) == False):
    return {"matrix" :np_matriz.tolist(), "error": "We could'nt convert the numbers below the diagonal to zero, try with other method"}
  
  if(is_row_zero(np_matriz)):
    return {"matrix" :np_matriz.tolist(), "error": "The equation system  has infinite solutions, cause all elements in a row are zero"}
  
  
  result = reversal_sustitution(np_matriz, unknowns)
  return {"solution" : result, "steps": []}

def make_zero(matriz, index):
  for i in range(len(matriz)-1):
    print((matriz[index+1][i], '/', matriz[index][index]), "ELEME")
    elemental_op = matriz[index+1][i] / matriz[index][index]

    string = str(matriz[index+1][i]) + '/' + str(matriz[index][index])
    for j in range(len(matriz[i+1])):
      print(matriz[i+1][j], '-', string, '*', matriz[i][j], "OPERACION" )
      print(matriz[i+1][j]- matriz[i+1][i]/matriz[i][i]*matriz[index][j], "RESULTADO" )
      matriz[i+1][j] = matriz[i+1][j] - ((elemental_op)* matriz[index][j])
    print("=======================")
    print(matriz)

  return matriz

def get_position_to_swap(matriz, row, col):
  operation = 0
  position = 0
  for j in range(row, len(matriz)):
    dividend = matriz[j][col]
    divisor = matriz[j][col]
    op = 0
    for i in range(col,len(matriz[j])-1):
      if(divisor <= matriz[j][i]):
        divisor = matriz[j][i]
        position = j
    
    temp_op = np.abs(dividend/divisor)
    if(temp_op == operation): return -1
    if( temp_op > operation):
      operation = temp_op
  
  return position