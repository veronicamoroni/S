import threading

# Definir semáforo
semaphore = threading.Semaphore(2)  # Ejemplo con semáforo de capacidad 2

def tarea():
    # Acceso al recurso protegido por el semáforo
    semaphore.acquire()
    
    try:
        # Lógica de la tarea
        print("Realizando tarea...")
    finally:
        # Liberar el semáforo después de completar la tarea
        semaphore.release()

# Crear hilos
thread1 = threading.Thread(target=tarea)
thread2 = threading.Thread(target=tarea)
thread3 = threading.Thread(target=tarea)

# Iniciar los hilos
thread1.start()
thread2.start()
thread3.start()

# Esperar a que los hilos terminen
thread1.join()
thread2.join()
thread3.join()

