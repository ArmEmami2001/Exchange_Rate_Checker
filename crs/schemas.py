from ninja import Schema
from typing import Dict

class CurrencyDetailSchema(Schema):
    slug: str
    name: str
    sell: float
    buy: float
    dolar_rate: float
    open: float
    high: float
    low: float
    dayChange: float
    updated_at: str

# This represents the entire JSON object (a dictionary of currencies)
class CurrencyResponseSchema(Schema):
    currencies: Dict[str, CurrencyDetailSchema]