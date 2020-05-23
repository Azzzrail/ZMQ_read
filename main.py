import sys
import matplotlib.pyplot as plt
import gui as gui  # импортируем самописные модули
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

port = gui.ask_port()
print(port)

while True:
    input_data = socket.zmq_read(port)
    plot_data, event_header = parser.parse(input_data)
    print(plot_data)
    plot_figure = plotter.histogrammer(plot_data)
    #print(plot_data)
    gui.dwraw_plot_window(plot_figure)
    #fig.canvas.draw()
    #print(plot_data)
#    plt.clf()

    # print(input_data)
