import inspect
import logging
from functools import wraps
from logging.handlers import TimedRotatingFileHandler

log = logging.getLogger('server_log')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
fh = TimedRotatingFileHandler('log/server_log.log', when='D', interval=1)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# th = TimedRotatingFileHandler("log/server_log.log", when='D', interval=1)

log.addHandler(fh)
log.setLevel(logging.DEBUG)


class MyServerLogger:
    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            log.info(
                f"Функция {func.__name__}() вызвана из функции {inspect.stack()[1][3]}()")
            return res

        return decorated
