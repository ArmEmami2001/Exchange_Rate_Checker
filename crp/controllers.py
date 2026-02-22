from ninja_extra import api_controller, route
from typing import Dict
from .schemas import CryptoDetail

@api_controller('/crypto', tags=['Cryptocurrency'])
class CryptoController:

    @route.get('/prices', response=Dict[str, CryptoDetail])
    def get_crypto_prices(self):
        # This is the data structure you provided
        data = {
            "BTC": {
                "slug": "BTC",
                "name": "Bitcoin",
                "price": 67951.96,
                "change_24h": -0.018,
                "change_1h": -0.01413243,
                "change_7d": -3.91715585,
                "change_30d": -23.91918161,
                "change_90d": -21.69237931,
                "change_365d": 0,
                "toman": 11329905485,
                "toman24hchange": 0.9,
                "updated_at": "2026-02-22 11:55:07"
            },
            "SHIB": {
                "slug": "SHIB",
                "name": "shiba ino",
                "price": 0.00000622, # Handled as float
                "change_24h": -4.601,
                "change_1h": -0.25413778,
                # ... other fields
                "toman": 1.0338,
                "toman24hchange": -4.55,
                "updated_at": "2026-02-22 11:55:07"
            }
        }
        return data