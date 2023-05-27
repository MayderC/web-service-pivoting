from fastapi import FastAPI
from Infrastructure.web_service.routes.pivoting_route import pivoting_router

app = FastAPI()


app.include_router(pivoting_router)