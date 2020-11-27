import DynamoService

logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ["LOGGING_LEVEL"]) )

class Sessions:
    def __init__(self):
        service = DynamoService(os.environ["SESSION_TABLE_NAME"])

    def new_session()        


# TTL attributes must use the epoch time format. 
# For example, the epoch timestamp for October 28, 2019 13:12:03 UTC is 1572268323. 
# You can use a free online converter, such as EpochConverter, to get the correct value.
# Note: Be sure that the timestamp is in seconds, not milliseconds (for example, use 1572268323 instead of 1572268323000).