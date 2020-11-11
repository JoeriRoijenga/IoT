import WebServer.run
import data_handler
from threading import Thread 

thread_handler = Thread(target = data_handler)
thread_run = Thread(target = run)

thread_handler.start()
thread_run.start()