
from clases.Maridaje import *
from clases.ClaseBodega import *
import datetime

#from clases.Vino import *
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *





class GestorActualizarVinos:
    def __init__(self):
        self.arregloBodegasSistema = []
        self.arregloMaridajes = []
        self.arregloUvas = []
        self.primer_inicio = False

    
    #================================================================================================================================  
    #Paso 1
    def cargarDatosAlSistema(self, arregloBodegas, arregloMaridajes, arregloUva):
        for bodega in arregloBodegas:
            self.arregloBodegasSistema.append(bodega)

        for maridaje in arregloMaridajes:
            self.arregloMaridajes.append(maridaje)

        for uva in arregloUva:
            self.arregloUvas.append(uva)



    def nuevaActualizacionVino(self, interfaz, btn_imp_click):

        if len(self.arregloBodegasSistema) != 0: 
            btn_imp_click.set(True)


            self.arreglobodegasDisponibles = []
            self.arregloBodegasDisponibles = self.buscarBodegasAActualizar(self.arregloBodegasSistema)

            print(self.arregloBodegasDisponibles)

            self.arregloBodegasSeleccionadas = []
            interfaz.mostrarBodegasActDisponibles(self.arregloBodegasDisponibles)
            self.arregloBodegasSeleccionadas = interfaz.bodegas_seleccionadas

            print(self.arregloBodegasSeleccionadas)

            self.arregloBodegasParaActualizar = []
            self.arregloBodegasParaActualizar = self.buscarBodegaSeleccionada(self.arregloBodegasSeleccionadas)

            print('bodegas para actualizar')
            print(self.arregloBodegasParaActualizar[0].nombre)

            self.arregloBodegasActualizadas = []
            self.arregloBodegasActualizadas = self.actualizarVinosDeBodegas(self.arregloBodegasParaActualizar)

            print('bodegas ACTUALIZADAS')
            print(self.arregloBodegasActualizadas[0].nombre)

            interfaz.mostrarResumenActualizacion(self.arregloBodegasActualizadas)
        else:
            return 'Las bodegas no se cargaron al sistema correctamente'
        
        
        




    #================================================================================================================================        
    #================================================================================================================================
    #Paso 2

    def getFechaActual(self):
        return date.today()

    def buscarBodegasAActualizar(self, arregloBodegasSeleccionadas): # VER EN EL DIAG DE SECUENCIA bellisimo
        self.arregloBodegasDisp = []
        fecha_actual = self.getFechaActual()
        for bodega in arregloBodegasSeleccionadas:
            if bodega.estaDisponible(fecha_actual):
                self.arregloBodegasDisp.append((bodega.nombre, bodega.coordenadas))
        
        return self.arregloBodegasDisp




    #=====================================================================================================================================
    #=====================================================================================================================================
    #Paso 5
    def buscarVinosAPI(bodegaApi):   #Obtiene los vinos actualizados y los nuevos vinos en la api
        return bodegaApi

    #SERIAN LAS BODEGAS DEL SISTEMA
    # STRING         BODEGAS

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
            
        
    #=================================================================================================================================

    #=================================================================================================================================
    #Paso 6

    def actualizarVinosDeBodegas(self, arregloBodegasParaActualizar):
        bodegasActualizadas = []
        for bodegaSeleccionada in arregloBodegasParaActualizar:
            vinosApi = bodegaSeleccionada.vinosAPI
            self.actualizarVinosBodega(bodegaSeleccionada, vinosApi)
            bodegasActualizadas.append(bodegaSeleccionada)

        return bodegasActualizadas

    def actualizarVinosBodega(self, bodega, arrayVinosApi):   #Recorre los vinos api buscandolo en la bodega actual, si encuentra el vino, actualiza los datos en la bodegade nuestro sistema, si no lo encuentra lo crea y le hace un append.
        hoy = self.getFechaActual()
        for vinoApi in arrayVinosApi:#  (vino1, vino2, vino3)
            existe = False
            for vino in bodega.vinos:#    (vino40, vin1, vino3)
                if self.sosElMismoVino(vinoApi, vino):
                    bodega.actualizarVino(vino, vinoApi, hoy) 
                    existe = True     
                    break
            
            if not existe:
                
                maridajeAPI = self.buscarMaridaje(vinoApi) 
                bodega.crearVino(vinoApi, hoy, maridajeAPI, self.arregloUvas)

        bodega.setFechaActualizacion(hoy)

    def buscarMaridaje(self, vinoApi):
        maridajesNuevoVino = []
        for maridajeApi in vinoApi[5]: #(maridaje1, 2 , 3)
            for maridaje in self.arregloMaridajes:      #(1, 2, 3, 4, 5)
                if maridaje.sosMaridaje(maridajeApi):
                    maridajesNuevoVino.append(maridaje)
                
        
        return maridajesNuevoVino
        
    def sosElMismoVino(self, vinoBodegaApi, vinoBodegaSeleccionada):
        return (vinoBodegaApi[0] == vinoBodegaSeleccionada.nombre)

    # FALTARIA LO DE CREAR UN RESUMEN DE LAS NOVEDADES
    def generarResumen(self):
        pass

    #=================================================================================================================================

