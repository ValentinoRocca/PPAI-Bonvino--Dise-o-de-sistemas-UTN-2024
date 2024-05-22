import datetime
import Vino

class Bodega:
    def __init__(self, coordenadaUbicacion, descripcion, historia, nombre, periodoActualizacion, ultimaActualizacion):
        self.coordenadas = coordenadaUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoAct = periodoActualizacion
        self.vinos = []
        self.ultimaActualizacion = ultimaActualizacion  ## ULTIMA VEZ QUE SE ACTUALIZO
         
    def agregar_vino(self, vino):
        self.vinos.append(vino)
    
    def agregar_vinos(self, vinosAAgregar):
        for vino in vinosAAgregar:
            self.vinos.append(vino)
    
    def estaDisponible(self, fechaActual):
        ##                          1/1/2024                                    2   *       30
        fecha_limite = self.ultimaActualizacion + datetime.timedelta(days=self.periodoAct * 30)
        if fechaActual > fecha_limite:
            return True
        else:  
            return False
    
    def getCordenadasUbicacion(self):
        return self.coordenadas

    def getNombre(self):
        return self.nombre
    
    def actualizarVinos(self):
        pass
    
    def setFechaActualizacion(self, nuevaActualizacion):
        self.ultimaActualizacion = nuevaActualizacion


    def actualizarVino(vinoPropio, vinoApi, fechaActual):
        vinoPropio.precio = vinoApi.precio
        vinoPropio.imagenEtiqueta = vinoApi.imagenEtiqueta
        vinoPropio.notaCata = vinoApi.notaCata
        vinoPropio.fechaAct = fechaActual
    


    def crearVino(self, VinoAPI, fechaAct):
        nuevoVino = Vino(VinoAPI.nombre, VinoAPI.imagenEtiqueta, VinoAPI.notaCataVino, VinoAPI.añada,fechaAct)
        Vino.crearVarietal(VinoAPI.varietal)
        self.agregar_vino(nuevoVino)
    '''
    nuevoVino = Vino(act.nombre, act.imagenEtiqueta, act.notaCataVino, act.añada,bodega,hoy)
            bodega.agregar_vino(nuevoVino)
    '''

    def agregarVinos(vino):
        






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