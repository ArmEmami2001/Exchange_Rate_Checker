from ninja_extra import api_controller, route
from .schemas import CurrencyResponseSchema
import httpx
from django.conf import settings

@api_controller('/currency', tags=['Rates'])
class CurrencyController:

    @route.get('/prices', response=CurrencyResponseSchema)
    def get_all_currencies(self):
        response = httpx.get(settings.CURRENCY_API_URL)
        response.raise_for_status()
        return {"currencies": response.json()}