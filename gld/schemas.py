from ninja import Schema
from typing import Dict

class GoldDetail(Schema):
    slug: str
    name: str
    price: float
    open: float
    high: float
    low: float
    dayChange: float
    # Optional fields because some items (like XAU/XAG) might not have bubbles
    real_price: float = None 
    bubble: float = None
    bubble_per: float = None
    updated_at: str

class GoldResponseSchema(Schema):
    gold_prices: Dict[str, GoldDetail]