import logging
from datetime import datetime

# Define a custom logging formatter
class StormStyleFormatter(logging.Formatter):
    def format(self, record):
        # Custom format to resemble NestJS
        log_format = "[Storm] {pid}   - {timestamp}   [{context}] {message}"
        log_message = log_format.format(
            pid=record.process,
            timestamp=datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p"),
            context=record.name,
            message=record.getMessage()
        )
        return log_message

# Set up the logger
def setup_logger(context: str):
    # Create a logger with the context
    logger = logging.getLogger(context)
    logger.setLevel(logging.INFO)

    # Create console handler with the custom formatter
    console_handler = logging.StreamHandler()
    formatter = StormStyleFormatter()
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger
