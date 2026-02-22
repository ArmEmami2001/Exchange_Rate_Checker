from ninja_extra import api_controller, route
from typing import Dict
from .schemas import CurrencyDetailSchema

@api_controller('/currency', tags=['Rates'])
class CurrencyController:

    @route.get('/all', response=Dict[str, CurrencyDetailSchema])
    def get_all_currencies(self):
        # In a real scenario, you'd fetch this from api.alanchand.com
        data = {
            "usd": {
                "slug": "usd",
                "name": "دلار آمریکا",
                "sell": 164100.0,
                "buy": 162450.0,
                "dolar_rate": 1.0,
                "open": 164200.0,
                "high": 164600.0,
                "low": 164100.0,
                "dayChange": -0.06,
                "updated_at": "2026-02-22 11:50:07"
            },
            "eur": {
                "slug": "eur",
                "name": "یورو",
                "sell": 193400.0,
                "buy": 191500.0,
                "dolar_rate": 0.8486,
                "open": 193500.0,
                "high": 194000.0,
                "low": 193400.0,
                "dayChange": -0.05,
                "updated_at": "2026-02-22 11:50:07"
            }
        }
        return data