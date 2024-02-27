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

class Error(Schema):
    message: str

class SetterBody(Schema):
    var0: str
    var1: str

@api_controller("")
class RootController:
    @route.get("")
    def get(self):
        p = Path(os.getcwd()) / settings.FILEMANAGER_BASEPATH
        dl_file = p / 'test.txt'
        response = FileResponse(dl_file.open('rb'))
        response['Content-Disposition'] = 'attachment; filename="test.txt"'
        return response

    @route.get("/{f}", response={200: None, 403: str})
    def get_file(self, f: str):
        p = Path(os.getcwd()) / settings.FILEMANAGER_BASEPATH
        dl_file = p / f
        if not dl_file.exists():
            return 403, "File not Found"
        response = FileResponse(dl_file.open('rb'))
        response['Content-Disposition'] = 'attachment; filename="test.txt"'
        return response

@api_controller("test")
class TestController:
    @route.get("")
    def get(self):
        return {'test': "is ok"}

@api_controller("set")
class SetterController:
    @route.get("/{f}", response={200: Dict, 403: str})
    def get(self, f: str):
        p = Path(os.getcwd()) / settings.FILEMANAGER_BASEPATH
        set_file = p / f
        if set_file.exists():
            return 200, {"p": f}
        return 403, "File not Fount"

    @route.post("/{f}", response={200: str, 403: str})
    def post(self, f: str, item: SetterBody):
        p = Path(os.getcwd()) / settings.FILEMANAGER_BASEPATH
        set_file = p / f
        with set_file.open('w') as f:
            toml.dump(item.dict(),f)
        return 200, "ok"
        if set_file.exists():
            return 200, {"p": f, 'info': item.dict() }
        return 403, "File not Fount"



