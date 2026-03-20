from typing import List, Tuple, Dict
from app.db import add_route, get_all_points, get_route

def build_base_route(point_ids: List[int]) -> Dict:
    pass
    
    '''return {
        "id": route_id,
        "points": point_ids,
        "distance_km": round(total_distance, 2),
        "duration_minutes": round(duration_minutes, 2),
        "coordinates": coordinates
    }'''

def optimize_route(point_ids: List[int]) -> Dict:
    pass
    #вызывает алгоритмы оптимизации