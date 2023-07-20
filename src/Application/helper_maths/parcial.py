import numpy as np
from .common import zeros_below_diagonal, reversal_sustitution, get_column, swap_rows, is_row_zero


PARCIAL = "Parcial pivoting"
PARCIAL_GAUSS = "Parcial pivoting with Gauss"

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
    #np_matriz = make_one(np_matriz, i)

    try:
      print(np_matriz)
      np_matriz = make_zero(np_matriz, i)
    except Exception as error:
      raise Exception('Zero  division') 
      
    print(np_matriz)
    print('----------------------------------------------------------------')
  
  if(zeros_below_diagonal(np_matriz) == False):
     raise Exception('Faild') 
  
  if(is_row_zero(np_matriz)):
    raise Exception('Faild') 
    #return {"matrix" :np_matriz.tolist(), "error": "The equation system  has infinite solutions, cause all elements in a row are zero"}
  
  result = reversal_sustitution(np_matriz, unknowns)
  return {"solution": result, "steps": [], "type": PARCIAL}

def gauss_parcial(matriz, array_col, unknowns):
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
    #np_matriz = make_one(np_matriz, i)

    try:
      print(np_matriz)
      np_matriz = make_one(np_matriz, i)
      np_matriz = make_zero_gauss(np_matriz, i)
    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) }
      
    print(np_matriz)
    print('----------------------------------------------------------------')
  
  if(zeros_below_diagonal(np_matriz) == False):
    return {"matrix" :np_matriz.tolist(), "error": "We could'nt convert the numbers below the diagonal to zero, try with other method"}
  
  if(is_row_zero(np_matriz)):
    return {"matrix" :np_matriz.tolist(), "error": "The equation system  has infinite solutions, cause all elements in a row are zero"}
  
  result = reversal_sustitution(np_matriz, unknowns)
  return {"solution": result, "steps": [], "type": PARCIAL_GAUSS}

def make_one(matriz, index):
  if(matriz[index][index] == 0):
    raise Exception('Zero  division', str(1) + '/' +str(matriz[index][index])) 
  elemental_op = 1/matriz[index][index]
  for j in range(index, len(matriz)):
    print(matriz[index][j] * (elemental_op))
    op = (elemental_op * matriz[index][j])
    print("RESULT = ", op)
    matriz[index][j] = float(op)
  return matriz

def make_zero_gauss(matriz, index):
  for i in range(index+1, len(matriz)):
    elemental_op = (matriz[i][index]*-1)
    for j in range(index, len(matriz[i])):
      if(matriz[i][index] == 0 ):break
      print(matriz[index][j],'x', elemental_op,'x', matriz[i][j], "OPERACION" ) 
      op=(matriz[index][j]*elemental_op) +matriz[i][j]
      print(op, "RESULTADO")
      matriz[i][j] = float(op)
  return matriz

def make_zero(matriz, indexI):
  print('INDEX', indexI, indexI+1)
  if(matriz[indexI][indexI] == 0):
    raise Exception('Zero  division', str(matriz[index+1][i]) + '/' +str(matriz[index][index])) 
  elemental_operation =   (matriz[indexI+1][indexI] / matriz[indexI][indexI])
  print("ELEMENTAL", matriz[indexI+1][indexI], '/', matriz[indexI][indexI]) 
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

