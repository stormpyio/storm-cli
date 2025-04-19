from storm.common import Controller, Get
from services.app_service import AppService

@Controller("/")
class AppController:
    def __init__(self, app_service: AppService):
        pass

    @Get("hi")
    async def get_users(self):
        return self.app_service.say_hello()
