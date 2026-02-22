from ninja_extra import api_controller, route
from .schemas import GoldResponseSchema
import httpx
from django.conf import settings

@api_controller('/gold', tags=['Gold & Metals'])
class GoldController:

    @route.get('/prices', response=GoldResponseSchema)
    def get_gold_prices(self):
        response = httpx.get(settings.GOLD_API_URL)
        response.raise_for_status()
        return {"gold_prices": response.json()}