from flask import Flask
import datetime
import time
import pytz
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Worlteaaaabbbstingd'

@app.route('/timezones')
def timezones():
    current_time = time.strftime("%H:%M:%S")
    berline_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).strftime("%H:%M:%S")
    return 'Current time: ' + current_time + ', Berlin time: ' + berline_time

@app.route('/hello/<MYNAME>')
def hello(MYNAME):
    return 'Hello ' + MYNAME

if __name__ == '__main__':
    app.run(debug=True)