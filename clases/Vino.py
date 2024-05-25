from .Varietal import *
from .Maridaje import *

class Vino:
    def __init__(self,nombre, imagenEtiqueta, notaCataVino, precio, añada, fechaAct):
        self.nombre = nombre
        self.imagenEtiqueta = imagenEtiqueta
        self.notaCataVino = notaCataVino
        self.precio = precio
        self.añada = añada
        self.maridajes= []
        self.varietales = []#VER px es un array
        self.reseñas = []
       # self.bodega = bodega => VINO NO TIENE BODEGA
        self.fechaAct = fechaAct

    
       
    def sosVinoAActualizar(self, vinosAActualizar):
        for i in range (vinosAActualizar):
            if i.nombre == self.nombre:
                print("El vino ", self.nombre, " esta disponible para actualizar")
                return True
            else:  
                print("El vino ", self.nombre, "no esta disponible para actualizar")
                return False

#    def sosVinoAActualizar(self, vinosAActualizar):
#        for i in vinosAActualizar:
#            if i.nombre == self.nombre:
#                return True
#            else:  
#                return False ## ====> crear vino directamente

    def setPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio
        #return ("El precio ha sido actualizado, el nuevo precio del vino es: ", nuevoPrecio)

    def setNotaCata(self, nuevaNotaCata):
        self.notaCataVino = nuevaNotaCata
        #print("Se han actualizado las notas de cata del vino")

    def setImagenEtiqueta(self, nuevaImagenEtiqueta):
        self.imagenEtiqueta = nuevaImagenEtiqueta
        
    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaAct = fechaActualizacion
        #print("Se ha actualizado la fecha de actualizacion del vino")

    def agregarVarietal(self, newVarietal):
            self.varietales.append(newVarietal)
            
    def agregarMaridaje(self, newMaridaje):
            self.maridajes.append(newMaridaje)
            
    
     # varietalAPI [descripcion, porcentaje, tipoDeUva]
    def crearVarietales(self,varietales, arrayDeTipoDeUva):
        for varietal in varietales:
            tipo_Uva = varietal[2]
            tipoDeUvaObjeto = self.buscarTipoUva(arrayDeTipoDeUva, tipo_Uva)  
            nuevoVarietal = Varietal(varietal[0], varietal[1], tipoDeUvaObjeto)
            self.agregarVarietal(nuevoVarietal)
    
##falta buscarTipoUva... (respecto al nombre)
    def buscarTipoUva( self, arrayTipoDeUvaSistema, stringTipoDeUva):
         for tipoDeUva in arrayTipoDeUvaSistema:
              if tipoDeUva.nombre == stringTipoDeUva:
                   return tipoDeUva
        
        


    