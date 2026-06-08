import uvicorn
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from src.api.routers import admin_router
from src.config import setting

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)


app.include_router(router=admin_router)



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)