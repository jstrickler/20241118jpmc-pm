import logging
import banana

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logging.basicConfig(

    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename='../LOGS/formatted.log',
    level=logging.INFO,
)

logger.info("this is information")
logger.warning("this is a warning")
logger.error("this is an ERROR")
value = 38.7
logger.error("Invalid value %s", value)
logger.info("this is information")
logger.critical("this is critical")
banana.peel()





