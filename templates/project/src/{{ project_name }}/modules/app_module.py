from storm.common import Module
from controllers.app_controller import AppController
from services.app_service import AppService


@Module(controllers=[AppController], providers=[AppService])
class AppModule:
    pass
