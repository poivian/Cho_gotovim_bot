import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def init_logger():
    dir_log = Path('Logs')
    if not dir_log.exists():
        dir_log.mkdir()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    format = logging.Formatter('%(asctime)s:%(name)s:%(lineno)s:[%(levelname)s]:%(message)s')

    std = logging.StreamHandler()
    std.setLevel(logging.INFO)
    std.setFormatter(format)

    file = RotatingFileHandler(filename=dir_log / 'log.log', maxBytes=5242880, backupCount=5, encoding='utf-8')
    file.setLevel(logging.DEBUG)
    file.setFormatter(format)

    
    logger.addHandler(std)
    logger.addHandler(file)

