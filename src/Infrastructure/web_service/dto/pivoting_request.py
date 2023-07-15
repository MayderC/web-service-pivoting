from pydantic import BaseModel
from typing import List

class PivotingRequest(BaseModel):
  unknowns: List[str]
  vector:  List[int]
  matrix: List[List[float]]
  
      
  