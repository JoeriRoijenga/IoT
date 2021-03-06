from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from time import strftime
from flask import Flask, render_template, send_file, make_response, request
import sqlite3

app = Flask(__name__)

def connectDB():
	conn = sqlite3.connect('espData.db')
	return conn


def disconnectDB(conn):
	conn.close()
	conn = None


# Retrieve LAST data from database
def getLastData():
	conn = connectDB()
	curs = conn.cursor()

	for row in curs.execute("SELECT * FROM ESP_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
		press = row[3]
	
	disconnectDB(conn)
	
	return time, temp, hum, press


def getHistData (numSamples):
	conn = connectDB()
	curs = conn.cursor()

	curs.execute("SELECT * FROM ESP_data ORDER BY timestamp DESC LIMIT "+str(numSamples))
	data = curs.fetchall()
	dates = []
	temps = []
	hums = []
	press = []

	for row in reversed(data):
		dates.append(row[0])
		temps.append(row[1])
		hums.append(row[2])
		press.append(row[3])

	
	disconnectDB(conn)

	return dates, temps, hums, press

def maxRowsTable():
	conn = connectDB()
	curs = conn.cursor()

	for row in curs.execute("select COUNT(temp) from ESP_data"):
		maxNumberRows=row[0]

	disconnectDB(conn)

	return maxNumberRows


def createResponse(ys, title = "default"):
	fig = Figure()
	
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title(title)
	axis.set_xlabel("Samples")
	axis.grid(True)
	xs = range(numSamples)
	axis.plot(xs, ys)
	
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'

	return response


def templateData():
    time, temp, hum, press = getLastData()

    templateData = {
        'time'		: strftime("%H:%M:%S"),
       	'temp'		: temp,
        'hum'		: hum,
        'press'		: press,
        'numSamples': numSamples
    }

    return render_template('index.html', **templateData)


#initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples >= 51):
	numSamples = 50
	
	
# main route 
@app.route("/")
def index():
	return templateData()


@app.route('/', methods=['POST'])
def my_form_post():
    global numSamples 
    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    
    return templateData()
	

@app.route('/plot/temp')
def plot_temp():
	return createResponse(getHistData(numSamples)[1], "Temperature [°C]")


@app.route('/plot/hum')
def plot_hum():
	return createResponse(getHistData(numSamples)[2], "Humidity [%]")

@app.route('/plot/press')
def plot_press():
	return createResponse(getHistData(numSamples)[3], "Pressure [pHa]")


if __name__ == "__main__":
	start()

def start():
	app.run(host='0.0.0.0', port=80, debug=False)
