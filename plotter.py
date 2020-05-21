import matplotlib.pyplot as plt
from numba import jit


@jit  # (nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def histogrammer(input_data):
    print(input_data)
    x = range(len(input_data))
    y = input_data
    hist = plt.plot(x, y)
    return hist
