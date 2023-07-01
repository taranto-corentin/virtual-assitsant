import logging


class Logger:
    def __init__(self):
        # Define the format of the logs
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Create the log file
        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)

        # Create the logger
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

    def log_error(self, message: str):
        logging.error(message)

    def log_warning(self, message: str):
        logging.warning(message)

    def log_info(self, message: str):
        logging.info(message)
