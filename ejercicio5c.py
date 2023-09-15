import threading

class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izquierdo, tenedor_derecho, semaforo):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedor_izquierdo = tenedor_izquierdo
        self.tenedor_derecho = tenedor_derecho
        self.semaforo = semaforo

    def run(self):
        while True:
            # Filósofo piensa
            print(f'{self.nombre} está pensando.')

            # Filósofo tiene hambre
            self.comer()

    def comer(self):
        with self.semaforo:
            # Obtener tenedores
            self.tenedor_izquierdo.acquire()
            self.tenedor_derecho.acquire()

            # Filósofo come
            print(f'{self.nombre} está comiendo.')

            # Liberar los tenedores después de comer
            self.tenedor_izquierdo.release()
            self.tenedor_derecho.release()

tenedores = [threading.Semaphore(1) for _ in range(5)]  # Crear una lista de semáforos para los tenedores
semaforo = threading.Semaphore(4)  # Crear un semáforo para controlar el acceso a la mesa

filosofos = []
for i in range(5):
    filosofo = Filosofo(f'Filósofo {i+1}', tenedores[i], tenedores[(i+1)%5], semaforo)  # Asignar tenedores y semáforo a los filósofos
    filosofos.append(filosofo)
    filosofo.start()  # Iniciar el hilo de cada filósofo