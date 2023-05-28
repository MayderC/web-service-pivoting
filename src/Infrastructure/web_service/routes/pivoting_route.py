from ..controller.pivoting_controller import PivotingController
from fastapi.routing import APIRouter
from typing import List



router = APIRouter(prefix="/pivoting")
pivoting_controller = PivotingController()


@router.post("/parcial")
def parcial(matriz: List[List[float]]):
  return pivoting_controller.parcial(matriz)
  
@router.post("/staggered")
def staggered(matriz: List[List[float]]):
  return pivoting_controller.staggered(matriz)

@router.post("/total")
def total(matriz: List[List[float]]):
  return pivoting_controller.total(matriz)