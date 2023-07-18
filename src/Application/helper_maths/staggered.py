import numpy as np
from .common import swap_rows, reversal_sustitution, zeros_below_diagonal, is_row_zero

def staggered(matriz, array_col, unknowns):
  print("================================")
  print("STAGGERED INICIO")
  print("================================")
  print(matriz)
  only_nums = np.array(matriz).astype(float)
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)

  dic_steps = []
  matrices = []
  cont_step = 0
  for i in range(len(np_matriz)-1):
    position = get_position_to_swap(np_matriz, i, i)
    print(position, "POSITION")
    if(position > 0):    
      string = 'Se intercambio la Fila ' + str(position) + ' Por la fila ' + str(i)
      matrices.append(np.copy(np_matriz).tolist())
      np_matriz = swap_rows(np_matriz, i, position)
      matrices.append(np.copy(np_matriz).tolist())
      cont_step +=1
      dic_steps.append({'description': string, 'step_matrices' : matrices, "step": cont_step })
    try:
      print(np_matriz)
      np_matriz = make_zero(np_matriz, i)
    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) }

  if(zeros_below_diagonal(np_matriz) == False):
    return {"matrix" :np_matriz.tolist(), "error": "We could'nt convert the numbers below the diagonal to zero, try with other method"}
  
  if(is_row_zero(np_matriz)):
    return {"matrix" :np_matriz.tolist(), "error": "The equation system  has infinite solutions, cause all elements in one row are zero"}
  
  
  result = reversal_sustitution(np_matriz, unknowns)
  return {"solution" : result, "steps": []}

def staggered_gauss(matriz, array_col, unknowns):
  print("================================")
  print("STAGGERED INICIO")
  print("================================")
  print(matriz)
  only_nums = np.array(matriz).astype(float)
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)

  dic_steps = []
  matrices = []
  cont_step = 0
  for i in range(len(np_matriz)-1):
    position = get_position_to_swap(np_matriz, i, i)
    print(position, "POSITION")
    if(position > 0):    
      string = 'Se intercambio la Fila ' + str(position) + ' Por la fila ' + str(i)
      matrices.append(np.copy(np_matriz).tolist())
      np_matriz = swap_rows(np_matriz, i, position)
      matrices.append(np.copy(np_matriz).tolist())
      cont_step +=1
      dic_steps.append({'description': string, 'step_matrices' : matrices, "step": cont_step })
    try:
      print(np_matriz)
      np_matriz = make_zero(np_matriz, i)
    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) }

  if(zeros_below_diagonal(np_matriz) == False):
    return {"matrix" :np_matriz.tolist(), "error": "We could'nt convert the numbers below the diagonal to zero, try with other method"}
  
  if(is_row_zero(np_matriz)):
    return {"matrix" :np_matriz.tolist(), "error": "The equation system  has infinite solutions, cause all elements in one row are zero"}
  
  
  result = reversal_sustitution(np_matriz, unknowns)
  return {"solution" : result, "steps": []}

def make_one(matriz, index):
  print("================================")
  print("MAKE ZERO INICIO")
  print("================================")
  print(matriz)

  elemental_op = 1/matriz[index][index]
  for j in range(index, len(matriz)):
    print(matriz[index][j] * (elemental_op))
    op = (elemental_op * matriz[index][j])
    print("RESULT = ", op)
    matriz[index][j] = float(op)

  print("================================")
  print("MAKE ZERO INICIO")
  print("================================")
  print(matriz)
  return matriz

def make_zero(matriz, index):
  print("================================")
  print("MAKE ZERO INICIO", index)
  print("================================")
  print(matriz)
  for i in range(index, len(matriz)-1):
    elemental_op = matriz[i+1][index] / matriz[index][index]
    print((matriz[i+1][index], '/', matriz[index][index]), "ELEME")
    if(matriz[index][index] == 0):
      raise Exception('Zero  division', str(matriz[index+1][i]) + '/' +str(matriz[index][index])) 

    string = str(matriz[i+1][index]) + '/' + str(matriz[index][index])
    for j in range(index, len(matriz[i])):
      #if(matriz[i+1][j] != 0): break
  
      print(matriz[i+1][j], '-', string, '*', matriz[index][j], "OPERACION" )
      print(matriz[i+1][j] - ((elemental_op)* matriz[index][i]), "RESULTADO" )
      matriz[i+1][j] = (matriz[i+1][j] - (elemental_op) * matriz[index][j])
    print(matriz)
  print("================================")
  print("MAKE ZERO FIN")
  print("================================")
  print(matriz)

  return matriz

def get_position_to_swap(matriz, row, col):
  print("================================")
  print("GET POSITION INICIO")
  print("================================")
  position = 0
  operation = 0
  for j in range(row, len(matriz)):
    dividend = matriz[j][col]
    divisor = matriz[j][col]
    temp_op = 0
    for i in range(col,len(matriz[j])-1):
      if divisor < matriz[j][i]:
        print(divisor, "<", matriz[j][i], "ACTUALIZO")
        divisor = matriz[j][i]
     

    temp_op = np.abs(dividend/divisor)
    print(matriz)
    print(dividend, "/", divisor)
    print(temp_op, '>' ,operation, "=", temp_op > operation)
    if( temp_op > operation):
      print("REMPLAZO")
      print("POSICION IN IF", j)
      operation = temp_op
      position = j
    print("POSICION OUT IF", position)
  print("================================")
  print("GET POSITION FIN")
  print("POSICION FIN", position-1)
  print("================================")
  return position



def get_position_to_swap2(matriz, row, col):


  for i in range(row, len(matriz)):
    arriba = [row][col]
    abajo = [row][col]
    element_op = 0
    pos = 0
    for j in range(col, len(matriz)):
      print(matriz[i][j])
      if(abajo < matriz[i][j]):
        abajo = matriz[i][j]

      temp = np.abs(arriba/abajo)
      if(element_op < temp):
        element_op = temp
        pos = j
    return 0

