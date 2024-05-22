import datetime

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