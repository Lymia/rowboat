import time

from contextlib import contextmanager

@contextmanager
def timed(metricname, tags=None):
    start = time.time()
    try:
        yield
    except:
        raise
    finally:
        pass
