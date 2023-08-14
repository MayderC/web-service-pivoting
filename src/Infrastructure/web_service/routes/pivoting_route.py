from ..controller.pivoting_controller import PivotingController
from fastapi.routing import APIRouter
from ..dto.pivoting_request import PivotingRequest
from fastapi import HTTPException
from ..validations.validation import validations

router = APIRouter(prefix="/pivoting")
pivoting_controller = PivotingController()


@router.post("/parcial")
def parcial(data: PivotingRequest):
  try:
    validations(data)
    return pivoting_controller.parcial(data)
  except HTTPException as error:
    raise error
  
@router.post("/staggered")
def staggered(data: PivotingRequest):
  try:
    validations(data)
    return pivoting_controller.staggered(data)
  except HTTPException as error:
    raise error

@router.post("/total")
def total(data: PivotingRequest):
  try:
    validations(data)
    return pivoting_controller.total(data)
  except HTTPException as error:
    raise error