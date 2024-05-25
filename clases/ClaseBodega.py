import datetime
from clases.Vino import *


class Bodega:
    def __init__(self, coordenadaUbicacion , descripcion, historia, nombre, periodoActualizacion, ultimaActualizacion):
        self.coordenadas = coordenadaUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoAct = periodoActualizacion
        self.vinos = []
        self.vinosAPI = []
        self.ultimaActualizacion = ultimaActualizacion  ## ULTIMA VEZ QUE SE ACTUALIZO
        
         
    def agregar_vino(self, vino):
        self.vinos.append(vino)
    
    def agregar_vinos(self, vinosAAgregar):
        for vino in vinosAAgregar:
            self.vinos.append(vino)
    
    def estaDisponible(self, fechaActual):
        ##                          1/1/2024                                    2      *    30
        fecha_limite = self.ultimaActualizacion + datetime.timedelta(days=self.periodoAct * 30)
        if fechaActual > fecha_limite:
            return True
        else:  
            return False
    
    def agregarVinosApi(self, listaDeVinos):
        for arrayDeVino in listaDeVinos:
            self.vinosAPI.append(arrayDeVino)

    def getCordenadasUbicacion(self):
        return self.coordenadas

    def getNombre(self):
        return self.nombre
    
    def actualizarVinos(self):
        pass
    
    def setFechaActualizacion(self, nuevaActualizacion):
        self.ultimaActualizacion = nuevaActualizacion


    def actualizarVino(self,vinoPropio, vinoApi, fechaActual):
        vinoPropio.setPrecio(vinoApi[3])
        vinoPropio.setImagenEtiqueta(vinoApi[1])
        vinoPropio.setNotaCata(vinoApi[2])
        vinoPropio.setFechaActualizacion(fechaActual)

    def getDatosVinoBodegaSeleccionada(self):
        return self.vinos

    def crearVino(self, vinoAPI, fechaAct, maridajes, arrayDeTipoDeUva):

        varietalesAPI = vinoAPI[6]
        
        nuevoVino = Vino(vinoAPI[0], vinoAPI[1], vinoAPI[2], vinoAPI[3], vinoAPI[4], fechaAct)
        for maridaje in maridajes:
            nuevoVino.agregarMaridaje(maridaje)
                                                            
        nuevoVino.crearVarietales(varietalesAPI, arrayDeTipoDeUva)
        self.agregar_vino(nuevoVino)

        # varietalAPI [nombre, descripcion, porcentaje, tipoDeUva]
        
    
    

    def agregarVinos(self, vino):
        self.vinos.append(vino)

    def getVinosBodega(self):
        return self.vinos

    def mostrarVinos(self):
        for vino in self.vinos:
            nombre= vino.nombre
            precioNuevo= vino.precio
            notaCataVinoNuevo = vino.notaCataVino
            imagenEtiquetaNuevo = vino.imagenEtiqueta
            añada = vino.añada
            fechaActNuevo = vino.fechaAct
            
            print(nombre, ' ,', precioNuevo,' ,', notaCataVinoNuevo, ' ,',imagenEtiquetaNuevo, ' ,',fechaActNuevo,' ,', añada)


#PRUEBA
fecha1 = datetime.datetime(2024,1,1)
fecha2 = datetime.datetime(2024,5,5)
fechaAct = datetime.datetime.now()

bodega1 = Bodega(None, None, None, 'bodega1', 1, fecha1)
bodega2 = Bodega(None, None, None, 'bodega2', 2, fecha2 )


hola = bodega1.estaDisponible(fechaAct)
hola2 = bodega2.estaDisponible(fechaAct)

#print(hola)
#print(hola2)