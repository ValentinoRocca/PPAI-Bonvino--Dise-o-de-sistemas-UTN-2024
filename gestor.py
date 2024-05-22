#from main import *
from Bodega import *
import datetime
from Vino import *
class GestorActualizarVinos:
    def __init__(self, fechaActual):
        self.fechaActual = fechaActual
        self.bodegasDisponibles = []
        

def agregar_bodega(self, bodega):
        self.bodegasDisponibles.append(bodega)

def nuevaActualizacionVino(self):
    pass


arrayBodega = [bodega, bodega2, bodega3]

def buscarBodegasAActualizar(arrayBodega): # VER EN EL DIAG DE SECUENCIA
    arregloBodegasDisp = []
    fecha_actual = getFechaActual()
    for bodega in arrayBodega:
        if bodega.estaDisponible(fecha_actual):
            
            arregloBodegasDisp.append(bodega)
    
    return arregloBodegasDisp


def getFechaActual():
    return datetime.datetime.now()

def buscarVinosActualizados(bodegaVin):
    return bodegaVin.vinos

def actualizarVinosBodega(bodega,bodegaApi):
    pass





#Definicion de variables
fecha = datetime.datetime(2024,1,17)
fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)


bodegaApi1 = Bodega(None, None,None, 'osopanda', 2, fecha )
bodega1 = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )
bodega2 = Bodega(None, None,None, 'holex', 2, fecha2 )
bodega3 = Bodega(None, None,None, 'holaa', 2, fecha3 )

vinoac1API = Vino("blue label de yoni caminante","img1", "Nota1", 3441, "añada", bodega1, fecha )
vinoac2API = Vino("Gordasa","img2", "Nota2", 34241, "añada2", bodega1,fecha2  )
vinoac3API = Vino("El desempleo","img1333", "Nota1", 3441, "añada", bodega1, fecha )
vinoac4API = Vino("la pobrezA","img45", "Nota45", 9241, "dsadsa", bodega1,fecha2  )


vinoac1 = Vino("blue label de yoni caminante","img", "notas de cereza con acentuaciones graves de jamon", 3441, "30009", bodega1, fecha )
vinoac2 = Vino("Gordasa","fotoDelValen", "Nota2", 34241, "añada2", bodega1,fecha2  )
vinoac3 = Vino("El desempleo","img1333", "Nota1", 3441, "añada", bodega1, fecha )


bodegaApi1.agregar_vino(vinoac1API)
bodegaApi1.agregar_vino(vinoac2API)
bodegaApi1.agregar_vino(vinoac3API)
bodegaApi1.agregar_vino(vinoac4API)

bodega1.agregar_vino(vinoac1)
bodega1.agregar_vino(vinoac2)
bodega1.agregar_vino(vinoac3)
bodega1.agregar_vino(vinoac4)

#### metodos probando 



'''
if __name__ == "__main__":

    from main import bodega, bodega2, bodega3

    arrayBodega = [bodega, bodega2, bodega3]       
    buscarBodegasAActualizar(arrayBodega) 
'''