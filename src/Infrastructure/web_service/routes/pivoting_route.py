from fastapi.routing import APIRouter
from ..controller.parcial_pivoting import ParcialController

pivoting_router = APIRouter(prefix="/api")
parcial_controller = ParcialController()

@pivoting_router.get("/parcial")
def parcial():
  return parcial_controller.parcial("Hello")
  
