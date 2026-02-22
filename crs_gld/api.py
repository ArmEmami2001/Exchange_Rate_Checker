import sys
from ninja_extra import NinjaExtraAPI
from crs.controllers import CurrencyController
from gld.controllers import GoldController
from crp.controllers import CryptoController
api = NinjaExtraAPI(
    title="Currency API",
    version="1.0.0",
    description="Currency API using Ninja Extra"
)
api.register_controllers(CurrencyController)
api.register_controllers(GoldController)
api.register_controllers(CryptoController)

