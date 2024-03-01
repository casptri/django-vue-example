from ninja_extra import api_controller, route, status
from ninja_extra.controllers import Detail, Id
from ninja import File
from ninja.files import UploadedFile
from ninja import Schema

from django.http import FileResponse
from django.conf import settings

from pathlib import Path
import os
from typing import Dict
import toml

@api_controller("")
class TestController:
    @route.get("")
    def get(self):
        return {'test': "is ok"}

    @route.get("/version")
    def get(self):
        return "0.1.0"

