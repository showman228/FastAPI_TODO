from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .router.users import router as users_router
from .router.tasks import router as tasks_router
from .config import settings


app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(tasks_router)

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {
        "message": "Welcome to TO-DO",
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    return {
        "status": "200_OK"
    }