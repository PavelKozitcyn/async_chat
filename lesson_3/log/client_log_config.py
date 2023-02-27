import logging

log = logging.getLogger('client_log')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
fh = logging.FileHandler('log/client_log.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

log.addHandler(fh)
log.setLevel(logging.DEBUG)
