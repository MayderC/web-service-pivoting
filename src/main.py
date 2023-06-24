from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Infrastructure.web_service.routes.pivoting_route import router


app = FastAPI(title='Métodos numéricos Api', description='Grupo 6: Técnicas de pivoteo')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["POST"],
)

app.include_router(router, prefix='/api')