from pydantic import BaseModel
from typing import Dict, List

class ItemDetail(BaseModel):
    volume: float
    weight: float
    fragile: int

class BoxDetail(BaseModel):
    volume_cap: float
    weight_cap: float
    base_cost: float
    box_count: int

class PackingRequest(BaseModel):
    items: Dict[str, ItemDetail]
    box_types: Dict[str, BoxDetail]