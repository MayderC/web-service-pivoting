import numpy as np
from .common import swap_rows, reversal_sustitution, zeros_below_diagonal, is_row_zero
from .log_helper import swap_row_log, current_pivot_log



def staggered(matriz, array_col, unknowns):
  print("================================")
  print("STAGGERED INICIO")
  print("================================")
  print(matriz)
  only_nums = np.array(matriz).astype(float)
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)

  dic_steps = []
  cont_step = 0


  for i in range(len(np_matriz)-1):
    position = get_position_to_swap(np_matriz, i, i)

    current_step = {}
    matrices = []
    description = ''
    pivot = {}

    if(position > 0):    
      string = 'Se intercambio la Fila ' + str(position) + ' Por la fila ' + str(i)
      matrices.append(np.copy(np_matriz).tolist())
      np_matriz = swap_rows(np_matriz, i, position)
      matrices.append(np.copy(np_matriz).tolist())

      pivot['pivot_row'] = current_pivot_log(position)
      pivot['pivot_value'] = np_matriz[position][i]
      pivot['description']= swap_row_log(position, i)
      pivot["sorted_pivot"] = False
      pivot['matrices'] = matrices
      pivot["helping_msg_dev"] = "matrices[0] = before swaping row, matriz[1] = after swaping row"
    else:
      matrices.append(np.copy(np_matriz).tolist())
      pivot['pivot_row'] = current_pivot_log(i)
      pivot['pivot_value'] = np_matriz[i][i]
      pivot['description']= "Pivote ordenado, la matriz queda igual"
      pivot["sorted_pivot"] = True
      pivot['matrices'] = matrices
      pivot["helping_msg_dev"] = "matrices[0] is the same, because it was not changed"

    try:
      print(np_matriz)
      zeros = []
      np_matriz = make_zero(np_matriz, i, zeros)
      current_step['zero_operations'] = zeros

    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) }

    cont_step = cont_step + 1
    pivot['step'] = cont_step
    current_step['pivot_swap'] = pivot
    dic_steps.append(current_step)

  if(zeros_below_diagonal(np_matriz) == False):
    return {"steps": {"first_operation": dic_steps}, "error": "No se puede seguir con sustitución hacia atrás, debido a que al menos un elemento bajo la diagonal no se pudo convertir a cero."}
  
  if(is_row_zero(np_matriz)):
    return {"steps": {"first_operation": dic_steps}, "error": "El sistema de ecuaciones tiene infinitas soluciones, todos los valores en una fila son ceros."}
  
  rs_arr = [] 
  result = reversal_sustitution(np_matriz, unknowns, rs_arr)
  return {"solution" : result, "steps": {"first_operation": dic_steps, "reversal": rs_arr}}
  

def make_zero(matriz, index, zeros):
  print("================================")
  print("MAKE ZERO INICIO", index)
  print("================================")
  print(matriz)
  if(matriz[index][index] == 0):
    raise Exception('Zero  division',"Numero" + '/' +str(matriz[index][index])) 



  for i in range(index, len(matriz)-1):
    elemental_op = matriz[i+1][index] / matriz[index][index]
    elemental_operation_text = str(matriz[i+1][index]) + "/"+ str(matriz[index][index])

    if(matriz[index][index] == 0):
      raise Exception('Zero  division', str(matriz[index+1][i]) + '/' +str(matriz[index][index])) 


    current_operation = {}
    current_operation["matrices"] =[]
    current_operation["matrices"].append(np.copy(matriz).tolist())
    current_operation['elemental_operation']= []
    current_operation['elemental_operation'].append(elemental_operation_text)
    current_operation["row"] = i+1
    current_operation['operations'] = {"operation" : []}
    current_operation["is_zero"]=False


    for j in range(index, len(matriz[i])):
      op = (matriz[i+1][j] - (elemental_op) * matriz[index][j])

      current_operation["operations"]['operation'].append(str(matriz[i][j])+" - "+elemental_operation_text+" * "+str(matriz[index][j])+" = "+str(op))
      current_operation['helping_msg_dev'] = "The index of each element in the array named 'operation', represents an index of the column of the currently matrix"
      

      matriz[i+1][j] = op
    print(matriz)
    current_operation["matrices"].append(np.copy(matriz).tolist())
    zeros.append(current_operation)
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
      operation = temp_op
      position = j
  print("================================")
  print("POSICION FIN", position-1)
  print("================================")
  return position