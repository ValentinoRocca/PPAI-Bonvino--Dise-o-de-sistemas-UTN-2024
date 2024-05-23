
from clases.Maridaje import *
from clases.ClaseBodega import *
import datetime
from clases.Vino import *
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *
class GestorActualizarVinos:
    def __init__(self, fechaActual):
        self.fechaActual = fechaActual
        self.bodegasDisponibles = []


#================================================================================================================================  
#Paso 1
def nuevaActualizacionVino(self):
    pass

#================================================================================================================================        
#================================================================================================================================
#Paso 2

def getFechaActual():
    return datetime.datetime.now()

def buscarBodegasAActualizar(arrayBodega): # VER EN EL DIAG DE SECUENCIA bellisimo
    arregloBodegasDisp = []
    fecha_actual = getFechaActual()
    for bodega in arrayBodega:
        if bodega.estaDisponible(fecha_actual):
            arregloBodegasDisp.append([bodega.nombre,bodega.coordenadaUbicacion])
    
    return arregloBodegasDisp




#=====================================================================================================================================
#=====================================================================================================================================
#Paso 5
def buscarVinosAPI(bodegaApi):   #Obtiene los vinos actualizados y los nuevos vinos en la api
    return bodegaApi.vinos

bodegasSistema = [] #SERIAN LAS BODEGAS DEL SISTEMA
#                                        STRING         BODEGAS
def buscarVinosBodegaSeleccionada(bodegaSeleccionada, arrayBodegas): # tras seleccionar una bodega, busca la bodega en el arrayBodegas y devuelve sus vinos
    for bodega in bodegasSistema:
        if bodega.nombre == bodegaSeleccionada:
            vinosDeLaBodegaSelec = bodegaSeleccionada.getVinosBodega()

    return vinosDeLaBodegaSelec


#=================================================================================================================================

#=================================================================================================================================
#Paso 6


def actualizarVinosBodega(bodega,arrayVinosApi):   #Recorre los vinos api buscandolo en la bodega actual, si encuentra el vino, actualiza los datos en la bodegade nuestro sistema, si no lo encuentra lo crea y le hace un append.
    hoy = datetime.datetime.now()
    for vinoApi in arrayVinosApi:#  (vino1, vino2, vino3)
        existe = False
        for vino in bodega.vinos:#    (vino40, vin1, vino3)
            
            if sosElMismoVino(vinoApi, vino):
                bodega.actualizarVino(vino, vinoApi, hoy) 
                existe = True     
                break
        
        if not existe:
            #maridajeAPI = buscarMaridaje(vinoApi.maridaje) 
            bodega.crearVino(vinoApi, hoy)



# nombreMaridaje
    
def sosElMismoVino(vinoBodegaApi, vinoBodegaSeleccionada):
    return (vinoBodegaApi.nombre == vinoBodegaSeleccionada.nombre)


#reinicio de variables
bodegaApi1 = None
bodega1 = None
bodega2 = None
bodega3 = None

vinoac1API = None
vinoac2API = None
vinoac3API = None
vinoac4API = None

#Definicion de variables
fecha = datetime.datetime(2024,1,17)
fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)


bodegaApi1 = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )
bodega1 = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )
bodega2 = Bodega(None, None,None, 'holex', 2, fecha2 )
bodega3 = Bodega(None, None,None, 'holaa', 2, fecha3 )

vinoac1API = Vino("blue label de yoni caminante","img1", "Nota1", 3441, "añada",fecha )
vinoac2API = Vino("Gordasa","img2", "Nota2", 34241, "añada2",fecha2  )
vinoac3API = Vino("El desempleo","img1333", "Nota1", 3441, "añada", fecha )
vinoac4API = Vino("la pobrezA","img45", "Nota45", 9241, "dsadsa", fecha2  )

vinoac1 = Vino("blue label de yoni caminante","img", "notas de cereza con acentuaciones graves de jamon", 3441, "30009", fecha )
vinoac2 = Vino("Gordasa","fotoDelValen", "Nota2", 34241, "añada2", fecha2  )
vinoac3 = Vino("El desempleo","img1333", "Nota1", 3441, "añada", fecha )

#uvas 
uva1 = TipoUva("Una uva bastante buena", "uva1")
uva2 = TipoUva("Una uva  buena", "uva2")
uva3 = TipoUva("Una uva mala", "uva3")
uva4 = TipoUva("Una uvita chica", "uva4")
uva55 = TipoUva("una pasita", "uva5")

#varietales de nuestra  bodega1 
varietal1 = ["descripcion 1", "55%", uva1]
varietal2 = ["descripcion 2","122%",uva2]
varietal3 = ["descripcon 3", "90%", uva3] 
#varietalDe
varietal4= ["descripcion 4", "31%", uva1]
varietal5= ["descripcion 5","26%",uva2]
varietal6 = ["descripcon 6", "47%", uva3] 
 4  5 6
varietal7 = ["descripcion 77", "76%", uva1]
varietal8 =  ["descripcion 8 8","14%",uva2]
varietal9 = ["descripcon 9 9", "62%", uva3] 

#varietales de apiies de la BodeAPI
varietalAPI1 = ["descripcion 1", "55%", "uva1"]
varietalAPI2 = ["descripcion2","83%","uva2"]
varietalAPI3 = ["descripcon3", "90%", "uva3"] 


#atributo varietal de cada vino
varietalVino1 = [varietal1, varietal2, varietal3]
varietalVino2 = [varietal4, varietal5, varietal6]
Varie
a




bodegaApi1.agregar_vino(vinoac1API)
bodegaApi1.agregar_vino(vinoac2API)
bodegaApi1.agregar_vino(vinoac3API)
bodegaApi1.agregar_vino(vinoac4API)

bodega1.agregar_vino(vinoac1)
bodega1.agregar_vino(vinoac2)
bodega1.agregar_vino(vinoac3)

arrayBodega = [bodega1, bodega2, bodega3]



maridaje1 = Maridaje('aaa', 'pizza')
maridaje2 = Maridaje('bbb', 'hamburguesa')
arrayMaridaje = [maridaje1, maridaje2] 
#### metodos probando 

def agregar_bodega(self, bodega): #  METHOD DE PRUEBA
        self.bodegasDisponibles.append(bodega)

vinosAPI = buscarVinosAPI(bodegaApi1)
nuestrosVinos= buscarVinosBodegaSeleccionada(bodega1)      # ?? -> aca tendria que pasar por parametro el nombre de la bodega

bodega1.mostrarVinos()
print('-------------')
actualizarVinosBodega(bodega1, vinosAPI)
bodega1.mostrarVinos()

'''#
if __name__ == "__main__":

    from main import bodega, bodega2, bodega3

    arrayBodega = [bodega, bodega2, bodega3]       
    buscarBodegasAActualizar(arrayBodega) 
'''


#DespuesLoVemos
'''

def buscarMaridaje(vinoApi, arrayMaridajesSistemas):
    maridajesNuevoVino = []
    for maridaje in vinoApi.maridajes: (maridaje1, 2 , 3)
        for mari in arrayMaridajesSistemas:      (1, 2, 3, 4, 5)
            if maridaje.sosMaridaje(maridajeApi):
            
                maridash.append(maridaje)
    
    return maridajesNuevoVino
         

def buscarTipoDeUva(tipoDeUvaApi):
    for varietal in arrayTipoDeUva:
        if maridaje.sosMaridaje(maridajeApi):
            return maridaje
'''