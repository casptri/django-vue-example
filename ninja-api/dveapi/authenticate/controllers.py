from datetime import datetime
from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from ninja_extra.permissions import IsAdminUser, IsAuthenticated
from ninja_jwt.authentication import JWTAuth
from ninja_extra import api_controller, route, permissions, http_get, ControllerBase


@api_controller("/me", auth=JWTAuth())
class InfoController:
    @route.get("")
    def info_get(self, request):
        user = request.user.__str__()
        email = request.user.email.__str__()
        return {'username': user, 'email': email}

