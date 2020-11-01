import logging.handlers


class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
    # add 2 class attributes - max_visitors (200) and min_visitors (10)
    max_visitors = 200
    min_visitors = 10

    def __init__(self, visitors_num):
        self.visitors_num = visitors_num

        """
        if visitors num is bigger than max_visitors - raise TooManyVisitors error
        if visitors num is less than min_visitors - raise TooFewVisitors error
        """
        if self.visitors_num > self.max_visitors:
            raise TooManyVisitors
        elif self.visitors_num < self.min_visitors:
            raise TooFewVisitors


def make_concert(visitors_num):
    """
    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    in case if caught - log error to console and return False, in case of successful initialization - return True
    """
    try:
        Concert(visitors_num)

    except Exception as e:
        if Exception == TooFewVisitors or TooManyVisitors:
            print(f"We got Exception: {e.__class__}")
            return False
        else:
            return True


# create Logger object
# set level to debug
test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.DEBUG)

# add handler to write logs to file "test.log"

test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler("test.log", maxBytes=200, backupCount=2)
test_logger.addHandler(handler)


def log_message(message, level):
    """
    this function should use the logger defined above and log messages.
    level is the numeric representation of log level the message should refer to.
    :param message:
    :param level:
    """
    if level == 10:
        return test_logger.debug(f"{message}")
    elif level == 20:
        return test_logger.info(f"{message}")
    elif level == 30:
        return test_logger.warning(f"{message}")
    elif level == 40:
        return test_logger.error(f"{message}")
    elif level == 50:
        return test_logger.critical(f"{message}")