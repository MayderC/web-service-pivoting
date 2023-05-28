from fastapi import FastAPI
from Infrastructure.web_service.routes.pivoting_route import router



app = FastAPI()
app.include_router(router, prefix='/api')