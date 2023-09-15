import multiprocessing

def proceso_hijo(numero):
    resultado = numero * 2
    print(f'El hijo ha calculado el resultado: {resultado}')

if __name__ == '__main__':
    numero = 5
    
    # Crear un proceso hijo y pasarle un número
    proceso = multiprocessing.Process(target=proceso_hijo, args=(numero,))
    proceso.start()
    proceso.join()

    print('El proceso principal ha terminado')
