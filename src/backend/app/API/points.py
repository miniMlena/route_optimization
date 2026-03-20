from fastapi import APIRouter, HTTPException
from app.models.point import PointGenerationRequest, PointsResponse, ClearResponse
from app.generation import generate_points, get_points
from app.db import clear_points

router = APIRouter()

@router.post("/points/generate", response_model=PointsResponse)
async def generate_points_endpoint(request: PointGenerationRequest):
    """
    Генерирует случайные точки в круге вокруг центра
    
    Пример запроса:
    {
        "center_lat": 55.7558,
        "center_lon": 37.6173,
        "radius": 5.0,
        "count": 10
    }
    """
    try:
        points = generate_points(
            center_lat=request.center_lat,
            center_lon=request.center_lon,
            radius_km=request.radius,
            count=request.count
        )
        return {
            "points": points,
            "total": len(points)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/points", response_model=PointsResponse)
async def get_points_endpoint():
    """Получить все текущие сгенерированные точки"""
    try:
        points = get_points()
        return {
            "points": points,
            "total": len(points)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/points", response_model=ClearResponse)
async def clear_points_endpoint():
    """Очистить все точки"""
    try:
        clear_points()
        return {
            "status": "cleared",
            "message": "Все точки успешно удалены"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))