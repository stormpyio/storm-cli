from storm.common import Controller
from services.app_service import AppService


@Controller("/hello")  # Define base path for this controller
class UsersController():

    def __init__(self, appService: AppService):
        """
        Initialize the UsersController with the AppService instance.
        """
        pass

    def on_module_init(self):
        """
        This method is called when the module is initialized.
        """
        return self.appService.say_hello()
