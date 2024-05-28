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
        self.varietales = []
        self.reseñas = []
        self.fechaAct = fechaAct

    
       
    def sosVinoAActualizar(self, vinosAActualizar):
        for i in range (vinosAActualizar):
            if i.nombre == self.nombre:
                print("El vino ", self.nombre, " esta disponible para actualizar")
                return True
            else:  
                print("El vino ", self.nombre, "no esta disponible para actualizar")
                return False

    def setPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio


    def setNotaCata(self, nuevaNotaCata):
        self.notaCataVino = nuevaNotaCata

    def setImagenEtiqueta(self, nuevaImagenEtiqueta):
        self.imagenEtiqueta = nuevaImagenEtiqueta
        

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaAct = fechaActualizacion


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
    

    # funcion buscar en el arreglo de uvas del sistema y compara si el string del tipo de uva corresponde a alguno del sistema
    def buscarTipoUva( self, arrayTipoDeUvaSistema, stringTipoDeUva):
         for tipoDeUva in arrayTipoDeUvaSistema:
              if tipoDeUva.nombre == stringTipoDeUva:
                   return tipoDeUva
              
              
    def mostrarMaridaje(self):
        var = ''
        for maridaje in self.maridajes:
            var += maridaje.__str__()
        return var
    
    def mostrarVarietal(self):
        var = ''
        for varietal in self.varietales:
            var += varietal.__str__()
        return var
    
    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Nota Cata: {self.notaCataVino} -{self.fechaAct} - Maridajes: {self.mostrarMaridaje()} - Varietales: {self.mostrarVarietal()} "
        

        


    