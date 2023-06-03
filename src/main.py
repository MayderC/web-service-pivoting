from fastapi import FastAPI
from Infrastructure.web_service.routes.pivoting_route import router



app = FastAPI(title='Métodos numéricos Api', description='Grupo 6: Técnicas de pivoteo')
app.include_router(router, prefix='/api')