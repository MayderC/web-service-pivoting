import numpy as np
from .common import get_column, swap_rows
import sympy as sp
from .log_helper import swap_row_log, swap_col_log, current_pivot_log


def total(matriz, array_col, unknowns):

  print("================================")
  print("GET POSITION INICIO")
  print("================================")

  only_nums = np.array(matriz).astype(float)
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)  
  unknowns_mutable = np.copy(unknowns)
  
  dic_steps = []
  cont_step = 0
  
  for i in range(len(np_matriz)):
    #row 0, colum 1
    value = find_highest_number(np_matriz, i)

    current_step = {}
    matrices = []
    vectores = []

    description = ''
    pivot = {}
    pivot["matrices"] = []
    pivot["unknowns"] = []
    pivot["one_operation"] = {
      "operations" : [],
      "matrices": []
    }
    pivot["zero_operation"] = {
      "operations" : [],
      "matrices": []
    }

    #row 
    if value[1] == i and value[0] != i:
      matrices.append(np.copy(np_matriz).tolist())
      vectores.append(np.copy(unknowns_mutable).tolist())
      pivot["sorted_pivot"] = False
      pivot['pivot_value'] = np_matriz[value[0]][value[1]]
      pivot['pivot_positions'] = {"row": value[0], "column": value[1]}
      pivot['description_row'] = swap_row_log(i, value[0])
      pivot['description_col'] = "No hay cambio de columnas"
      pivot['description_unk'] = "No hay cambio de posicion en las incognitas"

      swap_rows(np_matriz, i, value[0])
      matrices.append(np.copy(np_matriz).tolist())

    elif value[0] == i and value[1] != i:
      #column
      matrices.append(np.copy(np_matriz).tolist())
      vectores.append(np.copy(unknowns_mutable).tolist())
      pivot["sorted_pivot"] = False
      pivot['pivot_value'] = np_matriz[value[0]][value[1]]
      pivot['pivot_positions'] = {"row": value[0], "column": value[1]}
      pivot['description_row'] = "No hay cambio de filas"
      pivot['description_col'] = swap_col_log(i, value[1])
      pivot['description_unk'] = swap_col_log(i, value[1]) + " del vector de incognitas"

      swap_columns_matriz(np_matriz, i, value[1])
      swap_columns_vector(unknowns_mutable, i, value[1])

      matrices.append(np.copy(np_matriz).tolist())
      vectores.append(np.copy(unknowns_mutable).tolist())
    elif value[0] != i and value[1] !=i: 
      #row and column
      pivot["sorted_pivot"] = False
      pivot['pivot_value'] = np_matriz[value[0]][value[1]]
      pivot['pivot_positions'] = {"row": value[0], "column": value[1]}
      pivot['description_row'] = swap_row_log(i, value[0])
      pivot['description_col'] = swap_col_log(i, value[1])
      pivot['description_unk'] = swap_col_log(i, value[1]) + " del vector de incognitas"

      matrices.append(np.copy(np_matriz).tolist())
      vectores.append(np.copy(unknowns_mutable).tolist())

      swap_rows(np_matriz, i, value[0])
      swap_columns_matriz(np_matriz, i, value[1])
      swap_columns_vector(unknowns_mutable, i, value[1])

      matrices.append(np.copy(np_matriz).tolist())
      vectores.append(np.copy(unknowns_mutable).tolist())
    else: 

      pivot["sorted_pivot"] = True
      pivot['pivot_value'] = np_matriz[value[0]][value[1]]
      pivot['pivot_positions'] = {"row": value[0], "column": value[1]}
      pivot['description_row'] = "No hay cambio de filas"
      pivot['description_col'] = "No hay cambio de columnas"
      pivot['description_unk'] = "No hay cambio de posición en las incógnitas"

      matrices.append(np.copy(np_matriz).tolist())
      vectores.append(np.copy(unknowns_mutable).tolist())

    try:
      make_one(np_matriz, i, pivot["one_operation"])
    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) } 

    try:
      make_zero(np_matriz, i, pivot["zero_operation"])
    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) } 

    pivot["matrices"] = matrices
    pivot["unknowns"] = vectores
    dic_steps.append(pivot)


  result = get_organized_solutions(unknowns_mutable, unknowns, np.copy(np_matriz[:, len(matriz[0])]))
  return {"solution": result, "steps": {"first_operation":dic_steps, "sort_unknowns": []}}


def make_zero(matriz, index, obj):

  obj["matrices"].append(np.copy(matriz).tolist())

  for i in range(len(matriz)):
    if(i == index): continue
    elemntal_op1 = (matriz[i][index]*-1)
    elemental_op_text = str(matriz[i][index])+" * "+"-1"
    for j in range(index, len(matriz[i])):
      op = ((matriz[index][j]*elemntal_op1)+matriz[i][j])
      matriz[i][j] = op
      temp_operation = str(matriz[index][j])+ " * "+ elemental_op_text+ " + "+str(matriz[i][j])
      obj["operations"].append({"operation": temp_operation, "row": index, "col": i, "result": op})
  
  obj["matrices"].append(np.copy(matriz).tolist())


def make_one(matriz, index, obj):
  elemntal_op1 = 1/matriz[index][index]
  elemental_op_text = str(1) +" / "+str(matriz[index][index])
  if(matriz[index][index] == 0):
    raise Exception('Zero  division', str(1) + '/' +str(matriz[index][index]))  

  obj["matrices"].append(np.copy(matriz).tolist())

  for i in range(index, len(matriz[index])):
    op = (matriz[index][i]*elemntal_op1)
    matriz[index][i] = op
    temp_operation = str(matriz[index][i])+ " * "+ elemental_op_text
    obj["operations"].append({"operation": temp_operation, "row": index, "col": i, "result": op})
  
  obj["matrices"].append(np.copy(matriz).tolist())




def find_highest_number(matriz, pos):
  high = np.abs(matriz[pos][pos])
  positions = [pos, pos]
  for i in range(pos, len(matriz)-1):
    for j in range(pos, len(matriz[i])-1):
      if(np.abs(high) < np.abs(matriz[i][j])): 
        high = matriz[i][j]
        positions[0] = i
        positions[1] = j
  return positions

def get_organized_solutions(muatated, original, vector):
  temp_arr = []
  temp_dic = {}
  final_dic = {}

  for i in range(len(original)):
    temp_dic[original[i]]=vector[i]

  for i in range(len(original)):
    temp_arr.append([original[i], muatated[i]])

  for i in range(len(temp_arr)):
    final_dic[temp_arr[i][1]]=temp_dic[temp_arr[i][0]]

  return final_dic

def swap_columns_matriz(matriz, col1, col2):
  for row in matriz:
    temp = row[col1]
    row[col1] = row[col2]
    row[col2] = temp

def swap_columns_vector(vector, pos1, pos2):
  temp = vector[pos1]
  vector[pos1] = vector[pos2]
  vector[pos2] = temp
