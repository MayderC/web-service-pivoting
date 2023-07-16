from pydantic import BaseModel
from typing import List

class PivotingRequest(BaseModel):
  unknowns: List[str]
  vector:  List[List[float]]
  matrix: List[List[float]]
  
  example = {
    "matrix" :[
      [ 0,   -2,  -1], 
      [ 2,   3,  1],
      [ 3,   1,  -1]
    ], 
    "vector": [[-14], [1], [1]], 
    "unknowns": ['x', 'y', 'z']
  }
      
  