import sys

import matplotlib.pyplot as plt

import ZMQ_read as socket
import parser as parser
import plotter as plotter

# port = "37000"

plot_data = []

if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

print(port)
while True:
    input_data = socket.zmq_read(port)
    plot_data, event_header = parser.parse(input_data)
    plot = plotter.histogrammer(plot_data)
    plt.show()
    print(plot_data)
    # print(input_data)
