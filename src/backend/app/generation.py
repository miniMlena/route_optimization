import numpy as np
from typing import List, Dict
from app.db import add_point, clear_points, get_all_points

def generate_points(center_lat: float, center_lon: float, radius_km: float, count: int) -> List[Dict]:
    """
    Генерирует случайные точки в пределах заданного радиуса от центра.
    
    Использует полярные координаты для равномерного распределения точек внутри круга.
    Сохраняет точки в базу данных и возвращает их список.
    """
    lat_deg_per_km = 1 / 111.0
    lon_deg_per_km = 1 / (111.0 * np.cos(np.radians(center_lat)))
    
    angles = np.random.uniform(0, 2 * np.pi, count)
    
    distances = np.sqrt(np.random.uniform(0, 1, count)) * radius_km
    
    delta_lat_km = distances * np.cos(angles)
    delta_lon_km = distances * np.sin(angles)
    
    delta_lat_deg = delta_lat_km * lat_deg_per_km
    delta_lon_deg = delta_lon_km * lon_deg_per_km
    
    lats = center_lat + delta_lat_deg
    lons = center_lon + delta_lon_deg
    
    points = []
    for lat, lon in zip(lats, lons):
        point_id = add_point(lat, lon)
        points.append({
            "id": point_id,
            "lat": float(lat),
            "lon": float(lon)
        })
    
    return points

def get_points() -> List[Dict]:
    """Получить все текущие точки из БД"""
    return get_all_points()

def clear_all_points() -> int:
    """
    Очистить все точки из БД и вернуть количество удаленных.
    """
    current_points = get_all_points()
    count = len(current_points)

    clear_points()
    return count
