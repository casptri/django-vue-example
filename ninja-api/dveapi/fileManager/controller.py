from ninja_extra import api_controller, route, status
from ninja_extra.controllers import Detail, Id
from ninja import File
from ninja.files import UploadedFile
from ninja import Schema

from django.http import FileResponse
from django.conf import settings

from pathlib import Path
import os
from typing import Dict, List
import toml

class Error(Schema):
    message: str

class SetterBody(Schema):
    var0: str
    var1: str

@api_controller("get")
class GetterController:
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

@api_controller("ls")
class LsController:
    @route.get("/", response={200: list, 403: str})
    def get_base(self, request):
        base_path = Path(settings.FILEMANAGER_BASEPATH)
        print(base_path.resolve())
        l = []
        for entry in base_path.iterdir():
            l.append(entry.name)
        return 200, l

    @route.get("/{path:value}", response={200: list, 403: str})
    def get(self, request, value: str):
        if value[0] == "/":
            base_path = Path(settings.FILEMANAGER_BASEPATH)
        else:
            base_path = Path(settings.FILEMANAGER_BASEPATH) / value
        l = []
        for entry in base_path.iterdir():
            l.append(entry.name)
        return 200, l


@api_controller("file")
class FileController:
    def _save_file(self, file):
        base_path = Path(settings.FILEMANAGER_BASEPATH)
        data = file.read()
        file_path = base_path / file.name
        with file_path.open('wb') as f:
            f.write(data)
        return file_path

    @route.get("/{file_req}", response={200: None, 403: str})
    def get_file(self, request, file_req: str ):
        base_path = Path(settings.FILEMANAGER_BASEPATH)
        dl_file = base_path / file_req
        if not dl_file.exists():
            return 403, "File not Found"
        response = FileResponse(dl_file.open('rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_req}"'
        return response

    @route.post("", response={200: None, 403: str})
    #def upload(self, request):#, up_file: UploadedFile = File(...)):
    def upload(self, request, up_file: UploadedFile = File(...)):
        for e in request:
            print(e)
        print("Got file")
        base_path = Path(settings.FILEMANAGER_BASEPATH)
        file_name = up_file.name
        print(file_name)
        if (base_path / file_name).exists():
            return 403, "File already exists"
        self._save_file(up_file)
        return 200

