import WebServer.run
import data_handler
from threading import Thread 

thread = Thread(target = data_handler)
thread = Thread(target = run)