''''
#Paso 7

#arrayEnofilosSistemas -> serian todos lo enofilos del sistema
arrayEnofilosSistema = []

notificacionPush = NotificacionPush("mensaje")
resumen = "resumenDeLasNovedades"

def notificarSuscripciones(bodega):
    nombresUsuariosSuscriptosABodega=[]
    for enofilo in arrayEnofilosSistema:
        if enofilo.estaSuscriptoABodega(bodega):
            nombreEnofilo = enofilo.obtenerNombreUsuario()
            nombresUsuariosSuscriptosABodega.append(nombreEnofilo)

    notificacionPush.actualizarNovedadBodega(bodega, nombresUsuariosSuscriptosABodega, resumen)
'''












#-------------------------------------------------------------------------------------------------------
#reinicio de variables
arrayVinosApi = []


vinoac1API = None
vinoac2API = None
vinoac3API = None
vinoac4API = None

#Definicion de variables
fecha = datetime.datetime(2024,1,17)
fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)
fechaHoy = datetime.datetime.now()

#bodegaApi1  = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )

bodega1 = Bodega(None, None,None, 'Bodega Malbec', 2, fecha )
bodega2 = Bodega(None, None,None, 'Bodega Toro Viejo', 2, fecha2 )
bodega3 = Bodega(None, None,None, 'Bodega Otro Loco', 2, fecha3 )

#                   0       1       2       3      4    5           6           7
#               nombre, imagen, notaCata,precio,añada, maridajes, varietales, fecha
vinoac1API = ["blue label de yoni caminante","img1", "Nota1", "3441","añada",['hamburguesa'],[["descripcion 1", "50%", "uva1"],["descripcon 6", "50%", "uva3"]],  fecha ]
vinoac2API = ["Gordasa","img2", "Nota2", "34241", "añada2",['salamazo'],["descripcon 3", "30%", "uva3"], fecha2  ]
vinoac3API = ["El desempleo","img1333", "Nota1", "3441", "añada",[ 'oooo'], ["descripcon 4", "55%", "uva4"], fecha ]
vinoac4API = ["la pobrezA","img45", "Nota45", "9241", "dsadsa", ['quesaso'],["descripcon 6", "10%", "uva3"],fecha2  ]
vinoac5API = ["malvec","img60", "Nota45", "9241", "añada5", ["pizza", "quesaso"],[["descripcion 2","20%","uva2"], ["descripcion 8 ","14%","uva5"]], fecha2  ]
vinoac6API = ["malvecBodega2","img60", "Nota45", "9241", "añada5", ["pizza", "quesaso"],[["descripcion 2","20%","uva2"], ["descripcion 8 ","14%","uva5"]], fecha2  ]
vinos7API = ["Las perdices","img60", "Nota45", "9241", "añada5", ["marquiños", "quesaso"],[["descripcion 3","330%","uva2"], ["descripcion 8 ","14%","uva5"]], fechaHoy  ]


vinoac1 = Vino("blue label de yoni caminante","img", "notas de cereza con acentuaciones graves de jamon", 3441, "30009", fecha )
vinoac2 = Vino("Gordasa","fotoDelValen", "Nota2", 34241, "añada2", fecha2  )
vinoac3 = Vino("El desempleo","img1333", "Nota1", 3441, "añada", fecha )
vinoac4 = Vino("vino El loco","img", "notas de cereza con acentuaciones graves de jamon", 3441, "30009", fecha )
vinoac5 = Vino("Lebron","fotoDelValen", "Nota2", 34241, "añada2", fecha2  )
vinoac6 = Vino("el pinto","img1333", "Nota1", 3441, "añada", fecha )
#####


arrayVinosApi = [vinoac1API,vinoac2API, vinoac3API, vinoac4API, vinoac5API]
arrayVinosApi2 = [vinoac1API,vinoac2API, vinoac3API, vinoac4API, vinos7API]

bodega1.agregarVinosApi(arrayVinosApi)
bodega2.agregarVinosApi(arrayVinosApi2)


bodega1.agregar_vino(vinoac1)
bodega1.agregar_vino(vinoac2)
bodega1.agregar_vino(vinoac3)

bodega2.agregar_vino(vinoac1)
bodega2.agregar_vino(vinoac2)
bodega2.agregar_vino(vinoac6)

arrayBodega = [bodega1, bodega2, bodega3]
#======================================================================================================================================================================
#####-------------------------------VINOS SISTEMA-----------------------------------------------------------------------------------------------------------------#####
#======================================================================================================================================================================
#---------------------------------uvas---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------# 

