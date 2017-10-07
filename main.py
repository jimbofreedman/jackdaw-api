from gps import *
from time import *
import threading

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from math import isnan

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

gpsd = None #seting the global variable

# class GpsPoller(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.daemon = True
#         global gpsd #bring it in scope
gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
#         self.current_value = None
#         self.running = True #setting the thread running to true
#
#     def run(self):
#         global gpsd
#         while gpsp.running:
#             print('looping');
#             gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
#             #print(gpsd.fix.time)

# gpsp = GpsPoller() # create the thread
# gpsp.start()

@app.route('/')
def hello_world():
    return 'Hello, World!'

def nanToZero(num):
    if (not isinstance(num, float)):
        return num
    return 0 if isnan(num) else num

@app.route('/gps')
def gps():
    global gpsd
    i = 0
    # while (i >= 0 or isinstance(i, dictwrapper)):
    #     print('looping')
    i = gpsd.next()
    print(gpsd.fix.time)
    return jsonify({
        'latitude': nanToZero(gpsd.fix.latitude),
        'longitude': nanToZero(gpsd.fix.longitude),
        'time': nanToZero(gpsd.fix.time),
        'altitude': nanToZero(gpsd.fix.altitude),
        'eps': nanToZero(gpsd.fix.eps),
        'epx': nanToZero(gpsd.fix.epx),
        'epv': nanToZero(gpsd.fix.epv),
        'ept': nanToZero(gpsd.fix.ept),
        'speed': nanToZero(gpsd.fix.speed),
        'climb': nanToZero(gpsd.fix.climb),
        'track': nanToZero(gpsd.fix.track),
        'mode': nanToZero(gpsd.fix.mode),
        'satellites': gpsd.satellites,
    })

app.run(host='0.0.0.0', port=5000)
