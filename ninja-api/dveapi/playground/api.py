from ninja_extra import NinjaExtraAPI

from .controller import TestController

playgroundApi = NinjaExtraAPI(
        title = "Playground",
        #csrf=True,
        urls_namespace="playgroundApi",
        )

playgroundApi.register_controllers(
        TestController,
        )
