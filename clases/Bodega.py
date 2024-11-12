from datetime import *
from clases.Vino import *
from persistencias.PersistenciaBodega import PersistenciaBodega
from clases.Iterators import *
from gestor import GestorActualizarVinos

class Bodega:
    def __init__(self, coordenadaUbicacion, descripcion, historia, nombre, periodoActualizacion, ultimaActualizacion, id=None):
        self.id = id
        self.coordenadas = coordenadaUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoAct = periodoActualizacion
        self.vinos = []
        self.vinosAPI = [] 
        self.ultimaActualizacion = ultimaActualizacion
        self.persistencia_bodega = PersistenciaBodega()
        
         
    def agregar_vino(self, vino):
        self.vinos.append(vino)
    
    def agregar_vinos(self, vinosAAgregar):
        for vino in vinosAAgregar:
            self.vinos.append(vino)
    
    def estaDisponible(self, fechaActual):
        print(fechaActual)
        fecha_limite = self.ultimaActualizacion + timedelta(days=self.periodoAct * 30)
        print(fecha_limite)
        print(self.ultimaActualizacion)
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
    
    
    def setFechaActualizacion(self, nuevaActualizacion):
        self.ultimaActualizacion = nuevaActualizacion
        self.persistencia_bodega.actualizar(self.id, ultimaActualizacion=self.ultimaActualizacion)


    def actualizarVino(self, vinoPropio, vinoApi, fechaActual):
        vinoPropio.setPrecio(vinoApi[3])
        vinoPropio.setImagenEtiqueta(vinoApi[1])
        vinoPropio.setNotaCata(vinoApi[2])
        vinoPropio.setFechaActualizacion(fechaActual)

        return vinoPropio


    def crearVino(self, vinoAPI, fechaAct, maridajes, arrayDeTipoDeUva):

        varietalesAPI = vinoAPI[6]
        
        nuevoVino = Vino(vinoAPI[0], vinoAPI[1], vinoAPI[2], vinoAPI[3], vinoAPI[4], fechaAct)
        for maridaje in maridajes:
            nuevoVino.agregarMaridaje(maridaje)
                                                            
        nuevoVino.crearVarietales(varietalesAPI, arrayDeTipoDeUva)
        self.agregar_vino(nuevoVino)

        return nuevoVino

        
    def __str__(self):
        return f"{self.nombre}, {self.descripcion}"
    

    def getDatosVinosBodega(self):
        return self.vinos

    def mostrarVinos(self):
        for vino in self.vinos:
            nombre= vino.nombre
            precioNuevo= vino.precio
            notaCataVinoNuevo = vino.notaCataVino
            imagenEtiquetaNuevo = vino.imagenEtiqueta
            añada = vino.añada
            fechaActNuevo = vino.fechaAct
            
            print('| Nombre del vino:', nombre, '|Precio Vino: ', precioNuevo,' |Notas de la cata: ', notaCataVinoNuevo, ' | Imagen de la etiqueta:',imagenEtiquetaNuevo, '|Fecha de Actualizacion:',fechaActNuevo,'|Añada: ', añada, " |")

    def persistirBodega(self):
        # Si no se ha asignado un `id`, intenta agregar la bodega
        bodega_db = self.persistencia_bodega.agregar(self)
        if bodega_db:
            self.id = bodega_db.id  # Asigna el id generado en la base de datos
        else:
            print("Esta bodega ya existe en la base de datos.")
            print("entro aca")


    def crearIterador(self):
        bodega_iterator = IteradorVinosBodega(self.vinos)
        return bodega_iterator
    
    
    def actualizarVinoBodega(self, vinoApi, hoy, arregloUvas):

        bodega_iterator = self.crearIterador()
        
        bodega_iterator.primero()

        while bodega_iterator.tieneSiguiente():

            vino = bodega_iterator.actual()


            existe = bodega_iterator.cumpleFiltro(vino, vinoApi)
            if existe:
                vinoActualizado = self.actualizarVino(vino, vinoApi, hoy)
                vinoActualizado.actualizarPersistencia()
                

            # Si no existe el vino, lo crea
            else:
                maridajeObjeto = GestorActualizarVinos.buscarMaridaje(vinoApi)

                vinoNuevo = self.crearVino(vinoApi, hoy, maridajeObjeto, arregloUvas)
                vinoNuevo.persistirVino(self) 

            bodega_iterator.siguiente()

    # Le pasa por parametro el string nombre vino y un objeto vino, valida si sus nombres son el mismo
    def sosElMismoVino(self, vinoBodegaApi, vinoBodegaSeleccionada):
        return (vinoBodegaApi[0] == vinoBodegaSeleccionada.nombre)
    

