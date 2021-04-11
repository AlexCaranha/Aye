import logging
from win32api import OutputDebugString

class DbgViewHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
        
    def emit(self, record):
        OutputDebugString(self.format(record))

log = logging.getLogger()
log.addHandler(DbgViewHandler())

import threading
import time

def thread_function(name):
    log.warning("=> Thread %s: starting", name)
    time.sleep(2)
    log.warning("=> Thread %s: finishing", name)


if __name__ == "__main__":
    log.warning("=> Main    : before creating thread")

    x = threading.Thread(target=thread_function, args=(1,))

    log.warning("=> Main    : before running thread")
    
    x.start()

    log.warning("=> Main    : wait for the thread to finish")

    log.warning("=> Main    : all done")
