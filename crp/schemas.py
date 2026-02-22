from ninja import Schema
from typing import Dict

class CryptoDetail(Schema):
    slug: str
    name: str
    price: float
    change_24h: float
    change_1h: float
    change_7d: float
    change_30d: float
    change_90d: float
    change_365d: float
    toman: float
    toman24hchange: float
    updated_at: str

class CryptoResponseSchema(Schema):
    crypto_prices: Dict[str, CryptoDetail]