#
#  logger class
#
import logging
from logging import getLogger, StreamHandler, Formatter

class nk_Log():
    def __init__(self,name):
        self.logger = getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.stream_handler = StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(self.handler_format)
        self.logger.addHandler(self.stream_handler)
    def __str__(self):
        pass
    def error(self,msg):
        self.logger.error(msg)
    def debug(self,msg):
        self.logger.debug(msg)
