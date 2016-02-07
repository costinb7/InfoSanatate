# Logging module

import logging
import os

__all__ = ["exception", "error", "info", "debug"]

VERBOSITY_LEVEL = level=logging.DEBUG
LOG_FILE = "logging.txt"

if os.path.isfile(LOG_FILE):
    os.remove(LOG_FILE)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=VERBOSITY_LEVEL, filename=LOG_FILE)

error = logging.error
info = logging.info
debug = logging.debug
exception = logging.exception
