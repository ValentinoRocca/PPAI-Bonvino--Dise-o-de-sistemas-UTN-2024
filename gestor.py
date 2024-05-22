#from main import *

from clases import Bodega 
import datetime
from clases import Vino
class GestorActualizarVinos:
    def __init__(self, fechaActual):
        self.fechaActual = fechaActual
        self.bodegasDisponibles = []
        

def agregar_bodega(self, bodega):
        self.bodegasDisponibles.append(bodega)

def nuevaActualizacionVino(self):
    pass




def buscarBodegasAActualizar(arrayBodega): # VER EN EL DIAG DE SECUENCIA
    arregloBodegasDisp = []
    fecha_actual = getFechaActual()
    for bodega in arrayBodega:
        if bodega.estaDisponible(fecha_actual):
            
            arregloBodegasDisp.append(bodega)
    
    return arregloBodegasDisp


def getFechaActual():
    return datetime.datetime.now()

def buscarVinosActualizar(bodegaVin):
    return bodegaVin.vinos

def actualizarVinosBodega(bodega,bodegaApi):
    hoy = datetime.datetime.now()
    existe = False
    for act in bodegaApi:#(vino1, vino2, vino3)
        for vino in bodega:#(vino1, vin40, vino3)
            if sosElMismoVino(act, vino):
                bodega.actualizarVino(vino, act, hoy)
                existe = True
                print("El vino ", act.nombre, "fue actualizado con datos del ", hoy)
        if not existe:
            bodega.crearVino(act, hoy)
            print("El vino ", act.nombre, " fue agregado a la bodega.")

def sosElMismoVino(vinoBodegaApi, vinoBodegaSeleccionada):
    return vinoBodegaApi.nombre == vinoBodegaSeleccionada.nombre

#Definicion de variables
fecha = datetime.datetime(2024,1,17)
fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)


bodegaApi1 = Bodega(None, None,None, 'osopanda', 2, fecha )
bodega1 = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )
bodega2 = Bodega(None, None,None, 'holex', 2, fecha2 )
bodega3 = Bodega(None, None,None, 'holaa', 2, fecha3 )

vinoac1API = Vino("blue label de yoni caminante","img1", "Nota1", 3441, "añada",fecha )
vinoac2API = Vino("Gordasa","img2", "Nota2", 34241, "añada2",fecha2  )
vinoac3API = Vino("El desempleo","img1333", "Nota1", 3441, "añada", fecha )
vinoac4API = Vino("la pobrezA","img45", "Nota45", 9241, "dsadsa", fecha2  )

arregloDeVinos= [vinoac1API, vinoac2API, vinoac3API] 
bodega1.agregar_vinos(arregloDeVinos)

vinoac1 = Vino("blue label de yoni caminante","img", "notas de cereza con acentuaciones graves de jamon", 3441, "30009", fecha )
vinoac2 = Vino("Gordasa","fotoDelValen", "Nota2", 34241, "añada2", fecha2  )
vinoac3 = Vino("El desempleo","img1333", "Nota1", 3441, "añada", fecha )


bodegaApi1.agregar_vino(vinoac1API)
bodegaApi1.agregar_vino(vinoac2API)
bodegaApi1.agregar_vino(vinoac3API)
bodegaApi1.agregar_vino(vinoac4API)

bodega1.agregar_vino(vinoac1)
bodega1.agregar_vino(vinoac2)
bodega1.agregar_vino(vinoac3)


#arrayBodega = [bodega, bodega2, bodega3]
#### metodos probando 



'''
if __name__ == "__main__":

    from main import bodega, bodega2, bodega3

    arrayBodega = [bodega, bodega2, bodega3]       
    buscarBodegasAActualizar(arrayBodega) 
'''