uva1 = TipoUva("Una uva bastante buena", "uva1")
uva2 = TipoUva("Una uva  buena", "uva2")
uva3 = TipoUva("Una uva mala", "uva3")
uva4 = TipoUva("Una uvita chica", "uva4")
uva5 = TipoUva("una pasita", "uva5")
arrayTiposDeUvaSistema = [uva1, uva2, uva3, uva4, uva5]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#varietales de nuestro sistema
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
varietal1 = Varietal("descripcion 1", "50%", uva1)
varietal2 = Varietal("descripcion 2","20%",uva2)
varietal3 = Varietal("descripcon 3", "30%", uva3) 
varietal4 = Varietal("descripcion 4", "55%", uva4)
varietal5 = Varietal("descripcion 5","35%",uva5)
varietal6 = Varietal("descripcon 6", "10%", uva3)
varietal7 = Varietal("descripcion 7", "76%", uva1)
varietal8 = Varietal("descripcion 8 ","14%",uva5)
varietal9 = Varietal("descripcon 9 ", "10%", uva4)



arrayvarietalVino1 = [varietal1, varietal2, varietal3]
arrayvarietalVino2 = [varietal4, varietal5, varietal6]
arrayvarietalVino3 = [varietal7, varietal8, varietal9]


for varietal in vinoac1.varietales:
    print("varietal vino1: ", varietal)    
print("estos fueron los varietales antes de cargar")
print("-"*50)

#Apends de varietales propios
for varietal in arrayvarietalVino1:
    vinoac1.agregarVarietal(varietal)
for varietal in arrayvarietalVino2:
    vinoac2.agregarVarietal(varietal)
for varietal in arrayvarietalVino3:
    vinoac3.agregarVarietal(varietal)
for varietal in vinoac1.varietales:
    print("varietal vin1: ", varietal)
        
print("estos fueron los varietales despues de cargar")
print("-"*50)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#MARIDAJES SISTEMA
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
maridaje1 = Maridaje('aaa','pizza')
maridaje2 = Maridaje('bbb','hamburguesa')
maridaje3 = Maridaje('ccc','quesaso')
maridaje4 = Maridaje('ddd','pinchilazo')
maridaje5 = Maridaje('eee','salamazo')

arrayMaridajesSistemas = [maridaje1,maridaje2,maridaje3,maridaje4,maridaje5]


#array Maridajes propios
arrayMaridaje1 = [maridaje1,maridaje3]
arrayMaridaje2 = [maridaje4]
arrayMaridaje3 = []
print("maridaje sistema antes de cargar")
print("-"*50)

for maridaje in vinoac1.maridajes:
    print("maridaje Nuestro 1: ", maridaje)   



for maridaje in arrayMaridaje1:
    vinoac1.agregarMaridaje(maridaje)

for maridaje in arrayMaridaje2:
    vinoac2.agregarVarietal(maridaje)

for maridaje in vinoac1.maridajes:
    print("maridaje Nuestro 1: ", maridaje)

print("maridaje sistema despues de cargar")  
print("-"*50)
#vinoac3 no tiene maridaje (relacion de 0..*)

#============================================================================================================================================================#
#####-----------------------API--------------------------------------------------------------------------------------------------------------------------#####
#VARIETALES
#------------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#MARIDAJES
#---------------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#### metodos probando 


vinosAPI = GestorActualizarVinos.buscarVinosAPI(arrayVinosApi)
#nuestrosVinos= buscarVinosBodegaSeleccionada(bodega1)      # ?? -> aca tendria que pasar por parametro el nombre de la bodega

#print("--------------PRUEBA DEL GESTOR--------------")
#bodega1.mostrarVinos()
#print('-'*100)
#bodega2.mostrarVinos()
#print('-'*100)
bodegaNoActualizacion = Bodega(None, None,None, 'Bodega Malbec', 2, fechaHoy)

arrayBodegasPrueba = [bodega1, bodega2, bodegaNoActualizacion]
arregloDePrueba = []
gestorPrueba = GestorActualizarVinos()
#arregloPrueba = gestorPrueba.actualizarVinosDeBodegas(arrayBodegasPrueba)

#print('-'*100)

#bodega2.mostrarVinos()
#print('-'*100)
#bodega2.mostrarVinos()



'''#
if __name__ == "__main__":

    from main import bodega, bodega2, bodega3

    arrayBodega = [bodega, bodega2, bodega3]       
    buscarBodegasAActualizar(arrayBodega) 
'''



#DespuesLoVemos



         



# def buscarMaridaje(vinoApi, arrayMaridajesSistemas):
#     maridajesNuevoVino = []
#     for maridajeApi in vinoApi.maridajes: #(maridaje1, 2 , 3)
#         for maridaje in arrayMaridajesSistemas:      #(1, 2, 3, 4, 5)
#             if maridaje.sosMaridaje(maridajeApi):
#                 maridajesNuevoVino.append(maridaje)

