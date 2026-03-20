from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from app.db import init_db
from app.API import points, routes as routes_api
from app.models.route import HealthResponse, ConfigResponse

# Инициализация БД при запуске
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown
    pass

app = FastAPI(
    title="Routing Optimization API",
    description="API для оптимизации городских маршрутов доставки",
    version="1.0.0",
    lifespan=lifespan
)

# CORS для взаимодействия с фронтом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение рутера
app.include_router(points.router, prefix="/api", tags=["Points"])
app.include_router(routes_api.router, prefix="/api", tags=["Routes"])

# служебные эндпоинты, не связаны с основной логикой
@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """Проверка статуса сервера"""
    return {"status": "ok", "message": "Server is running"}

@app.get("/api/config", response_model=ConfigResponse)
async def get_config():
    """Получить конфиг приложения"""
    return {
        "routing_api": "osrm",
        "version": "1.0.0",
        "cors_enabled": True,
        "database": "sqlite"
    }

@app.get("/")
async def root():
    """Корневой путь"""
    return {
        "message": "Routing Optimization API",
        "docs": "/docs",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)