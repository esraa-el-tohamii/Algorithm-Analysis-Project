import time
import tracemalloc

def measure_performance(func, *args):
    tracemalloc.start()
    start = time.time()

    result = func(*args)

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end - start, peak / 1024
