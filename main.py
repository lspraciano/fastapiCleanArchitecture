from fastapi import FastAPI

from src.adapters.http.routers.user_change_last_name_router import user_router

app: FastAPI = FastAPI(
    title="User API",
    version="1.0.0"
)

app.include_router(
    router=user_router,
    prefix="/users",
    tags=[
        "Users"
    ]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
