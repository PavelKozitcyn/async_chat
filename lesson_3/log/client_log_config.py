import inspect
import logging
from functools import wraps

log = logging.getLogger('client_log')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
fh = logging.FileHandler('log/client_log.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

log.addHandler(fh)
log.setLevel(logging.DEBUG)


class MyLogger:
    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            log.info(
                f"Функция {func.__name__}() вызвана из функции {inspect.stack()[1][3]}()")
            return res
        return decorated
