from clases.Maridaje import *
from clases.Bodega import *
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *
from datetime import date
from persistencias.PersistenciaBodega import PersistenciaBodega
from clases import Bodega
from clases.Iterators import *
#from clases import InterfazBodega

class GestorActualizarVinos:
    def __init__(self, interfaz):
        self.arregloBodegasSistema = []
        self.arregloMaridajes = []
        self.arregloUvas = []
        self.primer_inicio = False
        self.interfazBodega = interfaz
        self.persistenciaBodega = PersistenciaBodega()

    
    def cargarDatosAlSistema(self, arregloBodegas, arregloMaridajes, arregloUva):  
        """
        for bodega in arregloBodegas:
           self.arregloBodegasSistema.append(bodega)
           bodega.persistirBodega()
        """
           
        listaBodegasBaseDatos = self.persistenciaBodega.obtener_todos()
        print(listaBodegasBaseDatos[0].coordenadas)
        self.arregloBodegasSistema = self.convertirBodegas(listaBodegasBaseDatos)  

        for maridaje in arregloMaridajes:
            self.arregloMaridajes.append(maridaje)

        for uva in arregloUva:
            self.arregloUvas.append(uva)

    def convertirBodegas(self, listaBodegas):
        bodegasConvertidas = []
        for bodega in listaBodegas:

            coordenadas_str = bodega.coordenadas.strip("()")  # Eliminar los paréntesis
            coordenadas = coordenadas_str.split(",")  # Separar las coordenadas por coma
            coordenadas_tupla = (float(coordenadas[0].strip()), float(coordenadas[1].strip()))

            periodoAct = int(bodega.periodoActualizacion)

            bodegaObtenida = Bodega(
                coordenadaUbicacion=coordenadas_tupla,
                descripcion=bodega.descripcion,
                historia=bodega.historia,
                nombre=bodega.nombre,
                periodoActualizacion=periodoAct,
                ultimaActualizacion=bodega.ultimaActualizacion,
                id = bodega.id
            )
            bodegasConvertidas.append(bodegaObtenida)

            print("bodega creada", bodegaObtenida)
        return bodegasConvertidas

    # funcion del gestor que incia el procesamiento del codigo
    def nuevaActualizacionVino(self, pantalla, btn_imp_click):
        if len(self.arregloBodegasSistema) != 0: 
            btn_imp_click.set(True)
            
            #Aca buscamos y guardamos todas las bodegas que se puedan Actualizar
            arregloBodegasDisponibles = []
            arregloBodegasDisponibles = self.buscarBodegasAActualizar()

            #Aca guardamos las bodegas que selec el user. Es un arreglo de tupla
            arregloBodegasSeleccionadas = []
            #Aca mostramos las Bodegas Disponibles al user
            pantalla.mostrarBodegasActDisponibles(arregloBodegasDisponibles)


            arregloBodegasSeleccionadas = pantalla.bodegas_seleccionadas


            print("arreglo de bodegas selecionadas", arregloBodegasSeleccionadas)
            #Aca guardamos en un array los objetos Bodega que el user selec (Antes teniamos los nombres de las Bodegas no los obj)
            arregloBodegasParaActualizar = []
            arregloBodegasParaActualizar = self.buscarBodegaSeleccionada(arregloBodegasSeleccionadas)

            #Aca Actualizamos las bodegas Selec y las guardamos  
            arregloBodegasActualizadas = []
            arregloBodegasActualizadas = self.buscarVinosBodegaSeleccionada(arregloBodegasParaActualizar)

            #Los obj de las bodegas Act se lo pasamos a la interfaz para que las muestre
            pantalla.mostrarResumenActualizacion(arregloBodegasActualizadas)
        else:
            return 'Las bodegas no se cargaron al sistema correctamente'

    def getFechaActual(self):
        return date.today()

    #   Aca buscamos de todas las bodegas del sistema, las que estan disponibles, 
    #   le guardamos en un array de tuplas, el nombre y las coordenadas y lo retornamos
    def buscarBodegasAActualizar(self):
        self.arregloBodegasDisp = []
        fecha_actual = self.getFechaActual()
        for bodega in self.arregloBodegasSistema:
            if bodega.estaDisponible(fecha_actual):
                self.arregloBodegasDisp.append((bodega.nombre, bodega.coordenadas))
        
        return self.arregloBodegasDisp


    #Funcion que le pasas un array de Strings de los nombres de las bodegas selec por el user y
    # y retorna un array de los objetos de esas bodegas en cuestion 
    def buscarBodegaSeleccionada(self, arrayBodegaSeleccionada):
        if len(self.arregloBodegasSistema) != 0:
            bodegasSeleccionadas = []
            for bodegaSeleccionada in arrayBodegaSeleccionada:
                for bodega in self.arregloBodegasSistema:
                    if bodega.nombre == bodegaSeleccionada[0]:
                        bodegasSeleccionadas.append(bodega)

            return bodegasSeleccionadas
        
        else:
            print('no se cargaron las bodegas en el sistema')
            
    #esta funcion es un for que por cada bodega que selec el user realice la func ActualizarVinosBodega
    def buscarVinosBodegaSeleccionada(self, arregloBodegasParaActualizar):
        bodegasActualizadas = []
        print("arreglo de bodeas para act", arregloBodegasParaActualizar[0])
        
        for bodegaSeleccionada in arregloBodegasParaActualizar:
            print("id de la bodega a actualizar", bodegaSeleccionada.id)
            #vinosApi = bodegaSeleccionada.vinosAPI
            #self.interfazBodega.buscarVinosApi(Bogdega)
            vinosApi = self.buscarVinosApi(bodegaSeleccionada)
            print("vinos obtenidos de la api", vinosApi)
            self.actualizarVinosBodega(bodegaSeleccionada, vinosApi)
            bodegasActualizadas.append(bodegaSeleccionada)

        return bodegasActualizadas
    
    def buscarVinosApi(self,bodegaSeleccionada):
        vinosApi = self.interfazBodega.getDatosVinoApi(bodegaSeleccionada)
        return vinosApi



    #Recorre los vinos api buscandolo en la bodega actual, si encuentra el vino, actualiza los datos en la bodega de nuestro sistema, si no lo encuentra lo crea y le hace un append.
    def actualizarVinosBodega(self, Bodega, arrayVinosApi):   
        hoy = self.getFechaActual()
        
        # Crear iterador para los vinos de la API
        api_iterator = IteradorVinosBodegaApi(arrayVinosApi)

        while api_iterator.tieneSiguiente():
            vinoApi = api_iterator.actual()
            existe = False

            # Crear iterador para los vinos de la bodega
            bodega_iterator = IteradorVinosBodega(Bodega.vinos)
            
            while bodega_iterator.tieneSiguiente():
                vino = bodega_iterator.actual()
                if self.sosElMismoVino(vinoApi, vino):
                    vinoActualizado = Bodega.actualizarVino(vino, vinoApi, hoy)
                    print("vino actualizado", vinoActualizado)
                    vinoActualizado.actualizarPersistencia()
                    existe = True
                    break

            # Si no existe el vino, lo crea
                if not existe:
                    maridajeAPI = self.buscarMaridaje(vinoApi)
                    vinoNuevo = Bodega.crearVino(vinoApi, hoy, maridajeAPI, self.arregloUvas)
                    print("bodega antes de persistir", Bodega)
                    vinoNuevo.persistirVino(Bodega)

                bodega_iterator.siguiente()
            
            api_iterator.siguiente()

        Bodega.setFechaActualizacion(hoy)

    # Le pasa por parametro el string nombre de un obj Maridaje y recorre todos los maridajes hasta encontrar el obj en cuestion y retornarlo
    def buscarMaridaje(self, vinoApi):
        maridajesNuevoVino = []
        for maridajeApi in vinoApi[5]:
            for maridaje in self.arregloMaridajes:
                if maridaje.sosMaridaje(maridajeApi):
                    maridajesNuevoVino.append(maridaje)
                
        return maridajesNuevoVino
        
    # Le pasa por parametro el string nombre vino y un objeto vino, valida si sus nombres son el mismo
    def sosElMismoVino(self, vinoBodegaApi, vinoBodegaSeleccionada):
        return (vinoBodegaApi[0] == vinoBodegaSeleccionada.nombre)
