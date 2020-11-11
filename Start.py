import WebServer.run as server
import data_handler
from threading import Thread

if __name__ == '__main__':
    # Thread(target = run.start).start()
    # Thread(target = data_handler).start()
    T1 = Thread(target=server.start, args=())
    T2 = Thread(target=data_handler, args=())
    T1.start()
    T2.start()
