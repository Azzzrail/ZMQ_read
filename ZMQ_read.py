import zmq


# if len(sys.argv) > 2:
#    socket.connect ("tcp://localhost:%s" % port1)


def zmq_read(port):
    # Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:%s" % port)
    topicfilter = b"ADC"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
    string = socket.recv()
    string = string.decode('utf-8')

    return string

#    with open('filename.txt', "a") as g:
#        g.write("%s\n" % string)  # Записываем имена файлов в текстовый файл
