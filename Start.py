import WebServer.run as server
import data_handler as handler
from threading import Thread

if __name__ == '__main__':
    T1 = Thread(target=server.start, args=())
    T2 = Thread(target=handler.start, args=())
    T1.start()
    T2.start()
