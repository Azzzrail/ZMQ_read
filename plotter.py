
# !/usr/bin/env python
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numba import jit
import time

# @jit  # (nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def histogrammer(input_data):
    #print(input_data)
    x = range(len(input_data))
    y = input_data
#    plt.show()
#    axes = plt.gca()
#    line, = axes.plot(x, y, 'r-')
#    line.set_xdata(x)
#    line.set_ydata(y)

    #time.sleep(0.1)

# add this if you don't want the window to disappear at the end
    #plt.show()

    matplotlib.use('Qt5Agg')

    """
    Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.
    Basic steps are:
     * Create a Canvas Element
     * Layout form
     * Display form (NON BLOCKING)
     * Draw plots onto convas
     * Display form (BLOCKING)

     Based on information from: https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
     (Thank you Em-Bo & dirck)
    """

    # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
    #
    # # Goal is to have your plot contained in the variable  "fig"
    #
    # # Fixing random state for reproducibility
    # np.random.seed(19680801)
    #
    # # make up some data in the interval ]0, 1[
    # y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    # y = y[(y > 0) & (y < 1)]
    # y.sort()
    # x = np.arange(len(y))
    #
    # # plot with various axes scales
    # plt.figure(1)
    #
    # # linear
    # plt.subplot(221)
    # plt.plot(x, y)
    # plt.yscale('linear')
    # plt.title('linear')
    # plt.grid(True)
    #
    # # log
    # plt.subplot(222)
    # plt.plot(x, y)
    # plt.yscale('log')
    # plt.title('log')
    # plt.grid(True)
    #
    # # symmetric log
    # plt.subplot(223)
    # plt.plot(x, y - y.mean())
    # plt.yscale('symlog', linthreshy=0.01)
    # plt.title('symlog')
    # plt.grid(True)
    #
    # # logit
    # plt.subplot(224)
    # plt.plot(x, y)
    # plt.yscale('logit')
    # plt.title('logit')
    # plt.grid(True)
    # plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
    #                     wspace=0.35)
    # fig = plt.gcf()
    #

    fig = matplotlib.figure.Figure(figsize=(8, 6), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(x, y)

    # ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------
    return fig

#histogrammer([1,2,3,4])