import threading
import random
import time

# Definimos un monitor para el cruce de carreteras
class IntersectionMonitor:
    def __init__(self):
        self.semaphore = threading.Semaphore(1)  # Semáforo para controlar el acceso a la intersección

    def enter_intersection(self, car_id):
        print(f'Car {car_id} is requesting entry to the intersection')
        self.semaphore.acquire()
        print(f'Car {car_id} entered the intersection')

    def exit_intersection(self, car_id):
        print(f'Car {car_id} is exiting the intersection')
        self.semaphore.release()
        print(f'Car {car_id} exited the intersection')

# Función que simula el movimiento de un coche a través de la intersección
def car_thread(car_id, intersection):
    while True:
        # Espera aleatoria antes de llegar a la intersección
        time.sleep(random.uniform(0, 2))
        
        intersection.enter_intersection(car_id)
        
        # Simula el tiempo que pasa en la intersección
        time.sleep(random.uniform(1, 3))
        
        intersection.exit_intersection(car_id)

if __name__ == '__main__':
    intersection = IntersectionMonitor()
    num_cars = 5
    
    # Creamos hilos para representar los coches
    car_threads = []
    
    for i in range(num_cars):
        car_thread_obj = threading.Thread(target=car_thread, args=(i, intersection))
        car_threads.append(car_thread_obj)
        car_thread_obj.start()
    
    # Esperamos a que todos los hilos terminen
    for car_thread_obj in car_threads:
        car_thread_obj.join()
