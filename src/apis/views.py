import logging


logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"
