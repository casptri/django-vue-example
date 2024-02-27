from ninja_extra import NinjaExtraAPI

from .controller import RootController, TestController, SetterController

devApi = NinjaExtraAPI(
        title = "FileManager",
        #csrf=True,
        urls_namespace="fileApi",
        )

devApi.register_controllers(
        RootController,
        TestController,
        SetterController,
        )
