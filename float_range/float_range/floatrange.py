import numpy as np

def float_range(stop, step=0.1, start=0.0):
    """Yield float64 values from start to stop, inclusive, with fixed step."""
    i = np.float64(start)
    stop = np.float64(stop)
    step = np.float64(step)

    while i <= stop:
        yield float(i)
        i += step
