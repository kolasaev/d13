import logging


class CustomHandler(logging.Handler):
    def emit(self, record):
        print("Hello")
        pass
