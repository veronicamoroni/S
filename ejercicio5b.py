import threading


mutex = threading.Semaphore(1)  # Controla el acceso a la base de datos
db_access = threading.Semaphore(1)  # Controla el acceso a la variable compartida num_reads

# Variable compartida
num_reads = 0

def lector(id):
    global num_reads
    while True:
        mutex.acquire()
        num_reads += 1
        if num_reads == 1:
            db_access.acquire()
        mutex.release()

        # Leer la base de datos
        print(f'Lector {id} está leyendo la base de datos')

        mutex.acquire()
        num_reads -= 1
        if num_reads == 0:
            db_access.release()
        mutex.release()

def escritor(id):
    while True:
        db_access.acquire()

        # Escribir en la base de datos
        print(f'Escritor {id} está escribiendo en la base de datos')

        db_access.release()

# Crear lectores y escritores
num_lectores = 3
num_escritores = 2

for i in range(num_lectores):
    threading.Thread(target=lector, args=(i,)).start()

for i in range(num_escritores):
    threading.Thread(target=escritor, args=(i,)).start()