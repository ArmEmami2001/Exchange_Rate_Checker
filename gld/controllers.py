from ninja_extra import api_controller, route
from typing import Dict
from .schemas import GoldDetail

@api_controller('/gold', tags=['Gold & Metals'])
class GoldController:

    @route.get('/prices', response=Dict[str, GoldDetail])
    def get_gold_prices(self):
        # This represents the data you provided
        data = {
            "abshodeh": {
                "slug": "abshodeh",
                "name": "آبشده(مثقال طلا)",
                "price": 85540000,
                "open": 85050000,
                "high": 86130000,
                "low": 85050000,
                "dayChange": 0.58,
                "real_price": 87538270,
                "bubble": -1998270,
                "bubble_per": -2.28,
                "updated_at": "2026-02-22 11:55:07"
            },
            "usd_xau": {
                "slug": "usd_xau",
                "name": "انس طلا",
                "price": 5107.03,
                "open": 5107.36,
                "high": 5107.36,
                "low": 5105.27,
                "dayChange": -0.01,
                "updated_at": "2026-02-22 11:55:07"
            }
            # ... and so on for others
        }
        return data