from ..controller.pivoting_controller import PivotingController
from fastapi.routing import APIRouter
from ..dto.pivoting_request import PivotingRequest
from fastapi import HTTPException
from Helper.validation import is_square_matriz

router = APIRouter(prefix="/pivoting")
pivoting_controller = PivotingController()


@router.post("/parcial")
def parcial(data: PivotingRequest):
  try:
    is_square_matriz(data)
    return pivoting_controller.parcial(data)
  except HTTPException as error:
    raise error
  
@router.post("/staggered")
def staggered(data: PivotingRequest):
  try:
    is_square_matriz(data)
    return pivoting_controller.parcial(data)
  except HTTPException as error:
    raise error

@router.post("/total")
def total(data: PivotingRequest):
  try:
    is_square_matriz(data)
    return pivoting_controller.parcial(data)
  except HTTPException as error:
    raise error