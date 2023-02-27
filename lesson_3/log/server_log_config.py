import logging
from logging.handlers import TimedRotatingFileHandler

log = logging.getLogger('server_log')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
fh = TimedRotatingFileHandler('log/server_log.log',when='D', interval=1)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

th = TimedRotatingFileHandler("log/server_log.log", when='D', interval=1)

log.addHandler(fh)
log.setLevel(logging.DEBUG)