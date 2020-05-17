import scipy
from scipy import stats
import zmq
import random
import sys
import time
import numpy as np

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
test_data=[1,2,3,4,5]
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)


mean = 0
standard_deviation = 1
x_values = np.arange(-5, 5, 0.1)
y_values = scipy.stats.norm(mean, standard_deviation)
test_data = y_values.pdf(x_values)
print(test_data)
test_data[::] *= 5000
delimiter = '_'
while True:
    topic = random.randrange(9999,10005)

    rnd_test_data = test_data[::] * random.triangular(0, 2)
    int_test_data = rnd_test_data.astype(int)
    string_output = ' '.join(map(str, int_test_data))
    #s = s = ' '.join('%i'% v for v in test_data)
    messagedata = string_output
    print("%d %s" % (topic, messagedata) )
    socket.send_string(("%d %s %s" % (topic, delimiter, messagedata)))
    time.sleep(1)


