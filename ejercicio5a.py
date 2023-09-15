import threading

class BufferLimitado:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.buffer = []
        self.mon = threading.Condition()

    def agregar(self, elemento):
        with self.mon:
            while len(self.buffer) >= self.capacidad:
                self.mon.wait()  # Esperar si el búfer está lleno
            self.buffer.append(elemento)
            print(f'Agregado: {elemento}')
            self.mon.notify_all()  # Notificar a otros hilos que hay elementos disponibles

    def extraer(self):
        with self.mon:
            while len(self.buffer) == 0:
                self.mon.wait()  # Esperar si el búfer está vacío
            elemento = self.buffer.pop(0)
            print(f'Extraído: {elemento}')
            self.mon.notify_all()  # Notificar a otros hilos que hay espacio disponible

buffer = BufferLimitado(5)  # Crear un búfer limitado de capacidad 5

class Productor(threading.Thread):
    def run(self):
        for i in range(10):
            buffer.agregar(i)

class Consumidor(threading.Thread):
    def run(self):
        for _ in range(10):
            buffer.extraer()

productor = Productor()
consumidor = Consumidor()
productor.start()
consumidor.start()
