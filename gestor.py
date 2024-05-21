from main import *
from Bodega import *
import datetime

class GestorActualizarVinos:
    def __init__(self, fechaActual):
        self.fechaActual = fechaActual
        self.bodegasDisponibles = []
        

def agregar_bodega(self, bodega):
        self.bodegasDisponibles.append(bodega)

def nuevaActualizacionVino(self):
    pass


"""fecha = datetime.datetime(2024,1,17)
fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)

bodega = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )
bodega2 = Bodega(None, None,None, 'holex', 2, fecha2 )
bodega3 = Bodega(None, None,None, 'holaa', 2, fecha3 )"""


###
"""fecha1 = datetime.datetime(2024,1,1)
fecha2 = datetime.datetime(2024,5,5)
bodegaPrueba1 = Bodega(None, None, None, 'bodega1', 1, fecha1)
bodegaPrueba2 = Bodega(None, None, None, 'bodega2', 2, fecha2 )"""
###

arrayBodega = [bodega, bodega2, bodega3]

def buscarBodegasAActualizar(arrayBodega): # VER EN EL DIAG DE SECUENCIA
    arregloBodegasDisp = []
    fecha_actual = getFechaActual()
    for bodega in arrayBodega:
        if bodega.estaDisponible(fecha_actual):
            
            arregloBodegasDisp.append(bodega)

            print(f"Nombre: {bodega.nombre}, Coordenada: {bodega.coordenadas}") 

            #retornar "bodegas" para interfaz
    return arregloBodegasDisp
    
def getFechaActual():
    return datetime.datetime.now()

#buscarBodegasAActualizar(arrayBodega)

if __name__ == "__main__":
    from main import bodega, bodega2, bodega3

    arrayBodega = [bodega, bodega2, bodega3]       
    buscarBodegasAActualizar(arrayBodega) 