from storm.common import Injectable


@Injectable()
class AppService():

    def say_hello(self):
        """
        This method returns a greeting message.
        """
        return "Hello, World!"
