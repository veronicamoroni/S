
import threading
import time

database_semaphore = threading.Semaphore(1)
readers_semaphore = threading.Semaphore(0)
writers_semaphore = threading.Semaphore(0)

active_readers = 0

def reader(reader_id):
    global active_readers
    print(f'Lector {reader_id} quiere leer.')
    
    writers_semaphore.acquire()
    
    active_readers += 1
    if active_readers == 1:
        database_semaphore.acquire()
    
    writers_semaphore.release()
    readers_semaphore.release()
    
    print(f'Lector {reader_id} está leyendo.')
    time.sleep(2)
    
    readers_semaphore.acquire()
    active_readers -= 1
    if active_readers == 0:
        database_semaphore.release()
    readers_semaphore.release()
    
    print(f'Lector {reader_id} ha terminado de leer.')

def writer(writer_id):
    print(f'Escritor {writer_id} quiere escribir.')
    
    database_semaphore.acquire()
    
    print(f'Escritor {writer_id} está escribiendo.')
    time.sleep(3)
    
    database_semaphore.release()
    print(f'Escritor {writer_id} ha terminado de escribir.')

reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

for thread in reader_threads + writer_threads:
    thread.start()

for thread in reader_threads + writer_threads:
    thread.join()

    print('Todos los lectores y escritores han terminado.')
