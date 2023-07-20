import numpy as np
from .common import get_column, swap_rows
import sympy as sp


def total(matriz, array_col, unknowns):

  only_nums = np.array(matriz).astype(float)
  np_matriz = np.concatenate((only_nums, np.array(array_col)), axis=1)  
  unknowns_mutable = np.copy(unknowns)
  dic_steps = []
  
  for i in range(len(np_matriz)):
    #row 0, colum 1
    value = find_highest_number(np_matriz, i)
    print(np_matriz)
    swap_rows(np_matriz, i, value[0])
    swap_columns_matriz(np_matriz, i, value[1])
    swap_columns_vector(unknowns_mutable, i, value[1])
    print('++++++++++++++++++++++++')
    print(np_matriz)
    print(unknowns)
    try:
      make_one(np_matriz, i)
    except Exception as error:
      return {"matrix": np_matriz.tolist(), "error": str(error) } 
    print(np_matriz)
    make_zero(np_matriz, i)
    print(np_matriz)
    print(unknowns, unknowns_mutable)

  result = get_organized_solutions(unknowns_mutable, unknowns, np.copy(np_matriz[:, len(matriz[0])]))
  return {"solution": result, "steps": []}


def make_zero(matriz, index):
  for i in range(len(matriz)):
    if(i == index): continue
    elemntal_op1 = (matriz[i][index]*-1)
    print(matriz[i][index], 'NUMEROO')
    for j in range(index, len(matriz[i])):
      op = ((matriz[index][j]*elemntal_op1)+matriz[i][j])
      matriz[i][j] = op
    print('000000000000000000000000')

def make_one(matriz, index):
  elemntal_op1 = 1/matriz[index][index]
  if(matriz[index][index] == 0):
    raise Exception('Zero  division', str(1) + '/' +str(matriz[index][index]))  
  for i in range(index, len(matriz[index])):
    op = (matriz[index][i]*elemntal_op1)
    matriz[index][i] = op
  print("1111111111111111111111111111")

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
