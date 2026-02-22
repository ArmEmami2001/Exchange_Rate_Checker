from ninja_extra import api_controller, route
from .schemas import CryptoResponseSchema
import httpx
from django.conf import settings

@api_controller('/crypto', tags=['Cryptocurrency'])
class CryptoController:

    @route.get('/prices', response=CryptoResponseSchema)
    def get_crypto_prices(self):
        response = httpx.get(settings.CRYPTO_API_URL)
        response.raise_for_status()
        return {"crypto_prices": response.json()}