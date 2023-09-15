
import threading
 
contador = 0             
def incrementar():           # Función que incrementa el contador                    
    global contador
    for _ in range(200):
        contador += 1

hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=incrementar)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
print("El valor final del contador es:", contador)

