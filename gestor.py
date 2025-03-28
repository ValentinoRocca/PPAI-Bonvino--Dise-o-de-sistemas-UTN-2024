from clases.Maridaje import *
from clases.Bodega import *
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *
from datetime import date
from persistencias.PersistenciaBodega import PersistenciaBodega
from persistencias.PersistenciaMaridaje import PersistenciaMaridaje
from persistencias.PersistenciaVino import PersistenciaVino
from persistencias.PersistenciaVinoMaridaje import PersistenciaVinoMaridaje
from persistencias.PersistenciaVarietal import PersistenciaVarietal
from clases.Bodega import Bodega
from clases.Vino import Vino
from clases.Maridaje import Maridaje
from clases.TipoUva import TipoUva
from clases.Iterators import *
#from clases import InterfazBodega

class GestorActualizarVinos:
    def __init__(self, interfaz):
        self.arregloBodegasSistema = []
        self.arregloMaridajes = []
        self.arregloUvas = []
        self.arregloVarietales = []
        self.primer_inicio = False
        self.interfazBodega = interfaz
        self.persistenciaBodega = PersistenciaBodega()
        self.persistenciaVino = PersistenciaVino()
        self.persistenciaMaridaje = PersistenciaMaridaje()
        self.persistenciaVinoMaridaje = PersistenciaVinoMaridaje()
        self.persistenciaTipoUva = PersistenciaTipoUva()
        self.persistenciaVarietal = PersistenciaVarietal()


    def obtener_vinos_de_bodega(self, nombre_bodega):
    # Buscar la bodega en el arreglo de bodegas cargadas en el sistema
        for bodega_sistema in self.arregloBodegasSistema:
            if bodega_sistema.nombre == nombre_bodega:  # Comparar el nombre directamente con el string
                return bodega_sistema.vinos  # Devolver los vinos de esa bodega
        return []  # Si no se encuentra la bodega, retornar lista vacía
    
    def cargarDatosAlSistema(self, arregloBodegas, arregloMaridajes, arregloUva):  
        
        
        for bodega in arregloBodegas:
           bodega.persistirBodega()
        
        listaBodegasBaseDatos = self.persistenciaBodega.obtener_todos()
        self.arregloBodegasSistema = self.convertirBodegas(listaBodegasBaseDatos)

        for maridaje in arregloMaridajes:
            maridaje.persistirMaridaje()
        listaMaridajes = self.persistenciaMaridaje.obtener_todos()
        self.arregloMaridajes = self.convertirMaridajes(listaMaridajes)
        
        for uva in arregloUva:
            uva.persistirTipoUva()
        listaTipoUva = self.persistenciaTipoUva.obtener_todos()
        self.arregloUvas = self.convertirTipoUva(listaTipoUva)
        
        
        listaVarietal = self.persistenciaVarietal.obtener_todos()
        self.arregloVarietales = self.convertirVarietal(listaVarietal)
        
        
        for bodega1 in self.arregloBodegasSistema:
            for bodega2 in arregloBodegas:
                if bodega1.nombre == bodega2.nombre:    
                    for vino in bodega2.vinos:
                        vino.persistirVino(bodega1)
                        objMaridajes = []
                        for maridaje in vino.maridajes:
                            objMaridajes.append(self.buscarMaridajeDescripcion(maridaje))
                            for mari in objMaridajes:
                                print("marii", mari)
                                mari.persistirVinoMaridaje(vino)

    
                        for varietal in vino.varietales:
                            tipoUvaEncontrada = self.buscarTipoUva(varietal.tipoUva)
                            varietal.persistirVarietal(tipoUvaEncontrada)
                             
                        
                            

    def buscarVarietal(self, varietal):

        for varietalSistema in self.arregloVarietales:
            if varietal.descripcion == varietalSistema.nombre:
                return varietal                        

        return None

        
    def convertirVarietal(self, listaVarietal):

        varietalesConvertidos = []

        for varietal in listaVarietal:

            tipoUva = self.persistenciaTipoUva.obtener_por_id(varietal.tipoUva_id)

            varietalObtenido = Varietal(
                descripcion=varietal.descripcion,
                porcentajeComposicion=varietal.porcentajeComposicion,
                tipoUva=tipoUva,
                id=varietal.id        
            )

            varietalesConvertidos.append(varietalObtenido)            

        return varietalesConvertidos
                        


    def convertirBodegas(self, listaBodegas):
        bodegasConvertidas = []
        for bodega in listaBodegas:

            coordenadas_str = bodega.coordenadas.strip("()")  # Eliminar los paréntesis
            coordenadas = coordenadas_str.split(",")  # Separar las coordenadas por coma
            coordenadas_tupla = (float(coordenadas[0].strip()), float(coordenadas[1].strip()))

            listaVinos = self.persistenciaVino.obtener_por_id_bodega(bodega.id)
            vinosParseados = self.convertirVinos(listaVinos)    




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

            bodegaObtenida.agregar_vinos(vinosParseados)

            bodegasConvertidas.append(bodegaObtenida)


        return bodegasConvertidas
    
    def buscarTipoUva(self, tipoUva):

        for uva in self.arregloUvas:
            if uva.nombre == tipoUva.nombre:
                return uva
                
        return None

    def convertirTipoUva(self, listaTipoUva):

        uvasConvertidas = []

        for uva in listaTipoUva:
            
            tipoUvaObtenida = TipoUva(
                descripcion=uva.descripcion,
                nombre=uva.nombre,
                id=uva.id,

            )

            uvasConvertidas.append(tipoUvaObtenida)

        return uvasConvertidas


    def convertirMaridajes(self, listaMaridajes):
        maridajesConvertidos = []

        for maridaje in listaMaridajes:

            maridajeObtenido = Maridaje(
                descripcion=maridaje.descripcion,
                nombre=maridaje.nombre,
                id=maridaje.id
            )

            maridajesConvertidos.append(maridajeObtenido)

        return maridajesConvertidos

    def obtenerMaridajesVino(self, id_vino):

        maridajesObtenidos = []

        listaMaridajes = self.persistenciaVinoMaridaje.obtener_por_id_vino(id_vino)
    
        for linea in listaMaridajes:
            maridajesObtenidos.append(self.persistenciaMaridaje.obtener_por_id(linea.maridaje_id))

        return maridajesObtenidos
    



    def convertirVinos(self, listaVinos):
        vinosConvertidos = []
        for vino in listaVinos:

            precioInt = int(vino.precio)
            añadaInt = int(vino.añada)

            maridajesVino = self.obtenerMaridajesVino(vino.id)

            vinoObtenido = Vino(
                nombre=vino.nombre,
                imagenEtiqueta=vino.imagenEtiqueta,
                notaCataVino=vino.notaCataVino,
                precio=precioInt,
                añada=añadaInt,
                fechaAct=vino.fechaAct,
                id=vino.id
            )

            for mari in maridajesVino:
                print("maridaje antes de agregar", mari.nombre)
                vinoObtenido.agregarMaridaje(mari)

            print("maridajes agregados al vino", vinoObtenido.maridajes)
            vinosConvertidos.append(vinoObtenido)


        return vinosConvertidos



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
        
        for bodegaSeleccionada in arregloBodegasParaActualizar:
            #vinosApi = bodegaSeleccionada.vinosAPI
            #self.interfazBodega.buscarVinosApi(Bogdega)
            vinosApi = self.buscarVinosApi(bodegaSeleccionada)
            
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
        api_iterator = self.crearIterador(arrayVinosApi)

        api_iterator.primero()
        # Iterar sobre todos los vinos en la API
        while api_iterator.tieneSiguiente():
            vinoApi = api_iterator.actual()

            print("indice:", api_iterator.index)
            print("vino a actualizar:", vinoApi)

            # Crear iterador para los vinos de la bodega
            Bodega.actualizarVinosBodega(vinoApi, hoy, self.arregloUvas, self)

            
            # Avanzar al siguiente vino de la API
            api_iterator.siguiente()
            print("avanzo el api iterador")
        
        # Actualizar la fecha de la última actualización de la bodega
        Bodega.setFechaActualizacion(hoy)


    # Le pasa por parametro el string nombre de un obj Maridaje y recorre todos los maridajes hasta encontrar el obj en cuestion y retornarlo
    def buscarMaridaje(self, vinoApi):
        maridajesNuevoVino = []

        for maridajeApi in vinoApi[5]:
            for maridaje in self.arregloMaridajes:
                if maridaje.sosMaridaje(maridajeApi):
                    maridajesNuevoVino.append(maridaje)
                
        return maridajesNuevoVino
        
    def buscarMaridajeDescripcion(self, maridaje):
        for maridajeSistema in self.arregloMaridajes:
            if maridaje.nombre == maridajeSistema.nombre:
                return maridajeSistema

        return None

    def crearIterador(self,arregloVino):
        api_iterator = IteradorVinosBodegaApi(arregloVino)
        return api_iterator
    