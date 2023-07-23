from fastapi import HTTPException, status


def is_square_matriz(data):
  len_of_matriz = len(data.matrix)
  len_of_vector = len(data.vector)
  len_of_unknowns = len(data.unknowns)
  if(len_of_matriz == 1):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must provide more than one element, matrix")
  
  if(len_of_vector == 1):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must provide more than one element, vector")

  if(len_of_unknowns == 1):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must provide more than one element, unknowns")

  for row in data.matrix:
    if(len(row) != len_of_matriz):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Matrix is not square")

  if(len_of_matriz > 15):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The length of matrix is too large")

  for i in range(len_of_matriz):
    if all(element == 0 for element in data.matrix[i]):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Make sure there's at least one value in row "+str(i+1))
  ''' 
  for i in range(len_of_vector):
    temp_len = data.vector[i]
    if(temp_len != 1):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Foreach element in vector you need to provide an array with one element exactly")
  '''
  if(len_of_vector != len_of_unknowns):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The length of vector and unknowns are not equal")

  if(len_of_matriz != len_of_unknowns):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The quantity of rows in matrix is not the same with the quantity of elements in unknowns")

  if(len_of_matriz != len_of_vector):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The quantity of rows in matrix is not the same with the quantity of elements in vector")

    
  

  return True