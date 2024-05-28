from clases.Maridaje import *
from clases.ClaseBodega import *
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *

class GestorActualizarVinos:
    def __init__(self):
        self.arregloBodegasSistema = []
        self.arregloMaridajes = []
        self.arregloUvas = []
        self.primer_inicio = False

    
    def cargarDatosAlSistema(self, arregloBodegas, arregloMaridajes, arregloUva):  
        for bodega in arregloBodegas:
            self.arregloBodegasSistema.append(bodega)

        for maridaje in arregloMaridajes:
            self.arregloMaridajes.append(maridaje)

        for uva in arregloUva:
            self.arregloUvas.append(uva)


    # funcion del gestor que incia el procesamiento del codigo
    def nuevaActualizacionVino(self, interfaz, btn_imp_click):
        if len(self.arregloBodegasSistema) != 0: 
            btn_imp_click.set(True)

            arregloBodegasDisponibles = []
            arregloBodegasDisponibles = self.buscarBodegasAActualizar(self.arregloBodegasSistema)

            arregloBodegasSeleccionadas = []
            interfaz.mostrarBodegasActDisponibles(arregloBodegasDisponibles)
            arregloBodegasSeleccionadas = interfaz.bodegas_seleccionadas

            arregloBodegasParaActualizar = []
            arregloBodegasParaActualizar = self.buscarBodegaSeleccionada(arregloBodegasSeleccionadas)

            arregloBodegasActualizadas = []
            arregloBodegasActualizadas = self.buscarVinosBodegaSeleccionada(arregloBodegasParaActualizar)

            interfaz.mostrarResumenActualizacion(arregloBodegasActualizadas)
        else:
            return 'Las bodegas no se cargaron al sistema correctamente'

    def getFechaActual(self):
        return date.today()


    def buscarBodegasAActualizar(self, arregloBodegasSeleccionadas):
        self.arregloBodegasDisp = []
        fecha_actual = self.getFechaActual()
        for bodega in arregloBodegasSeleccionadas:
            if bodega.estaDisponible(fecha_actual):
                self.arregloBodegasDisp.append((bodega.nombre, bodega.coordenadas))
        
        return self.arregloBodegasDisp


    def buscarVinosAPI(bodegaApi):
        return bodegaApi


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
            

    def buscarVinosBodegaSeleccionada(self, arregloBodegasParaActualizar):
        bodegasActualizadas = []
        for bodegaSeleccionada in arregloBodegasParaActualizar:
            vinosApi = bodegaSeleccionada.vinosAPI
            self.actualizarVinosBodega(bodegaSeleccionada, vinosApi)
            bodegasActualizadas.append(bodegaSeleccionada)

        return bodegasActualizadas


    #Recorre los vinos api buscandolo en la bodega actual, si encuentra el vino, actualiza los datos en la bodegade nuestro sistema, si no lo encuentra lo crea y le hace un append.
    def actualizarVinosBodega(self, bodega, arrayVinosApi):   
        hoy = self.getFechaActual()
        for vinoApi in arrayVinosApi:#  (vino1, vino2, vino3)
            existe = False
            for vino in bodega.vinos:#    (vino40, vin1, vino3)
                if self.sosElMismoVino(vinoApi, vino):
                    bodega.actualizarVino(vino, vinoApi, hoy) 
                    existe = True     
                    break
            
            # si no existe el vino lo crea
            if not existe:
                maridajeAPI = self.buscarMaridaje(vinoApi) 
                bodega.crearVino(vinoApi, hoy, maridajeAPI, self.arregloUvas)

        bodega.setFechaActualizacion(hoy)


    def buscarMaridaje(self, vinoApi):
        maridajesNuevoVino = []
        for maridajeApi in vinoApi[5]:
            for maridaje in self.arregloMaridajes:
                if maridaje.sosMaridaje(maridajeApi):
                    maridajesNuevoVino.append(maridaje)
                
        return maridajesNuevoVino
        

    def sosElMismoVino(self, vinoBodegaApi, vinoBodegaSeleccionada):
        return (vinoBodegaApi[0] == vinoBodegaSeleccionada.nombre)
