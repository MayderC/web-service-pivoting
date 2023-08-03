from fastapi import HTTPException, status


def validations(data):
  len_of_matriz = len(data.matrix)
  len_of_vector = len(data.vector)
  len_of_unknowns = len(data.unknowns)
  if(len_of_matriz == 1):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Debe ingresar más de un elemento en la matriz")
  
  if(len_of_vector == 1):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Debe ingresar más de un elemento en el vector")

  if(len_of_unknowns == 1):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Debe ingresar más de un elemento en las incógnitas")

  for row in data.matrix:
    if(len(row) != len_of_matriz):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La matriz no es cuadrada")

  if(len_of_matriz > 15):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La matrtiz tiene un máximo de 15x15")

  for i in range(len_of_matriz):
    if all(element == 0 for element in data.matrix[i]):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Asegúrese de que haya un valor en la fila "+str(i+1))

  if(len_of_vector != len_of_unknowns):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La longuitud del vector y incognitas deben ser iguales")

  if(len_of_matriz != len_of_unknowns):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La cantidad de filas en la matriz no es igual a la cantidad de elementos en incognitas")

  if(len_of_matriz != len_of_vector):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La cantidad de filas en la matriz no es igual a la cantidad de elementos en incognitas")

    
  

  return True