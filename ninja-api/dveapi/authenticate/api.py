"""
Api definition for accounts.
"""
from ninja_extra import NinjaExtraAPI, api_controller, route
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth

from .controllers import InfoController

authApi = NinjaExtraAPI(
    title="Authenticate api",
    #csrf=True,
    urls_namespace="authApi",
)

authApi.register_controllers(
    NinjaJWTDefaultController,
    InfoController,
)
