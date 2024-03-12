from ninja_extra import NinjaExtraAPI

from .controller import GetterController, SetterController, FileController

devApi = NinjaExtraAPI(
        title = "FileManager",
        #csrf=True,
        urls_namespace="fileApi",
        )

devApi.register_controllers(
        GetterController,
        SetterController,
        FileController,
        )
