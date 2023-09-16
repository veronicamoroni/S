import threading
import time

num_filosofos = 5
tenedores = [threading.Semaphore(1) for i in range(num_filosofos)]
mutex = threading.Semaphore(1)

def filosofo(filosofo_id):
    while True:
        print(f"Filósofo {filosofo_id} está pensando.")
        time.sleep(2)
        
        mutex.acquire()
        tenedores[filosofo_id].acquire()
        tenedores[(filosofo_id + 1) % num_filosofos].acquire()
        mutex.release()
        
        print(f"Filósofo {filosofo_id} está comiendo.")
        time.sleep(2)
        
        tenedores[filosofo_id].release()
        tenedores[(filosofo_id + 1) % num_filosofos].release()

# Crear hilos para cada filósofo
for i in range(num_filosofos):
    t = threading.Thread(target=filosofo, args=(i,))
    t.start()

# Esperar a que todos los hilos terminen
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()