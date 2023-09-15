import threading

class Monitor:
    def __init__(self):
        self.semaphore = threading.Semaphore(0)
        self.mutex = threading.Lock()
        self.data = None

    def set_data(self, value):
        with self.mutex:
            self.data = value
            self.semaphore.release()

    def get_data(self):
        self.semaphore.acquire()
        with self.mutex:
            return self.data

monitor = Monitor()

def producer():
    data = "Hola bienvenidos a Sistemas Operativos!"
    monitor.set_data(data)

def consumer():
    data = monitor.get_data()
    print(data)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
