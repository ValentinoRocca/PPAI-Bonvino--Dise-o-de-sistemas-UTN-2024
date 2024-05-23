
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

 #SERIAN LAS BODEGAS DEL SISTEMA
# STRING         BODEGAS

def buscarBodegaSeleccionada(bodegaSeleccionada, arrayBodegasSistemas):
        
        for bodega in arrayBodegasSistemas:
            if bodega.nombre == bodegaSeleccionada[0]:
                return bodega
        
       
                
    


#=================================================================================================================================

#=================================================================================================================================
#Paso 6


def actualizarVinosBodega(bodega,arrayVinosApi):   #Recorre los vinos api buscandolo en la bodega actual, si encuentra el vino, actualiza los datos en la bodegade nuestro sistema, si no lo encuentra lo crea y le hace un append.
    hoy = getFechaActual()
    for vinoApi in arrayVinosApi:#  (vino1, vino2, vino3)
        existe = False
        for vino in bodega.vinos:#    (vino40, vin1, vino3)
            
            if sosElMismoVino(vinoApi, vino):
                bodega.actualizarVino(vino, vinoApi, hoy) 
                existe = True     
                break
        
        if not existe:

            maridajeAPI = buscarMaridaje(vinoApi, arrayMaridajesSistemas) 
            
            tiposUvaAPI = buscarTipoUva(vinoApi, arrayTiposDeUvaSistema)
            
            bodega.crearVino(vinoApi, hoy, maridajeAPI, vinoApi.varietales, arrayDeTipoDeUva)
            

def buscarTipoUva(VinoAPI, tiposDeUvaSistema):
    tipoUvaNuevoVino = []
    for varietal in VinoAPI.varietales:
        for uvaSistema in tiposDeUvaSistema:
            if varietal.tipoUva == uvaSistema.nombre:
                tipoUvaNuevoVino.append(uvaSistema)
    
    return tipoUvaNuevoVino


def buscarMaridaje(vinoApi, arrayMaridajesSistemas):
    maridajesNuevoVino = []
    for maridajeApi in vinoApi.maridajes: #(maridaje1, 2 , 3)
        for maridaje in arrayMaridajesSistemas:      #(1, 2, 3, 4, 5)
            if maridaje.sosMaridaje(maridajeApi):
                maridajesNuevoVino.append(maridaje)
            
    
    return maridajesNuevoVino
    
# nombreMaridaje
    
def sosElMismoVino(vinoBodegaApi, vinoBodegaSeleccionada):
    return (vinoBodegaApi.nombre == vinoBodegaSeleccionada.nombre)

#-------------------------------------------------------------------------------------------------------
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
#####
bodegaApi1.agregar_vino(vinoac1API)
bodegaApi1.agregar_vino(vinoac2API)
bodegaApi1.agregar_vino(vinoac3API)
bodegaApi1.agregar_vino(vinoac4API)

bodega1.agregar_vino(vinoac1)
bodega1.agregar_vino(vinoac2)
bodega1.agregar_vino(vinoac3)
arrayBodega = [bodega1, bodega2, bodega3]
#================================================================================
#####-------------------------------VINOS SISTEMA---------------------------#####
#================================================================================
#uvas
#--------------------------------------------------------------------------------# 
uva1 = TipoUva("Una uva bastante buena", "uva1")
uva2 = TipoUva("Una uva  buena", "uva2")
uva3 = TipoUva("Una uva mala", "uva3")
uva4 = TipoUva("Una uvita chica", "uva4")
uva5 = TipoUva("una pasita", "uva5")
arrayTiposDeUvaSistema = [uva1, uva2, uva3, uva4, uva5]
#--------------------------------------------------------------------------------#
#varietales de nuestro sistema
#--------------------------------------------------------------------------------#
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
    vinoac1.agregarVarietAlVino(varietal)
for varietal in arrayvarietalVino2:
    vinoac2.agregarVarietAlVino(varietal)
for varietal in arrayvarietalVino3:
    vinoac3.agregarVarietAlVino(varietal)
