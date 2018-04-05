import logging
from tasks import test_task


logger = logging.getLogger("default")


def index():
    test_task.delay()
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"
