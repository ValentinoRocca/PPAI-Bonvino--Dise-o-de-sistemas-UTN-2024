from declaracionesLocal import vinosApiCatena
from declaracionesLocal import vinosApiNorton
from declaracionesLocal import vinosApiLuigi
from declaracionesLocal import vinosApiAchaval
from declaracionesLocal import vinosApiTrapiche




class InterfazBodega:
    def __init__(self):

        self.bodega1api=["Bodega Catena Zapata", vinosApiCatena] 
        self.bodega2api=["Bodega Norton", vinosApiNorton]
        self.bodega3api=["Bodega Trapiche", vinosApiTrapiche]
        self.bodega4api=["Bodega Luigi Bosca", vinosApiLuigi]
        self.bodega5Api = ["Bodega Achaval Ferrer", vinosApiAchaval]    
        
        
        self.bodegasApi=[self.bodega1api, self.bodega2api, self.bodega3api, self.bodega4api, self.bodega4api, self.bodega5Api]
    
    def getDatosVinoApi(self, bodegaSeleccionada):
        for bodega in self.bodegasApi:
            if bodega[0] == bodegaSeleccionada.nombre:
                return bodega[1]

    
    
    
   