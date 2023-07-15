from fastapi import HTTPException, status


def is_square_matriz(data):
  len_of_matriz = len(data.matrix)
  len_of_vector = len(data.vector)
  len_of_unknowns = len(data.unknowns)
  if(len_of_matriz == 0):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty matrix")
  
  if(len_of_vector == 0):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty vector")

  if(len_of_unknowns == 0):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty unknowns")

  for row in data.matrix:
    if(len(row) != len_of_matriz):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Matrix is not square")

  if(len_of_vector != len_of_unknowns):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The length of vector and unknowns are not equal")

  if(len_of_matriz != len_of_unknowns):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The quantity of rows in matrix is not the same with the quantity of elements in unknowns")

  if(len_of_matriz != len_of_vector):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The quantity of rows in matrix is not the same with the quantity of elements in vector")

    
  

  return True