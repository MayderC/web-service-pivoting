import numpy as np
from .common import zeros_below_diagonal, reversal_sustitution, get_column, swap_rows, is_row_zero
from .log_helper import swap_row_log

PARCIAL = "Parcial pivoting"
PARCIAL_GAUSS = "Parcial pivoting with Gauss"

def parcial(matriz, array_col, unknowns):
  print("================================")
  print("PARCIAL INICIO")
  print("================================")
  only_nums = np.array(matriz).astype(float)

  dic_steps = []
  cont_step = 0

  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)

  print(np_matriz)
  for i in range(len(np_matriz[0])-2):

    curret_column = get_column(np_matriz, i)
    higer = get_max_abs(curret_column)
    index_pivot = [np.where(np_matriz[:, i] == higer)[0][0], higer]
    
    current_step = {}
    matrices = []
    description = ''
    pivot = {}
    
    if not(index_pivot[0] == i):
      print("================================")
      print("PIVOTE ENCONTRADO FILA ", index_pivot[0]+1)
      print("================================")

      matrices.append(np.copy(np_matriz).tolist())
      print("================================")
      print("CAMBIO DE FILA ", i+1 ," POR ", index_pivot[0]+1, "ANTES")
      print("================================")

      print(np_matriz)
      np_matriz = swap_rows(np_matriz, i, index_pivot[0])


      print("================================")
      print("CAMBIO DE FILA ", i+1 ," POR ", index_pivot[0]+1, "DESPUES")
      print("================================")
      print(np_matriz)

      matrices.append(np.copy(np_matriz).tolist())
      pivot['description']= swap_row_log(index_pivot[0], i)
      pivot["sorted_pivot"] = False
      pivot['matrices'] = matrices
      pivot["helping_msg_dev"] = "matrices[0] = before swaping row, matriz[1] = after swaping row"
    
    else:
      print("================================")
      print("PIVOTE ORDENADO")
      print("================================")
      print(np_matriz)

      matrices.append(np.copy(np_matriz).tolist())
      pivot['description']= "Pivote ordenado, la matriz queda igual"
      pivot["sorted_pivot"] = True
      pivot['matrices'] = matrices
      pivot["helping_msg_dev"] = "matrices[0] is the same, because it was not changed"

    try:
      print("================================")
      print("MATRIZ ANTES DE HACER CERO, CON OPERACION ELEMENTAL")
      print("================================")

      zeros = []
      print(np_matriz)
      np_matriz = make_zero2(np_matriz, i, zeros)
      current_step['zero_operations'] = zeros

    except Exception as error:
      raise Exception('Zero  division') 
    print("================================")
    print("MATRIZ DESPUES DE HACER CERO, CON OPERACION ELEMENTAL")
    print("================================")
    print(np_matriz)

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
  return {"solution": result, "steps": {"first_operation": dic_steps, "reversal": rs_arr}}


  for i in range(index+1, len(matriz)):
    elemental_op = (matriz[i][index]*-1)
    for j in range(index, len(matriz[i])):
      if(matriz[i][index] == 0 ):break
      print(matriz[index][j],'x', elemental_op,'x', matriz[i][j], "OPERACION" ) 
      op=(matriz[index][j]*elemental_op) +matriz[i][j]
      print(op, "RESULTADO")
      matriz[i][j] = float(op)
  return matriz

def make_zero(matriz, indexI, zeros):
  print('INDEX', indexI, indexI+1)
  if(matriz[indexI][indexI] == 0):
    raise Exception('Zero  division', str(matriz[index+1][i]) + '/' +str(matriz[index][index])) 
  print("ELEMENTAL", matriz[indexI+1][indexI], '/', matriz[indexI][indexI]) 

  matrix_before = np.copy(matriz).tolist()
 
  for i in range(indexI+1, len(matriz)):
    if(matriz[indexI][indexI] == 0):
      raise Exception('Zero  division', str(matriz[index+1][i]) + '/' +str(matriz[index][index]))
    elemental_operation =   (matriz[i][indexI] / matriz[indexI][indexI])
    elemental_operation_text = str(matriz[i][indexI]) + "/"+ str(matriz[indexI][indexI])


    current_operation = {}
    current_operation["matrices"] =[]
    current_operation["matrices"].append(np.copy(matriz).tolist())
    current_operation['elemental_operation']= []
    current_operation['elemental_operation'].append(str(matriz[i][indexI]) + "/"  + str(matriz[indexI][indexI]))
    current_operation["row"] = i
    current_operation['operations'] = {"operation" : []}
    current_operation["is_zero"]=False


    for j in range(indexI, len(matriz[i])):
      if(j == indexI and matriz[i][j] == 0): 
        print("================================")
        print("CERO ENCONTRADO, SE OMITE LA OPERACION", "POSICION ", i+1, j+1 )
        print("================================")

        current_operation["is_zero"]=True
        current_operation["matrices"] = []

        break
      #current_operation['operations']["position"] = []
      #current_operation['colunm'] = j
      print("================================")
      print("APLICANDO OPERACION", "POSICION ", i+1, j+1 )
      print("================================")
      print(matriz[i][j], " - ",(elemental_operation), " * ",matriz[indexI][j], "CEROO" )
      op = matriz[i][j] - (elemental_operation * matriz[indexI][j])

      print("================================")
      print("RESULTADO EN LA ", "POSICION ", i+1, j+1, ' ', op )
      print("================================")
      current_operation["operations"]['operation'].append(str(matriz[i][j])+" - "+elemental_operation_text+" * "+str(matriz[indexI][j])+" = "+str(op))
      current_operation['helping_msg_dev'] = "The index of each element in the array named 'operation', represents an index of the column of the currently matrix"
      
      matriz[i][j] = op
      print(matriz)
    
    current_operation["matrices"].append(np.copy(matriz).tolist())
    zeros.append(current_operation)

  return matriz

#if the numbers below the main digonal are not zeros then we will return false,
def are_zeros(matriz):
  for i in range(1, len(matriz)):
    for j in range(i):
      if( matriz[i][j] != 0): return False
  return True

def get_max_abs(array):
  output = array[0]
  for i in range(len(array)):
    if(np.abs(output) < np.abs(array[i])):
      output = array[i]
  return output

def make_zero2(matriz, index, zeros):
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