for varietal in vinoac1.varietales:
    print("varietal vin1: ", varietal)
        
print("estos fueron los varietales despues de cargar")
print("-"*50)
#--------------------------------------------------------------------------------#
#MARIDAJES SISTEMA
#--------------------------------------------------------------------------------#
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
    vinoac1.agregar_maridaje(maridaje)

for maridaje in arrayMaridaje2:
    vinoac2.agregarVarietAlVino(maridaje)

for maridaje in vinoac1.maridajes:
    print("maridaje Nuestro 1: ", maridaje)

print("maridaje sistema despues de cargar")  
print("-"*50)
#vinoac3 no tiene maridaje (relacion de 0..*)

#=========================================================================================================================#
#####-----------------------API------------------------------------#####
#VARIETALES
#-------------------------------------------------------------------#

varietalAPI4 = Varietal("descripcion4", "20%", "uva4")
varietalAPI5 =  Varietal("dporonga", "80%", "uva3")

arrayVarietalAPI1 = [varietal1, varietal2, varietal3]
arrayVarietalAPI2 = [varietal4, varietal5, varietal6]
arrayVarietalAPI3 = [varietal7, varietal8, varietal9]
arrayVarietalAPI4 = [varietalAPI5,varietalAPI4]

for varietal in vinoac1API.varietales:
    print("varietal API 1: ", varietal)    
print("estos fueron los varietales antes de cargar")
print("-"*50)

for varietal in arrayVarietalAPI1:
    vinoac1API.agregarVarietAlVino(varietal)
for varietal in arrayVarietalAPI2:
    vinoac2API.agregarVarietAlVino(varietal)
for varietal in arrayVarietalAPI3:
    vinoac3API.agregarVarietAlVino(varietal)
for varietal in arrayVarietalAPI4:
    vinoac4API.agregarVarietAlVino(varietal)

for varietal in vinoac1API.varietales:
    print("varietal API 1: ", varietal)    
print("estos fueron los varietales despues de cargar")
print("-"*50)
#-------------------------------------------------------------------#
#MARIDAJES
#-------------------------------------------------------------------#
arrayMaridajeAPI1 = ['pizza', 'salamazo','pinchilazo'] 
arrayMaridajeAPI2 = ['salamazo','quesaso','salamazo']
arrayMaridajeAPI3 = ['pizza','hamburguesa']
arrayMaridajeAPI4 = [] #no tiene maridaje

for maridaje in vinoac1API.maridajes:
    print("maridaje API 1: ", maridaje)   
print("maridaje API antes de cargar")  
print("-"*50)
for maridajeAPI in arrayMaridajeAPI1:
    vinoac1API.agregar_maridaje(maridajeAPI)

for maridajeAPI in arrayMaridajeAPI2:
    vinoac2API.agregar_maridaje(maridajeAPI)
    
for maridaje in arrayMaridajeAPI3:
    vinoac3API.agregar_maridaje(maridajeAPI)
#despues de cargar
for maridaje in vinoac1API.maridajes:
    print("maridaje API 1: ", maridaje)  
print("maridaje API despues de cargar")
 
print("-"*50)
#-------------------------------------------------------------------#
#### metodos probando 

def agregar_bodega(self, bodega): #  METHOD DE PRUEBA
        self.bodegasDisponibles.append(bodega)

vinosAPI = buscarVinosAPI(bodegaApi1)
#nuestrosVinos= buscarVinosBodegaSeleccionada(bodega1)      # ?? -> aca tendria que pasar por parametro el nombre de la bodega


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



         



# def buscarMaridaje(vinoApi, arrayMaridajesSistemas):
#     maridajesNuevoVino = []
#     for maridajeApi in vinoApi.maridajes: #(maridaje1, 2 , 3)
#         for maridaje in arrayMaridajesSistemas:      #(1, 2, 3, 4, 5)
#             if maridaje.sosMaridaje(maridajeApi):
#                 maridajesNuevoVino.append(maridaje)

