from clases import Varietal

class Vino:
    def __init__(self,nombre, imagenEtiqueta, notaCataVino, precio, añada, bodega, fechaAct):
        self.nombre = nombre
        self.imagenEtiqueta = imagenEtiqueta
        self.notaCataVino = notaCataVino
        self.precio = precio
        self.añada = añada
        self.maridaje= []
        self.varietal = []
        self.reseñas = []
        self.bodega = bodega
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
        return ("El precio ha sido actualizado, el nuevo precio del vino es: ", nuevoPrecio)
    def setNotaCata(self, nuevaNotaCata):
        self.notaCataVino = nuevaNotaCata
        print("Se han actualizado las notas de cata del vino")
    def setImagenEtiqueta(self, nuevaImagenEtiqueta):
        self.imagenEtiqueta = nuevaImagenEtiqueta
    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaAct = fechaActualizacion
        print("Se ha actualizado la fecha de actualizacion del vino")
    def crearVarietal(self, newVarietal):
        esVarietal = isinstance(newVarietal, Varietal)
        if esVarietal:
            self.varietal.append(newVarietal)
            print("Se ha actualizado el varietal del vino")
        else:
            print("El objeto ingresado no es de la clase varietal, no se han realizado cambios...")